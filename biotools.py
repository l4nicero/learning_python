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
	
KDscale = {
	'I':4.5,			'V':4.2,		'L':3.8,		'F':2.8,
	'C':2.5,			'M':1.9,			'A':1.8,		'G':-0.4,
	'T':-0.7,			'S':-0.8,		'W':-0.9,		'Y':-1.3,
	'P':-1.6,			'H':-3.2,		'E':-3.5,		'Q':-3.5,
	'D':-3.5,			'N':-3.5,		'K':-3.9,		'R':-4.5
	}
	
ISscale = {
	'I':-0.31,		'V':0.07,		'L':-0.56,		'F':-1.13,
	'C':-0.24,		'M':-0.23,		'A':0.17,		'G':0.01,
	'T':0.14,		'S':0.13,		'W':-1.85,		'Y':-0.94,
	'P':0.45,		'H':0.17,		'E':-0.01,		'Q':0.58,
	'D':-0.07,		'N':0.42,		'K':0.99,		'R':0.81
	}
	
OSscale = {
	'I':-1.12,		'V':-0.46,		'L':-1.25,		'F':-1.71,
	'C':-0.02,		'M':-0.67,		'A':0.50,		'G':1.15,
	'T':0.25,		'S':0.46,		'W':-2.09,		'Y':-0.71,
	'P':0.14,		'H':0.11,		'E':0.11,		'Q':0.77,
	'D':0.43,		'N':0.85,		'K':2.80,		'R':1.81
	}
	
IOSscale = {
	'I':-0.81,		'V':-0.53,		'L':-0.69,		'F':-0.58,
	'C':0.22,		'M':-0.44,		'A':0.33,		'G':1.15,
	'T':0.11,		'S':0.33,		'W':-0.24,		'Y':0.23,
	'P':-0.31,		'H':-0.06,		'E':0.12,		'Q':0.19,
	'D':0.50,		'N':0.43,		'K':1.81,		'R':1.00
	}

def calc_hydro(seq, method, w):
	if method == 'KD':		scale = KDscale
	elif method == 'IS':	scale = ISscale
	elif method == 'OS':	scale = OSscale
	elif method == 'IOS':	scale = IOSscale
	hscore = 0
	for aa in seq:
		if aa in scale: hscore += scale[aa]
	return hscore