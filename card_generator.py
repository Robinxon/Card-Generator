#!/usr/bin/env python3
"""
Card Generator - Generate PDF files with numbered cards for printing

This script generates a PDF file containing double-sided cards with numbers.
Both sides display the number. The front side has a black border for cutting
guidance. Optionally, numbers can have an underline.
"""

import argparse
import os
from typing import List, Tuple
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


class CardConfig:
    """Configuration for card generation"""
    def __init__(self, width_mm: float = 63, height_mm: float = 88, font: str = 'Helvetica-Bold', font_size: float = None, underline: bool = False):
        """
        Initialize card configuration
        
        Args:
            width_mm: Card width in millimeters (default: 63mm, standard poker card)
            height_mm: Card height in millimeters (default: 88mm, standard poker card)
            font: Font name or path to .ttf/.otf file (default: Helvetica-Bold)
            font_size: Font size in points (default: None, auto-calculated)
            underline: Whether to underline numbers (default: False)
        """
        self.width = width_mm * mm
        self.height = height_mm * mm
        self.border_width = 0.1 * mm  # Border thickness for cutting guide
        self.font = font
        self.font_name = None  # Will be set when registering custom fonts
        self.font_size = font_size  # Custom font size in points (None = auto-calculate)
        self.underline = underline  # Whether to underline numbers


