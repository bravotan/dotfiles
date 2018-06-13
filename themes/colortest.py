#!/usr/bin/env python
from __future__ import print_function
# Ported to Python from http://www.vim.org/scripts/script.php?script_id=1349

print("Color indexes should be drawn in bold text of the same color.\n")

colored = [0] + [0x5f + 40 * n for n in range(0, 5)]
colored_palette = [
	"{:02x}{:02x}{:02x}".format(r, g, b)
	for r in colored
	for g in colored
	for b in colored
]

grayscale = [0x08 + 10 * n for n in range(0, 24)]
grayscale_palette = [
	"{:02x}{:02x}{:02x}".format(a, a, a)
	for a in grayscale
]

normal = "\033[38;5;{}m{}\033[0m"
bold = "\033[1;38;5;{}m{}\033[0m"

for (i, rgb) in enumerate(colored_palette + grayscale_palette, 16):
    index = bold.format(i, '{:>3}:'.format(i))
    hexa = normal.format(i, rgb)
    square = bold.format(i, '\u2588')
    print(index, hexa, square, end=('\n' if i % 6 == 3 else '  '))
