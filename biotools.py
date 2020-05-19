#!/usr/bin/env python3

import sys
import gzip
import random

def read_fasta(filename):
	name = None
	seqs = []
	
	fp = None
	if filename == '-':
		fp = sys.stdin
	elif filename.endswith('.gz'):
		fp = gzip.open(filename, 'rt')
	else:
		fp = open(filename)

	for line in fp.readlines():
		line = line.rstrip()
		if line.startswith('>'):
			if len(seqs) > 0:
				seq = ''.join(seqs)
				yield(name, seq)
				name = line[1:]
				seqs = []
			else:
				name = line[1:]
		else:
			seqs.append(line)
	yield(name, ''.join(seqs))
	fp.close()

def gc(seq):
	count = 0
	for nt in seq:
		if nt == 'G' or nt == 'C':
			count += 1
	return count / len(seq)

def randseq(l, gc):
	dna = []
	for i in range(l):
		r = random.random()
		if r < gc:
			r = random.random()
			if r < 0.5: dna.append('G')
			else:		dna.append('C')
		else:
			r = random.random()
			if r < 0.5: dna.append('T')
			else:		dna.append('A')
		
def hydro(seq):
	kd = 0
	for aa in seq:
		if   aa == 'I': kd += 4.5
		elif aa == 'V': kd += 4.2
		elif aa == 'L': kd += 3.8
		elif aa == 'F': kd += 2.8
		elif aa == 'C': kd += 2.5
		elif aa == 'M': kd += 1.9
		elif aa == 'A': kd += 1.8
		elif aa == 'G': kd -= 0.4
		elif aa == 'T': kd -= 0.7
		elif aa == 'S': kd -= 0.8
		elif aa == 'W': kd -= 0.9
		elif aa == 'Y': kd -= 1.3
		elif aa == 'P': kd -= 1.6
		elif aa == 'H': kd -= 3.2
		elif aa == 'E': kd -= 3.5
		elif aa == 'Q': kd -= 3.5
		elif aa == 'D': kd -= 3.5
		elif aa == 'N': kd -= 3.5
		elif aa == 'K': kd -= 3.9
		elif aa == 'R': kd -= 4.5
	return kd / len(seq)
	
def gc(seq):
	count = 0
	for nt in seq:
		if nt == 'G' or nt == 'C':
			count =+ 1
	return count / len(seq)
	
def skew(seq):
	#(g-c)/(g+c)
	for nt in seq:
		if nt == 'G':
			g += 1
		if nt == 'C':
			c += 1
	return (g - c)/(g + c)