class CardGenerator:
    """Generator for numbered cards PDF"""
    
    def __init__(self, config: CardConfig):
        """
        Initialize card generator
        
        Args:
            config: CardConfig object with card dimensions
        """
        self.config = config
        self.page_width, self.page_height = A4
        self._register_font()
    
    def _register_font(self):
        """Register custom font if provided as a file path"""
        font = self.config.font
        
        # Check if font is a file path (.ttf or .otf)
        if font.endswith(('.ttf', '.TTF', '.otf', '.OTF')):
            if os.path.exists(font):
                # Extract font name from file path
                font_basename = os.path.basename(font)
                font_name = os.path.splitext(font_basename)[0]
                
                try:
                    # Register the custom font
                    pdfmetrics.registerFont(TTFont(font_name, font))
                    self.config.font_name = font_name
                    print(f"Registered custom font: {font_name} from {font}")
                except Exception as e:
                    print(f"Warning: Could not load font file {font}: {e}")
                    print("Falling back to Helvetica-Bold")
                    self.config.font_name = 'Helvetica-Bold'
            else:
                print(f"Warning: Font file not found: {font}")
                print("Falling back to Helvetica-Bold")
                self.config.font_name = 'Helvetica-Bold'
        else:
            # Assume it's a built-in font name
            self.config.font_name = font
        
    def calculate_cards_per_page(self) -> Tuple[int, int]:
        """
        Calculate how many cards fit on one page
        
        Returns:
            Tuple of (cards_per_row, cards_per_column)
        """
        # Add small margin for spacing
        margin = 5 * mm
        cards_per_row = int((self.page_width - margin) / (self.config.width + margin))
        cards_per_column = int((self.page_height - margin) / (self.config.height + margin))
        return cards_per_row, cards_per_column
    
    def draw_card_front(self, c: canvas.Canvas, x: float, y: float, number: int):
        """
        Draw the front side of a card (with number and border)
        
        Args:
            c: ReportLab canvas object
            x: X coordinate for card bottom-left corner
            y: Y coordinate for card bottom-left corner
            number: Number to display on card
        """
        # Draw card border (cutting guide)
        c.setStrokeColorRGB(0, 0, 0)  # Black
        c.setLineWidth(self.config.border_width)
        c.rect(x, y, self.config.width, self.config.height, stroke=1, fill=0)
        
        # Draw number in the center
        c.setFillColorRGB(0, 0, 0)  # Black
        # Use custom font size if provided, otherwise auto-calculate
        if self.config.font_size is not None:
            font_size = self.config.font_size
        else:
            font_size = min(self.config.width, self.config.height) * 0.4
        c.setFont(self.config.font_name, font_size)
        
        # Center the text
        text = str(number)
        text_width = c.stringWidth(text, self.config.font_name, font_size)
        text_x = x + (self.config.width - text_width) / 2
        
        # Center text vertically by accounting for typical font ascent (~35% of font size)
        # If underline is enabled, adjust slightly higher to center the text+underline combo
        if self.config.underline:
            # With underline: position slightly higher to center the visual group
            text_y = y + (self.config.height / 2) - (font_size * 0.35) + 2
        else:
            # Without underline: use standard centering
            text_y = y + (self.config.height / 2) - (font_size * 0.35)
        
        c.drawString(text_x, text_y, text)
        
        # Draw underline beneath the number (if enabled)
        if self.config.underline:
            underline_y = text_y - 3  # 3 points below text baseline
            c.setLineWidth(1.5)
            c.line(text_x, underline_y, text_x + text_width, underline_y)
    
    def draw_card_back(self, c: canvas.Canvas, x: float, y: float, number: int):
        """
        Draw the back side of a card (with number only, no border)
        
        Args:
            c: ReportLab canvas object
            x: X coordinate for card bottom-left corner
            y: Y coordinate for card bottom-left corner
            number: Number to display on card
        """
        # Draw number in the center (no border)
        c.setFillColorRGB(0, 0, 0)  # Black
        # Use custom font size if provided, otherwise auto-calculate
        if self.config.font_size is not None:
            font_size = self.config.font_size
        else:
            font_size = min(self.config.width, self.config.height) * 0.4
        c.setFont(self.config.font_name, font_size)
        
        # Center the text
        text = str(number)
        text_width = c.stringWidth(text, self.config.font_name, font_size)
        text_x = x + (self.config.width - text_width) / 2
        
        # Center text vertically by accounting for typical font ascent (~35% of font size)
        # If underline is enabled, adjust slightly higher to center the text+underline combo
        if self.config.underline:
            # With underline: position slightly higher to center the visual group
            text_y = y + (self.config.height / 2) - (font_size * 0.35) + 2
        else:
            # Without underline: use standard centering
            text_y = y + (self.config.height / 2) - (font_size * 0.35)
        
        c.drawString(text_x, text_y, text)
        
        # Draw underline beneath the number (if enabled)
        if self.config.underline:
            underline_y = text_y - 3  # 3 points below text baseline
            c.setLineWidth(1.5)
            c.line(text_x, underline_y, text_x + text_width, underline_y)
    
    def generate_pdf(self, numbers: List[int], output_file: str):
        """
        Generate PDF file with cards
        
        Args:
            numbers: List of numbers to include on cards
            output_file: Path to output PDF file
        """
        c = canvas.Canvas(output_file, pagesize=A4)
        cards_per_row, cards_per_column = self.calculate_cards_per_page()
        cards_per_page = cards_per_row * cards_per_column
        
        # Calculate centered margins
        card_spacing = 5 * mm  # spacing between cards
        
        # Calculate total space used by cards and spacing
        total_cards_width = cards_per_row * self.config.width + (cards_per_row - 1) * card_spacing
        total_cards_height = cards_per_column * self.config.height + (cards_per_column - 1) * card_spacing
        
        # Calculate margins to center the cards on the page
        margin_x = (self.page_width - total_cards_width) / 2
        margin_y = (self.page_height - total_cards_height) / 2
        
        # Generate alternating front and back pages
        total_pages = (len(numbers) + cards_per_page - 1) // cards_per_page
        print(f"Generating {total_pages} front and {total_pages} back pages for {len(numbers)} cards...")
        
        for page_num in range(total_pages):
            # Calculate which numbers go on this page
            start_idx = page_num * cards_per_page
            end_idx = min(start_idx + cards_per_page, len(numbers))
            page_numbers = numbers[start_idx:end_idx]
            
            # Generate front page
            for idx, number in enumerate(page_numbers):
                row = idx // cards_per_row
                col = idx % cards_per_row
                
                x = margin_x + col * (self.config.width + card_spacing)
                y = self.page_height - margin_y - (row + 1) * self.config.height - row * card_spacing
                
                self.draw_card_front(c, x, y, number)
            
            c.showPage()
            
            # Generate back page (mirrored horizontally)
            for idx, number in enumerate(page_numbers):
                row = idx // cards_per_row
                # Mirror horizontally for back side
                col = (cards_per_row - 1) - (idx % cards_per_row)
                
                x = margin_x + col * (self.config.width + card_spacing)
                y = self.page_height - margin_y - (row + 1) * self.config.height - row * card_spacing
                
                self.draw_card_back(c, x, y, number)
            
            c.showPage()
        
        c.save()
        print(f"PDF generated successfully: {output_file}")
        print(f"Total pages: {total_pages * 2}")
        print(f"Cards per page: {cards_per_page} ({cards_per_row}x{cards_per_column})")


