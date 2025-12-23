# Technical Provenance System

**Source:** MUDP.md, Lines ~637-651, ~2000-2100, ~3972-4015  
**Extracted:** 2025-12-22  
**Status:** Technical Implementation Guide

---

## Overview

The Technical Provenance System creates an auditable chain of custody and authenticity for all images of your children. This system provides technical proof that courts recognize as authoritative, enabling you to prove ownership, derivation, and timeline of images.

**Key Principle:** Steganography's role is **not preventative**, it's **evidentiary**. The system provides proof after the fact, not protection before misuse.

---

## Core Components

### 1. Cryptographic Hashing

**Purpose:** Create unique fingerprints for every original image

**Hash Types:**

#### SHA-256 (Cryptographic Hash)
- **Use:** Primary identification and verification
- **Properties:**
  - Unique fingerprint for each image
  - One-way function (cannot reverse)
  - Detects any modification
  - Standard in legal proceedings
- **Implementation:**
  - Generate hash of original image file
  - Store hash in registry
  - Use for verification and matching

#### Perceptual Hashes (Fuzzy Matching)
- **pHash (Perceptual Hash):** Survives transformations, compression, resizing
- **dHash (Difference Hash):** Detects similar images with modifications
- **aHash (Average Hash):** Fast similarity detection
- **Use:** Detect derived images even after AI processing
- **Properties:**
  - Survives image transformations
  - Detects similar images
  - Useful for AI-generated derivatives

---

### 2. Hash Boundary System (HBS)

**Purpose:** Comprehensive hash-based identification system

**Components:**

#### Private Database
Maintain a private database containing:
- Cryptographic hashes of every original image
- Perceptual hashes (pHash, dHash, aHash) for fuzzy matching
- Embedding vectors (FaceNet, ArcFace) for similarity detection

#### Why This Matters

If an AI model or app generates a sexualized deepfake, you can show:

> "This output has a >92% embedding similarity to my child, using the same biometric facial signature embedded in our registry."

**This converts the argument from:**
- _"It's just AI, not real."_

**to:**
- **"It is a derivative biometric asset originating from a unique, registered, timestamped, provably-identifiable face."**

**Result:** You are now in _biometric identity misuse_ territory — a vastly more serious domain.

---

### 3. Embedding Vectors (AI-Based Similarity Detection)

**Purpose:** Advanced similarity detection using AI models

**Technologies:**
- **FaceNet:** Face recognition embeddings
- **ArcFace:** Advanced face recognition
- **Other:** Any facial recognition embedding system

**Use Cases:**
- Prove derivation from original images
- Show biometric similarity
- Establish identity connection
- Support legal claims

**Advantages:**
- Works even after heavy AI processing
- Provides similarity percentages
- Court-recognized evidence
- Biometric-level proof

---

### 4. Watermarking Systems

**Purpose:** Additional identification layer (optional but helpful)

**Types:**

#### Invisible Watermarks
- **Robust invisible watermark** in pixels
- **Cryptographic token** embedded (e.g., 128-bit ID)
- **Survives:** Compression, light filters, small crops
- **Does NOT survive:** Heavy AI processing, complete re-rendering

#### Watermarking Strategy
- Each image gets unique ID or family-wise ID
- Example: `FAMILY_ID + per-photo nonce`
- Store watermark ID in registry
- Use for additional proof layer

**Limitations:**
- AI nudify models don't care about watermarks
- Watermarks do NOT survive AI processing
- Steganographic fingerprints do NOT survive AI processing
- C2PA-style provenance metadata will NOT survive AI processing

**However:** If YOU maintain provenance (hashes, timestamped originals, watermark IDs), you can still prove:
- "This real photograph is mine."
- "This AI-generated sexualized image was created using (or is derived from) my child's likeness."
- "Here is the economic and reputational harm, and proof of derivation."

---

### 5. Cryptographic Signing

**Purpose:** Prove authenticity and ownership

**Approach:**
- Compute cryptographic hash (SHA-256) of original file
- Sign hash with private key (GPG or similar)
- Store signature in registry or metadata
- Can prove you made it

**Integration:**
- Works alongside watermarking
- Provides additional proof layer
- Can be used in legal proceedings
- Establishes timeline

---

### 6. Provenance Registry

**Purpose:** Organized tracking system for all images

**Registry Contents:**

For each published photo, record:
- **Hash** (SHA-256)
- **Perceptual hashes** (pHash, dHash, aHash)
- **Watermark ID** (if used)
- **Where posted** (platform, URL)
- **Timestamp** (publication date/time)
- **Embedding vectors** (if using AI similarity)
- **Original file location** (private archive)
- **Metadata** (camera info, date taken, etc.)

**Registry Format:**
- Database (SQLite, PostgreSQL, etc.)
- Spreadsheet (Excel, Google Sheets)
- JSON/YAML files
- Custom registry system

**Maintenance:**
- Update immediately upon publication
- Maintain chronological list
- Cross-reference with contracts
- Link to economic harm documentation

---

### 7. Chain-of-Custody Procedures

**Purpose:** Ensure immediate use as evidence

**Procedures:**
1. **Original Storage:**
   - Keep raw originals offline or in private cloud
   - Never publicly accessible
   - Maintain backup copies
   - Document storage location

2. **Export Process:**
   - Create web version:
     - Downscaled
     - Robust-watermarked (if using)
     - Has hash and entry in registry
   - Only web versions go online

3. **Verification Process:**
   - If suspicious image appears:
     - Download suspicious image
     - Try to extract watermark (if present)
     - Compare hash to stored hashes
     - Run perceptual hash comparison
     - Check embedding vector similarity
     - Look up in registry

