#!/usr/bin/python3
# Conrado Pelegrino (D3s0late) - 10/12/2019 - 09:58

import argparse	

parser = argparse.ArgumentParser(description='Capitalize, lowercase or uppercase all words from a target file. (default output is lowercase).')
parser.add_argument('--input', required=True, help='an input wordlist.')
parser.add_argument('--output', required=True, help='an output file to write wordlist.')
parser.add_argument('--uppercase', action="store_true", help='Uppercase target wordlist')
parser.add_argument('--lowercase', action="store_true", help='Lowercase target wordlist')
parser.add_argument('--capitalize', action="store_true", help='Capitalize target wordlist')


args = parser.parse_args()

with open(args.input , "r") as f:
	for line in f:
		line = line.lower()
		if args.uppercase is True:
			line = line.upper()
		elif args.capitalize is True:
			line = line.capitalize()
		out = line.strip()
		with open(args.output, "a") as o:
			o.writelines(out + '\n')
			o.close()
f.close()