def parse_number_range(range_str: str) -> List[int]:
    """
    Parse number range string
    
    Args:
        range_str: String like "1-10,15,20-25"
        
    Returns:
        List of numbers
    """
    numbers = []
    for part in range_str.split(','):
        part = part.strip()
        if '-' in part:
            start, end = map(int, part.split('-'))
            numbers.extend(range(start, end + 1))
        else:
            numbers.append(int(part))
    return sorted(set(numbers))  # Remove duplicates and sort


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Generate PDF file with numbered cards for printing',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate cards 1-99
  python card_generator.py -O cards.pdf
  
  # Generate specific numbers
  python card_generator.py -N "1-10,15,20-25" -O cards.pdf
  
  # Generate with custom dimensions (70mm x 100mm)
  python card_generator.py -W 70 -H 100 -O cards.pdf
  
  # Generate only cards 50-60
  python card_generator.py -N "50-60" -O cards_50-60.pdf
  
  # Use custom font from system
  python card_generator.py -F "Times-Bold" -O cards.pdf
  
  # Use custom font from file (.ttf or .otf) with custom size
  python card_generator.py -F "/path/to/font.ttf" -S 48 -O cards.pdf
  python card_generator.py -F "/path/to/font.otf" -S 48 -O cards.pdf
  
  # Add underline to numbers
  python card_generator.py -U -O cards_underlined.pdf
  
  # Combine all options
  python card_generator.py -N "1-20" -W 80 -H 120 -F "Courier-Bold" -S 60 -U -O cards.pdf
        """
    )
    
    parser.add_argument(
        '-N', '--numbers',
        type=str,
        default='1-99',
        help='Numbers to generate (e.g., "1-99", "1-10,15,20-25"). Default: 1-99'
    )
    
    parser.add_argument(
        '-O', '--output',
        type=str,
        default='cards.pdf',
        help='Output PDF file name. Default: cards.pdf'
    )
    
    parser.add_argument(
        '-W', '--width',
        type=float,
        default=63,
        help='Card width in millimeters. Default: 63mm (poker card size)'
    )
    
    parser.add_argument(
        '-H', '--height',
        type=float,
        default=88,
        help='Card height in millimeters. Default: 88mm (poker card size)'
    )
    
    parser.add_argument(
        '-F', '--font',
        type=str,
        default='Helvetica-Bold',
        help='Font name or path to font file (.ttf/.otf). Default: Helvetica-Bold'
    )
    
    parser.add_argument(
        '-S', '--font-size',
        type=float,
        default=None,
        help='Font size in points. If not specified, auto-calculated based on card size'
    )
    
    parser.add_argument(
        '-U', '--underline',
        action='store_true',
        help='Add underline beneath numbers. Default: no underline'
    )
    
    args = parser.parse_args()
    
    # Parse numbers
    try:
        numbers = parse_number_range(args.numbers)
        if not numbers:
            print("Error: No numbers specified")
            return 1
        print(f"Generating cards for numbers: {min(numbers)}-{max(numbers)} ({len(numbers)} cards)")
    except ValueError as e:
        print(f"Error parsing numbers: {e}")
        return 1
    
    # Create configuration
    config = CardConfig(width_mm=args.width, height_mm=args.height, font=args.font, font_size=args.font_size, underline=args.underline)
    print(f"Card dimensions: {args.width}mm x {args.height}mm")
    if args.font != 'Helvetica-Bold':
        print(f"Using font: {args.font}")
    if args.font_size is not None:
        print(f"Using font size: {args.font_size} points")
    if args.underline:
        print("Underline enabled")
    
    # Generate PDF
    generator = CardGenerator(config)
    try:
        generator.generate_pdf(numbers, args.output)
        return 0
    except Exception as e:
        print(f"Error generating PDF: {e}")
        return 1


if __name__ == '__main__':
    exit(main())
