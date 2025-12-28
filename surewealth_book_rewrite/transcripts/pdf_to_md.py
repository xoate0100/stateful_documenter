import os
import sys
import json
import logging
import hashlib
import shutil
from pathlib import Path
from datetime import datetime
from concurrent.futures import ProcessPoolExecutor
from contextlib import contextmanager

# Dependencies: pip install pymupdf tqdm
import pymupdf as fitz
from tqdm import tqdm

# --- Configuration ---
INPUT_DIR = Path(".")  # Current directory (transcripts)
OUTPUT_DIR = Path("./markdown_export")
STATE_FILE = Path("./conversion_state.json")
LOG_FILE = Path("./conversion.log")

# Setup Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler(LOG_FILE), logging.StreamHandler(sys.stdout)]
)

class ConversionManager:
    def __init__(self):
        self.state = self._load_state()
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    def _load_state(self):
        if STATE_FILE.exists():
            try:
                with open(STATE_FILE, 'r') as f:
                    return json.load(f)
            except Exception as e:
                logging.error(f"Failed to load state file: {e}. Starting fresh.")
        return {}

    def _save_state(self):
        """Atomic write for state file."""
        temp_state = STATE_FILE.with_suffix('.tmp')
        with open(temp_state, 'w') as f:
            json.dump(self.state, f, indent=4)
        temp_state.replace(STATE_FILE)

    def get_file_hash(self, filepath):
        """Check if file content changed."""
        hash_sha256 = hashlib.sha256()
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_sha256.update(chunk)
        return hash_sha256.hexdigest()

    @contextmanager
    def atomic_write(self, target_path):
        """Ensures file is only created if the process completes successfully."""
        temp_path = target_path.with_suffix('.tmp')
        try:
            yield temp_path
            # On success, swap temp to real
            if temp_path.exists():
                temp_path.replace(target_path)
        finally:
            if temp_path.exists():
                temp_path.unlink()

    def convert_file(self, pdf_path: Path):
        try:
            file_id = str(pdf_path.relative_to(INPUT_DIR))
            current_hash = self.get_file_hash(pdf_path)

            # Idempotency Check
            if file_id in self.state and self.state[file_id]['hash'] == current_hash:
                if (OUTPUT_DIR / f"{pdf_path.stem}.md").exists():
                    return "skipped"

            output_path = OUTPUT_DIR / f"{pdf_path.stem}.md"

            with self.atomic_write(output_path) as temp_out:
                # Actual Conversion Logic
                doc = fitz.open(str(pdf_path))
                md_text = ""
                for page_num, page in enumerate(doc, start=1):
                    md_text += f"# Page {page_num}\n\n"
                    # Try markdown format first, fallback to text
                    try:
                        page_text = page.get_text("markdown")
                    except:
                        # Fallback to plain text if markdown not supported
                        page_text = page.get_text()
                        # Basic markdown formatting
                        lines = page_text.split('\n')
                        formatted_lines = []
                        for line in lines:
                            line = line.strip()
                            if line:
                                formatted_lines.append(line)
                        page_text = '\n\n'.join(formatted_lines)
                    md_text += page_text
                    md_text += "\n\n"
                doc.close()
                with open(temp_out, 'w', encoding='utf-8') as f:
                    f.write(md_text)

            # Update State
            self.state[file_id] = {
                'hash': current_hash,
                'converted_at': datetime.now().isoformat()
            }
            self._save_state()
            return "success"

        except Exception as e:
            import traceback
            logging.error(f"Failed to convert {pdf_path}: {str(e)}")
            logging.error(traceback.format_exc())
            return "error"

def main():
    manager = ConversionManager()
    pdf_files = list(INPUT_DIR.glob("*.pdf"))
    
    if not pdf_files:
        print("No PDF files found in input directory.")
        return

    print(f"Starting conversion of {len(pdf_files)} files...")
    
    results = {"success": 0, "skipped": 0, "error": 0}
    
    # ProcessPoolExecutor for CPU-bound PDF parsing
    with tqdm(total=len(pdf_files), desc="Converting", unit="file") as pbar:
        for pdf in pdf_files:
            status = manager.convert_file(pdf)
            results[status] += 1
            pbar.update(1)

    print(f"\nTask Complete!")
    print(f"Processed: {results['success']} | Skipped: {results['skipped']} | Errors: {results['error']}")

if __name__ == "__main__":
    main()