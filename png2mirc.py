#!/usr/bin/env python
#png2mirc by Lilly Chalupowski

from __future__ import print_function
import sys
from PIL import Image

def palette(imgpath, ypix, xpix):
	try:
		ref = []
		im = Image.open(imgpath)
		pix = im.load()
		mirc = 0
		for y in range(0, ypix):
			for x in range(0, xpix):
				ref.append([mirc, pix[x,y]])
				mirc = mirc + 1
		return ref
	except Exception as e:
		print("ERROR: " + str(e))
		return False

def getSize(imgpath):
	try:
		im = Image.open(imgpath)
		pix = im.load()
		return im.size
	except Exception as e:
		print("ERROR: " + str(e))
		return False

def getRGB(imgpath):
	rgb = []
	try:
		im = Image.open(imgpath)
		pix = im.load()
		xsize = im.size[0]
		ysize = im.size[1]
		for y in range(0, ysize):
			for x in range(0, xsize):
				rgb.append(pix[x,y])
		return rgb
	except Exception as e:
		print("ERROR: " + str(e))
		return False

def printIMG(imgpath, palettepath):
	try:
		if palettepath == False:
			rgbpalette = [(255, 255, 255, 255), (0, 0, 0, 255), (0, 0, 192, 255), (0, 192, 0, 255), (255, 63, 63, 255), (192, 0, 0, 255), (192, 0, 192, 255), (192, 192, 0, 255), (255, 255, 63, 255), (63, 255, 63, 255), (0, 192, 192, 255), (63, 255, 255, 255), (63, 63, 255, 255), (255, 63, 255, 255), (63, 63, 63, 255), (192, 192, 192, 255), (95, 0, 0, 255), (135, 95, 0, 255), (135, 135, 0, 255), (95, 95, 0, 255), (0, 95, 0, 255), (0, 135, 95, 255), (0, 95, 95, 255), (0, 95, 135, 255), (0, 0, 95, 255), (95, 0, 135, 255), (95, 0, 95, 255), (135, 0, 95, 255), (135, 0, 0, 255), (175, 95, 0, 255), (175, 175, 0, 255), (95, 135, 0, 255), (0, 135, 0, 255), (0, 175, 95, 255), (0, 135, 135, 255), (0, 95, 175, 255), (0, 0, 135, 255), (135, 0, 175, 255), (135, 0, 135, 255), (175, 0, 95, 255), (175, 0, 0, 255), (215, 95, 0, 255), (215, 215, 0, 255), (135, 175, 0, 255), (0, 175, 0, 255), (0, 255, 175, 255), (0, 175, 175, 255), (0, 135, 255, 255), (0, 0, 175, 255), (175, 0, 255, 255), (175, 0, 175, 255), (215, 0, 95, 255), (255, 0, 0, 255), (255, 135, 0, 255), (255, 255, 0, 255), (175, 255, 0, 255), (0, 255, 0, 255), (95, 255, 215, 255), (0, 255, 255, 255), (95, 175, 255, 255), (0, 0, 255, 255), (215, 95, 255, 255), (255, 0, 255, 255), (255, 0, 135, 255), (255, 95, 95, 255), (255, 175, 95, 255), (255, 255, 95, 255), (215, 255, 95, 255), (95, 255, 95, 255), (135, 255, 215, 255), (95, 255, 255, 255), (135, 175, 255, 255), (95, 95, 255, 255), (215, 135, 255, 255), (255, 95, 255, 255), (255, 95, 175, 255), (255, 175, 175, 255), (255, 215, 175, 255), (255, 255, 175, 255), (215, 255, 175, 255), (175, 255, 175, 255), (175, 255, 215, 255), (175, 255, 255, 255), (175, 215, 255, 255), (175, 175, 255, 255), (215, 175, 255, 255), (255, 175, 255, 255), (255, 135, 215, 255), (0, 0, 0, 255), (18, 18, 18, 255), (38, 38, 38, 255), (58, 58, 58, 255), (78, 78, 78, 255), (98, 98, 98, 255), (128, 128, 128, 255), (158, 158, 158, 255), (188, 188, 188, 255), (228, 228, 228, 255), (255, 255, 255, 255), (216, 216, 1, 1)]
		else:
			rgbpalette = getRGB(palettepath)
		rgbvals = getRGB(imgpath)
		imgsize = getSize(imgpath)
		wreset = 0
		for i in range(0, len(rgbvals)):
			if rgbvals[i] in rgbpalette:
				print('\x030,' + str(rgbpalette.index(rgbvals[i])) + '  \x03', end='')
				wreset = wreset + 1
			else:
				print('\x030,0  \x03', end='')
				wreset = wreset + 1
			if wreset == imgsize[0]:
				wreset = 0
				print("")
	except Exception as e:
		print("ERROR: " + str(e))
		return False

def help_menu():
	print("png2mirc")
	print("     -h | --help    --> This help menu       (opt)")
	print("     -i | --input   --> Input PNG            (req)")
	print("     -o | --output  --> Output to file       (opt)")
	print("     -p | --palette --> Specify Palette File (opt)")
	print("Author: Lilly Chalupowski")

for i in range(0, len(sys.argv)):
	if sys.argv[i] == "-h" or sys.argv[i] == "--help":
		help_menu()
		sys.exit(0)
	if sys.argv[i] == "-i" or sys.argv[i] == "--input":
		input_file = sys.argv[i+1]
	if sys.argv[i] == "-o" or sys.argv[i] == "--output":
		output_file = sys.argv[i+1]
	if sys.argv[i] == "-p" or sys.argv[i] == "--palette":
		palette_file = sys.argv[i+1]

if len(sys.argv) < (1 * 2):
	print("ERROR: Not enough arguments.")
	help_menu()
	sys.exit(1)

if 'output_file' in globals():
	sys.stdout = open(output_file, 'w')

if 'palette_file' not in  globals():
	palette_file = False

printIMG(input_file, palette_file)
