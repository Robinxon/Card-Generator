# Implementation Notes for Card Generator

## Overview
This implementation provides a complete solution for generating printable PDF cards with numbers from 1 to 99, as specified in the requirements.

## Requirements Met

### ✅ Core Requirements
1. **Python Script for PDF Generation**: Implemented in `card_generator.py` using reportlab library
2. **Double-sided Cards**: 
   - Front side: Large, centered, underlined number with black border for cutting guidance
   - Back side: Large, centered, underlined number (no border)
3. **Number Range (1-99)**: Full support for generating any number from 1 to 99
4. **Flexible Number Selection**: Users can specify exact numbers or ranges (e.g., "1-10,15,20-25")
5. **Customizable Dimensions**: Card width and height can be adjusted via command-line parameters

### ✅ Additional Features Implemented
- Automatic layout optimization for A4 paper
- Alternating front and back pages for easy duplex printing
- Mirrored back pages for proper duplex printing alignment
- Underlined numbers on both sides
- Comprehensive documentation in English and Polish
- Example configuration script
- Test suite for quality assurance
- Command-line interface with helpful examples

## Technical Details

### Card Layout
- **Default card size**: 63mm × 88mm (standard poker card)
- **Default layout on A4**: 3 cards × 3 cards (9 cards per page)
- **Margin**: 5mm between cards and page edges
- **Border thickness**: 2mm for cutting guide

### Double-sided Printing
The script generates alternating front and back pages:
1. **Front pages**: Cards with underlined numbers and black borders in reading order
2. **Back pages**: Cards with underlined numbers (no border), horizontally mirrored for duplex printing

Page order: Front page 1, Back page 1, Front page 2, Back page 2, etc.

When printed using duplex printing with "flip on short edge", the backs align perfectly with the fronts.

### Dependencies
- **Python**: 3.6+
- **reportlab**: 4.0.0+ (PDF generation library)

## File Structure

```
Card-Generator/
├── card_generator.py      # Main script
├── requirements.txt       # Python dependencies
├── example_config.sh      # Example usage scenarios
├── test_generator.py      # Test suite
├── README.md             # Documentation (English)
├── README_PL.md          # Documentation (Polish)
└── .gitignore           # Git ignore rules (includes *.pdf)
```

## Usage Examples

### Basic Usage
```bash
# Generate all cards (1-99)
python card_generator.py -o cards.pdf

# Generate specific range
python card_generator.py -n "50-60" -o reprint_50-60.pdf

# Custom dimensions
python card_generator.py -w 70 --height 100 -o large_cards.pdf

# Complex number selection
python card_generator.py -n "1-10,15,20-25,50,75-80" -o selected.pdf
```

## Testing

The implementation includes a comprehensive test suite (`test_generator.py`) that verifies:
- Default usage (1-99)
- Small ranges (1-5)
- Specific number selection
- Complex range parsing
- Custom dimensions

All tests pass successfully with no security vulnerabilities (verified with CodeQL).

## Security

- No shell injection vulnerabilities
- No hardcoded credentials
- Safe file operations
- Input validation for number ranges
- CodeQL analysis: 0 alerts

## Print Instructions

For best results:
1. Use duplex (double-sided) printing
2. Select "Flip on short edge"
3. Print at 100% scale (no fitting)
4. Use 200-300gsm cardstock
5. Cut along the black border on the back side

## Future Enhancements (Optional)

Possible improvements for future versions:
- GUI interface for easier use
- Support for custom text instead of numbers
- Color options for borders and numbers
- Different paper sizes (Letter, Legal, etc.)
- Batch processing from CSV files
- Preview generation before printing

## Compliance with Requirements

This implementation fully satisfies all requirements from the problem statement:
- ✅ Python script for PDF generation
- ✅ Double-sided cards with numbers 1-99
- ✅ Black border on one side for cutting
- ✅ Full control over which numbers to generate
- ✅ Configurable card dimensions

The solution is production-ready and can be used immediately for generating printable cards.
