#!/usr/bin/env python3
"""
QR Code Generator
Generates QR codes for tools, landing pages, and resources with tracking

Usage:
    python generate_qr.py --tool lifetime_tax_calculator --chapter 2 --output qr_codes/
"""

import argparse
import qrcode
from pathlib import Path
from typing import Dict, Any
import yaml
from urllib.parse import urlencode


class QRGenerator:
    """Generate QR codes with tracking parameters"""
    
    def __init__(self, config_file: Path = Path("qr_system.yaml")):
        with open(config_file, 'r') as f:
            self.config = yaml.safe_load(f)
    
    def build_url(self, destination_type: str, destination_id: str, 
                  chapter: int = None, page: int = None, 
                  campaign: str = None) -> str:
        """Build URL with tracking parameters"""
        base_pattern = self.config['qr_system']['destinations'][destination_type]['pattern']
        
        # Replace placeholders
        url = base_pattern.format(
            tool_id=destination_id,
            page_id=destination_id,
            resource_id=destination_id
        )
        
        # Add tracking parameters
        params = {'source': 'book'}
        if chapter:
            params['chapter'] = chapter
        if page:
            params['page'] = page
        if campaign:
            params['campaign'] = campaign
        
        # Add params to URL
        if '?' in url:
            url += '&' + urlencode(params)
        else:
            url += '?' + urlencode(params)
        
        return url
    
    def generate_qr(self, url: str, output_path: Path, 
                    size: int = 300, logo_path: Path = None) -> Path:
        """Generate QR code image"""
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Resize if needed
        if size != 300:
            img = img.resize((size, size))
        
        # Add logo if provided
        if logo_path and logo_path.exists():
            # TODO: Implement logo embedding
            pass
        
        # Save
        img.save(output_path)
        return output_path
    
    def generate_for_tool(self, tool_id: str, chapter: int, 
                         output_dir: Path, page: int = None) -> Path:
        """Generate QR code for a calculator/tool"""
        url = self.build_url('calculators', tool_id, chapter, page)
        output_path = output_dir / f"qr_{tool_id}_ch{chapter}.png"
        return self.generate_qr(url, output_path)
    
    def generate_for_landing_page(self, page_id: str, chapter: int,
                                  output_dir: Path) -> Path:
        """Generate QR code for a landing page"""
        url = self.build_url('landing_pages', page_id, chapter)
        output_path = output_dir / f"qr_landing_{page_id}_ch{chapter}.png"
        return self.generate_qr(url, output_path)


def main():
    parser = argparse.ArgumentParser(description="Generate QR codes")
    parser.add_argument("--tool", help="Tool ID")
    parser.add_argument("--landing-page", help="Landing page ID")
    parser.add_argument("--chapter", type=int, required=True, help="Chapter number")
    parser.add_argument("--page", type=int, help="Page number")
    parser.add_argument("--output", default="qr_codes", help="Output directory")
    
    args = parser.parse_args()
    
    generator = QRGenerator()
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    if args.tool:
        qr_path = generator.generate_for_tool(args.tool, args.chapter, output_dir, args.page)
        print(f"QR code generated: {qr_path}")
        print(f"URL: {generator.build_url('calculators', args.tool, args.chapter, args.page)}")
    elif args.landing_page:
        qr_path = generator.generate_for_landing_page(args.landing_page, args.chapter, output_dir)
        print(f"QR code generated: {qr_path}")


if __name__ == "__main__":
    main()

