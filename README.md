# Card-Generator
App for generating numeric cards ready to print.

## Description

This Python script generates PDF files containing double-sided numbered cards (1-99) optimized for printing. The cards include:
- **Front side**: Large, centered, underlined numbers with black border for cutting
- **Back side**: Large, centered, underlined numbers (no border)

Perfect for educational materials, games, or any application requiring numbered cards.

## Features

- ✅ Generate cards with numbers from 1 to 99
- ✅ Double-sided design with underlined numbers on both sides
- ✅ Black border on front side for precise cutting
- ✅ Alternating front and back pages for easy duplex printing
- ✅ Customizable card dimensions
- ✅ Flexible number selection (generate only specific numbers)
- ✅ Automatic layout optimization for A4 paper
- ✅ Print-ready PDF output

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Robinxon/Card-Generator.git
cd Card-Generator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

Generate all cards (1-99):
```bash
python card_generator.py -o cards.pdf
```

### Generate Specific Numbers

Generate cards for numbers 1-10:
```bash
python card_generator.py -N "1-10" -O cards_1-10.pdf
```

Generate specific numbers (e.g., 1-10, 15, and 20-25):
```bash
python card_generator.py -N "1-10,15,20-25" -O custom_cards.pdf
```

### Custom Card Dimensions

Generate cards with custom dimensions (e.g., 70mm × 100mm):
```bash
python card_generator.py -W 70 -H 100 -O large_cards.pdf
```

### Custom Font

Use a different font (built-in or custom):
```bash
# Use a built-in font
python card_generator.py -F "Times-Bold" -O cards.pdf

# Use a custom font file (.ttf or .otf)
python card_generator.py -F "/path/to/myfont.ttf" -O cards.pdf
python card_generator.py -F "/path/to/myfont.otf" -O cards.pdf
```

### Custom Font Size

Control the size of numbers on cards:
```bash
# Use custom font size (in points)
python card_generator.py -S 60 -O cards.pdf

# Combine with other options
python card_generator.py -W 80 -H 120 -F "Courier-Bold" -S 72 -O large_cards.pdf
```

### Optional Underline

Add underline beneath numbers (disabled by default):
```bash
# Generate cards with underlined numbers
python card_generator.py -U -O cards_underlined.pdf

# Combine with other options
python card_generator.py -N "1-50" -S 60 -U -O cards.pdf
```

### Vertical Adjustment

For fonts that don't center properly automatically, you can manually adjust the vertical position:
```bash
# Move numbers up by 10 points (positive = up, negative = down)
python card_generator.py -F "Cute Notes.ttf" -V 10 -O cards.pdf

# Move numbers down by 5 points
python card_generator.py -F "SomeFont.otf" -V -5 -O cards.pdf
```

### All Options

```
usage: card_generator.py [-h] [-N NUMBERS] [-O OUTPUT] [-W WIDTH] [-H HEIGHT] [-F FONT] [-S FONT_SIZE] [-U] [-V VERTICAL_OFFSET]

Generate PDF file with numbered cards for printing

optional arguments:
  -h, --help            show this help message and exit
  -N NUMBERS, --numbers NUMBERS
                        Numbers to generate (e.g., "1-99", "1-10,15,20-25"). 
                        Default: 1-99
  -O OUTPUT, --output OUTPUT
                        Output PDF file name. Default: cards.pdf
  -W WIDTH, --width WIDTH
                        Card width in millimeters. Default: 63mm (poker card size)
  -H HEIGHT, --height HEIGHT
                        Card height in millimeters. Default: 88mm (poker card size)
  -F FONT, --font FONT  Font name or path to font file (.ttf/.otf). Default: Helvetica-Bold
  -S FONT_SIZE, --font-size FONT_SIZE
                        Font size in points. If not specified, auto-calculated based on card size
  -U, --underline       Add underline beneath numbers. Default: no underline
  -V VERTICAL_OFFSET, --vertical-offset VERTICAL_OFFSET
                        Manual vertical adjustment in points (positive = move up, negative = move down).
                        Use this if font appears off-center. Default: 0
```

## Examples

### Example 1: Standard poker-sized cards (all numbers)
```bash
python card_generator.py -O cards_1-99.pdf
```

### Example 2: Print only missing cards
If you need to reprint cards 45-50:
```bash
python card_generator.py -N "45-50" -O reprint_45-50.pdf
```

### Example 3: Custom size cards
Create larger cards (80mm × 120mm):
```bash
python card_generator.py -W 80 -H 120 -O large_cards.pdf
```

### Example 4: Multiple ranges
Generate cards: 1-20, 50, and 80-90:
```bash
python card_generator.py -N "1-20,50,80-90" -O selected_cards.pdf
```

### Example 5: Custom font
Use a different font for the numbers:
```bash
# Built-in font
python card_generator.py -F "Times-Roman" -O cards_times.pdf

# Custom font file (.ttf or .otf)
python card_generator.py -F "/path/to/custom_font.ttf" -O cards_custom.pdf
python card_generator.py -F "/path/to/custom_font.otf" -O cards_custom.pdf
```

### Example 6: Custom font size
Control the size of numbers:
```bash
# Larger numbers
python card_generator.py -S 72 -O cards_large_numbers.pdf

# Combine with custom dimensions
python card_generator.py -W 100 -H 150 -F "Courier-Bold" -S 96 -O jumbo_cards.pdf
```

## Printing Instructions

1. **Generate the PDF** using one of the commands above
2. **Print settings**:
   - Use duplex (double-sided) printing
   - Select "Flip on short edge" for proper alignment
   - Use actual size (100% scale, no fitting)
   - Use thick paper (200-300gsm) for better card quality
3. **Cutting**:
   - The black border on the front side serves as a cutting guide
   - Use a paper trimmer or craft knife for clean edges
   - Cut along the outer edge of the black border

## Card Layout

The script automatically calculates the optimal layout for A4 paper based on your card dimensions:
- **Standard cards (63×88mm)**: 3 cards per row, 3 cards per column (9 cards per page)
- The PDF contains alternating front and back pages (page 1: front, page 2: back, page 3: front, etc.)
- Both sides display the number with underline
- Front side has a black border for cutting guidance
- Back pages are horizontally mirrored for proper alignment during duplex printing

## Requirements

- Python 3.6+
- reportlab 4.0.0+

## License

This project is open source and available for personal and commercial use.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

If you encounter any issues or have questions, please open an issue on GitHub.
