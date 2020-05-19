#!/usr/bin/env python3

import gzip
import sys
import biotools as bt
import argparse

# Use argparse
# Write a program that translates an mRNA
# Assume the protein encoded is the longest ORF

parser = argparse.ArgumentParser(
	description='Brief description of program.')
parser.add_argument('--file', required=True, type=str,
	metavar='<path>', help='fasta file')
	
def longest_orf(seq):
	#find all atg
	atgs = []
	for i in range(len(seq) -2):
		if seq[i:i+3] == 'ATG': atgs.append(i)
		
	#for each atg find nearest frame stop
	#check if longest
	max_len = 0
	max_seq = None
	for atg in atgs:
		stop = None
		for i in range(atg, len(seq) -2, 3):
			codon = seq[i:i+3]
			if codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
				stop = i
				break
		if stop != None: #if there is a stop  # != means not equal to
			cds_len = stop - atg +3
			if cds_len > max_len:
				max_len = cds_len
				max_seq = seq[atg:atg+max_len]
			
	#translate longest ORF into protein
	protein = translate(max_seq)
	return protein
	if max_seq == None:
		return None
	
def translate(seq):
	assert(len(seq)) % 3 == 0
	prt = []
	for i in range(0, len(seq), 3):
		codon = seq[i:i+3]
		if codon[0] == 'A':
			if codon[1] == 'A':
				if codon[2] == 'A' or codon[2] == 'G': 	prt.append('K')
				elif codon[2] == 'C' or codon[2] == 'T':	prt.append('N')
			elif codon[1] == 'C':						prt.append('T')
			elif codon[1] == 'G':
				if codon[2] == 'A' or codon[2] == 'G':	prt.append('R')
				elif codon[2] == 'C' or codon[2] == 'T':	prt.append('S')
			elif codon[1] == 'T':
				if codon[2] == 'G':						prt.append('M')
				elif codon[2] == 'A' or codon[2] == 'C' or codon[2] == 'T':	prt.append('I')
		elif codon[0] == 'C':
			if codon[1] == 'A':
				if codon[2] == 'A' or codon[2] == 'G': prt.append('Q')
				elif codon[2] == 'C' or codon[2] == 'T': prt.append('H')
			elif codon[1] == 'C': prt.append('P')
			elif codon[1] == 'G': prt.append('R')
			elif codon[1] == 'T': prt.append('L')
		elif codon[0] == 'G':
			if codon[1] == 'A':
				if codon[2] == 'A' or codon[2] == 'G': prt.append('E')
				elif codon[2] == 'C' or codon[2] == 'T': prt.append('D')
			elif codon[1] == 'C': prt.append('A')
			elif codon[1] == 'G': prt.append('G')
			elif codon[1] == 'T': prt.append('V')
		elif codon[0] == 'T':
			if codon[1] == 'A':
				if codon[2] == 'A' or codon[2] == 'G': prt.append('*')
				elif codon[2] == 'C' or codon[2] == 'T': prt.append('Y')
			elif codon[1] == 'C': prt.append('S')
			elif codon[1] == 'G':
				if codon[2] == 'A': prt.append('*')
				elif codon[2] == 'C' or codon[2] == 'T': prt.append('C')
				elif codon[2] == 'G': prt.append('W')
			elif codon[1] == 'T':
				if codon[2] == 'A' or codon[2] == 'G': prt.append('L')
				elif codon[2] == 'C' or codon[2] == 'T': prt.append('F')		
	return ''.join(prt)	

arg = parser.parse_args()	
for name, seq in bt.read_fasta(arg.file):
	print(f'>{name}')
	print(longest_orf(seq))
	break
	
"""
python3 translate_mRNA.py --file ../Lesson05/transcripts.fasta.gz
>CBG00001.1
MTFCENKNLPKPPSDRCQVVVISILSMILDFYLKYNPDKHWAHLFYGASPILEILVIFGMLANSVYGNKLAMFACVLDLVSGVFCLLTLPVISVAENATGVRLHLPYISTFHSQFSFQVSTPVDLFYVATFLGFVSTILILLFLILDALKFMKLRKLRNEDLEKEKKMNPIEKV*
>CBG00006.1
MNGVEKVNKYFDIKDKRDFLYHFGFGVDTLDIKAVFGDTKFVCTGGSPGRFKLYAEWFAKETSIPCSENLSRSDRFVIYKTGPVCWINHGMGTPSLSIMLVESFKLMHHAGVKNPTFIRLGTSGGVGVPPGTVVVSTGAMNAELGDTYVQVIAGKRIERPTQLDATLREALCAVGKEKNIPVETGKTMCADDFYEGQMRLDGYFCDYEEEDKYAFLRKLNSLGVRNIEMESTCFASFTCRAGFPSAIVCVTLLNRMDGDQVQIDKEKYIEYEERPFRLVTAYIRQQTGV*
etc.
"""
