#!/bin/bash
# Example configuration script for Card Generator
# This file shows various ways to use the card generator

# Generate all cards (1-99) with default settings
python card_generator.py -o cards_complete.pdf

# Generate cards for a specific range
python card_generator.py -n "1-50" -o cards_1-50.pdf

# Generate only specific cards (useful for reprinting)
python card_generator.py -n "25,26,27,28,29,30" -o reprint_25-30.pdf

# Generate cards with multiple ranges
python card_generator.py -n "1-10,20-30,50-60" -o cards_selected.pdf

# Generate cards with custom dimensions (bridge card size: 57mm x 89mm)
python card_generator.py -w 57 -H 89 -o cards_bridge_size.pdf

# Generate large cards (for visibility)
python card_generator.py -w 80 -H 120 -n "1-20" -o cards_large.pdf

# Generate mini cards
python card_generator.py -w 45 -H 65 -n "1-99" -o cards_mini.pdf

# Use custom fonts
python card_generator.py -f "Times-Bold" -o cards_times.pdf
python card_generator.py -f "Courier-Bold" -o cards_courier.pdf

# Use custom font from file (replace with actual path)
# python card_generator.py -f "/path/to/custom_font.ttf" -o cards_custom_font.pdf

