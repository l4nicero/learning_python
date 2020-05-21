#!/usr/bin/env python3

import argparse
import biotools as bt

# setup
parser = argparse.ArgumentParser(
	description='Predicts transmembrane proteins.')
# required arguments
parser.add_argument('--file', required=True, type=str,
	metavar='<path>', help='protein file')
# optional arguments with default parameters
parser.add_argument('--win1', required=False, type=int, default=8,
	metavar='<int>', help='length for signal peptide [%(default)i]')
parser.add_argument('--win2', required=False, type=int, default=11,
	metavar='<int>', help='length of transmembrane domain [%(default)i]')
parser.add_argument('--kd1', required=False, type=float, default=2.5,
	metavar='<float>', help='kd value for signal peptide [%(default)f]')
parser.add_argument('--kd2', required=False, type=float, default=2.0,
	metavar='<float>', help='kd value for hydrophobic region [%(default)f]')
# finalization
arg = parser.parse_args()

def hh(seq, w, kd):
	for i in range(len(seq) -w +1):
		win = seq[i:i+w]
		if hydro(win) > kd and 'P' not in win:
			return True
	return False
 
for name, seq in bt.read_fasta(arg.file):
	nterm = seq[0:30]
	rest = seq[30:len(seq)]
	if hh(nterm, arg.kd1, arg.win1) and hh(rest, arg.kd2, arg.win2):
		print(name)
