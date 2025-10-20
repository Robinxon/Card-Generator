# Card-Generator
App for generating numeric cards ready to print.

## Description

This Python script generates PDF files containing double-sided numbered cards (1-99) optimized for printing. The cards include:
- **Front side**: Large, centered numbers for easy reading
- **Back side**: Black borders as cutting guides

Perfect for educational materials, games, or any application requiring numbered cards.

## Features

- ✅ Generate cards with numbers from 1 to 99
- ✅ Double-sided design (number on front, cutting guide on back)
- ✅ Black border on back side for precise cutting
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
python card_generator.py -n "1-10" -o cards_1-10.pdf
```

Generate specific numbers (e.g., 1-10, 15, and 20-25):
```bash
python card_generator.py -n "1-10,15,20-25" -o custom_cards.pdf
```

### Custom Card Dimensions

Generate cards with custom dimensions (e.g., 70mm × 100mm):
```bash
python card_generator.py -w 70 --height 100 -o large_cards.pdf
```

### All Options

```
usage: card_generator.py [-h] [-n NUMBERS] [-o OUTPUT] [-w WIDTH] [-h HEIGHT]

Generate PDF file with numbered cards for printing

optional arguments:
  -h, --help            show this help message and exit
  -n NUMBERS, --numbers NUMBERS
                        Numbers to generate (e.g., "1-99", "1-10,15,20-25"). 
                        Default: 1-99
  -o OUTPUT, --output OUTPUT
                        Output PDF file name. Default: cards.pdf
  -w WIDTH, --width WIDTH
                        Card width in millimeters. Default: 63mm (poker card size)
  --height HEIGHT       Card height in millimeters. Default: 88mm (poker card size)
```

## Examples

### Example 1: Standard poker-sized cards (all numbers)
```bash
python card_generator.py -o cards_1-99.pdf
```

### Example 2: Print only missing cards
If you need to reprint cards 45-50:
```bash
python card_generator.py -n "45-50" -o reprint_45-50.pdf
```

### Example 3: Custom size cards
Create larger cards (80mm × 120mm):
```bash
python card_generator.py -w 80 --height 120 -o large_cards.pdf
```

### Example 4: Multiple ranges
Generate cards: 1-20, 50, and 80-90:
```bash
python card_generator.py -n "1-20,50,80-90" -o selected_cards.pdf
```

## Printing Instructions

1. **Generate the PDF** using one of the commands above
2. **Print settings**:
   - Use duplex (double-sided) printing
   - Select "Flip on short edge" for proper alignment
   - Use actual size (100% scale, no fitting)
   - Use thick paper (200-300gsm) for better card quality
3. **Cutting**:
   - The black border on the back side serves as a cutting guide
   - Use a paper trimmer or craft knife for clean edges
   - Cut along the outer edge of the black border

## Card Layout

The script automatically calculates the optimal layout for A4 paper based on your card dimensions:
- **Standard cards (63×88mm)**: 3 cards per row, 3 cards per column (9 cards per page)
- The PDF contains front pages first, then back pages
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