4. **Evidence Preparation:**
   - Create "Exhibit Packet" template
   - Include:
     - Original image with hash
     - Suspicious image
     - Hash comparison results
     - Registry entry
     - Timeline documentation
     - Similarity analysis

---

## Implementation Workflow

### Phase 1: Setup

1. **Choose Hash Tools:**
   - SHA-256 generator (built into most systems)
   - Perceptual hash library (Python: `imagehash`, etc.)
   - Face recognition library (FaceNet, ArcFace)

2. **Set Up Registry:**
   - Choose storage format (database, spreadsheet, files)
   - Create schema/structure
   - Set up backup system

3. **Configure Watermarking (Optional):**
   - Choose watermarking tool
   - Set up embedding system
   - Configure ID generation

### Phase 2: For Each Image

1. **Before Publication:**
   - Generate SHA-256 hash
   - Generate perceptual hashes
   - Generate embedding vectors (if using)
   - Add watermark (if using)
   - Store original in private archive

2. **Create Registry Entry:**
   - Record all hashes
   - Record watermark ID
   - Record timestamp
   - Record original location

3. **Export for Publication:**
   - Create web version (downscaled)
   - Apply watermark (if using)
   - Generate final hash
   - Update registry with publication info

4. **After Publication:**
   - Record where posted
   - Record URL (if applicable)
   - Update registry
   - Link to contracts/valuations

### Phase 3: Monitoring & Detection

1. **Set Up Monitoring:**
   - Reverse image search alerts
   - Face recognition monitoring (if using)
   - Automated hash checking
   - OSINT monitoring tools

2. **Detection Process:**
   - Receive alert or discover suspicious image
   - Download suspicious image
   - Run hash comparisons
   - Check embedding similarity
   - Verify against registry
   - Document findings

3. **Evidence Collection:**
   - Create exhibit packet
   - Document chain of custody
   - Prepare for legal use

---

## Advanced Systems

### Hash Boundary System (HBS) for Child Images

**Complete System:**
- Private database with all hash types
- Perceptual hashes for fuzzy matching
- Embedding vectors for similarity detection
- Automated comparison tools
- Alert system for matches

**Benefits:**
- Proves derivation even after AI processing
- Biometric-level identification
- Court-recognized evidence
- Comprehensive protection

---

### Child Identity Watcher (OSINT Monitoring)

**Purpose:** Instant detection of misuse

**Tools:**
- PimEyes (used safely)
- Custom face-recognition embedding search
- Python scripts
- AWS Rekognition
- Reverse image search APIs

**Configuration:**
- Alert only YOU
- Do not publish anything
- Private monitoring only
- Automated alerts

**Benefits:**
- Instant detection
- Early warning system
- Proactive protection
- Evidence collection

---

## Technical Tools & Libraries

### Hash Generation
- **SHA-256:** Built into most systems (OpenSSL, Python hashlib, etc.)
- **Perceptual Hashes:** Python `imagehash` library
- **Face Recognition:** FaceNet, ArcFace, OpenFace

### Watermarking
- Open-source libraries (Python)
- Commercial libraries (may be proprietary)
- Academic research tools

### Registry Systems
- **Databases:** SQLite, PostgreSQL, MySQL
- **Spreadsheets:** Excel, Google Sheets
- **Files:** JSON, YAML, CSV
- **Custom:** Build your own system

### Monitoring Tools
- **Face Recognition:** PimEyes, AWS Rekognition, custom
- **Reverse Image Search:** Google, TinEye, custom APIs
- **OSINT Tools:** Various monitoring services

---

## Legal Considerations

### Evidence Admissibility
- Hashes are court-recognized as authoritative
- Chain of custody is critical
- Documentation must be complete
- Timestamps must be accurate

### Privacy
- Don't embed personal info in stego payload
- Stick to random IDs that only you can map
- Protect registry data
- Secure storage of originals

### Limitations
- Watermarks don't prevent misuse
- Technical proof is evidentiary, not preventative
- AI tools can strip watermarks
- Social media mangles images

---

## Best Practices

### 1. Always Maintain Originals
- Keep raw originals offline
- Never publicly accessible
- Maintain backups
- Document storage

### 2. Hash Before Publication
- Generate all hashes before posting
- Record in registry immediately
- Never skip this step

### 3. Update Registry Continuously
- Add entry for every published image
- Update with publication details
- Maintain chronological order
- Cross-reference with contracts

### 4. Regular Backups
- Backup registry regularly
- Backup original images
- Test restoration process
- Store backups securely

### 5. Documentation
- Document all procedures
- Maintain chain of custody
- Record all actions
- Prepare exhibit packets

---

## Integration with Other Systems

### Economic Contracts
- Link registry entries to modeling contracts
- Track economic value
- Document commercial use

### Legal Framework
- Use hashes as evidence
- Support legal claims
- Prove derivation
- Establish timeline

### Rapid Response
- Quick hash verification
- Fast evidence preparation
- Immediate exhibit packet creation
- Support legal notices

---

## Related Documents

- [Four-Pillar Architecture](../strategic/four_pillars.md)
- [Implementation Phases](../../plans/implementation_phases.yaml)
- [Crisis Playbook](../operational/crisis_playbook.md)
- [Binder Structure](../../plans/binder_structure.yaml)

---

## Notes

- This system is **evidentiary**, not preventative
- Technical proof enables legal claims
- Multiple hash types provide redundancy
- Registry is critical for organization
- Chain of custody ensures admissibility

