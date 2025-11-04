#!/bin/bash
# Example configuration script for Card Generator
# This file shows various ways to use the card generator

# Generate all cards (1-99) with default settings
python card_generator.py -O cards_complete.pdf

# Generate cards for a specific range
python card_generator.py -N "1-50" -O cards_1-50.pdf

# Generate only specific cards (useful for reprinting)
python card_generator.py -N "25,26,27,28,29,30" -O reprint_25-30.pdf

# Generate cards with multiple ranges
python card_generator.py -N "1-10,20-30,50-60" -O cards_selected.pdf

# Generate cards with custom dimensions (bridge card size: 57mm x 89mm)
python card_generator.py -W 57 -H 89 -O cards_bridge_size.pdf

# Generate large cards (for visibility)
python card_generator.py -W 80 -H 120 -N "1-20" -O cards_large.pdf

# Generate mini cards
python card_generator.py -W 45 -H 65 -N "1-99" -O cards_mini.pdf

# Use custom fonts
python card_generator.py -F "Times-Bold" -O cards_times.pdf
python card_generator.py -F "Courier-Bold" -O cards_courier.pdf

# Use custom font size
python card_generator.py -S 60 -O cards_large_numbers.pdf
python card_generator.py -S 36 -O cards_small_numbers.pdf

# Add underline to numbers
python card_generator.py -U -O cards_underlined.pdf
python card_generator.py -N "1-20" -U -S 72 -O cards_underlined_large.pdf

# Combine options: large cards with large font
python card_generator.py -W 100 -H 150 -F "Courier-Bold" -S 96 -O jumbo_cards.pdf

# Use custom font from file (.ttf or .otf format - replace with actual path)
# python card_generator.py -F "/path/to/custom_font.ttf" -O cards_custom_font.pdf
# python card_generator.py -F "/path/to/custom_font.otf" -O cards_custom_font.pdf

# Adjust vertical position for fonts with incorrect centering (e.g., Cute Notes)
# python card_generator.py -F "Cute Notes.ttf" -V 10 -O cards_cute_notes.pdf
# python card_generator.py -F "SomeFont.otf" -V -5 -O cards_adjusted.pdf

