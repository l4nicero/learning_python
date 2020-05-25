#!/usr/bin/env python3

# Modify entropy_fast() however you like to make it faster
# Ideally, your method is faster at all ranges of window size

import math
import time
import random

def entropy_slow(seq, w, th):
	t0 = time.perf_counter()
	low_H_count = 0
	
	for i in range(len(seq) - w + 1):
		win = seq[i:i+w]
		a, c, g, t = 0, 0, 0, 0
		for nt in win:
			if   nt == 'A': a += 1
			elif nt == 'C': c += 1
			elif nt == 'G': g += 1
			elif nt == 'T': t += 1
		total = a + c + g + t
		h = 0
		pa, pc, pg, pt = a/total, c/total, g/total, t/total
	
		if a != 0: h -= pa * math.log2(pa)
		if c != 0: h -= pc * math.log2(pc)
		if g != 0: h -= pg * math.log2(pg)
		if t != 0: h -= pt * math.log2(pt)
	
		if h < th: low_H_count += 1
	
	t1 = time.perf_counter()
	return low_H_count, t1-t0

def entropy_fast(seq, w, th):
	t0 = time.perf_counter()
	low_H_count = 0
	
	for i in range(len(seq) - w + 1):
		#create window
		win = seq[i:i+w]
		
		#calc h for that window
		#step 1: get counts
		nt_ct = {}
		for nt in win:
			if nt in nt_ct:		nt_ct[nt] += 1
			else:				nt_ct[nt] = 1
		#step 2: convert for probs
		total = len(win) 
		prob = []
		for i in nt_ct.values():
			p = i / total
			prob.append(p)
		#step 3: calc h
		h = 0
		for j in range(len(prob)):
			if prob[j] != 0: h -= prob[j] * math.log2(prob[j])
	
		#ask is h below t
		if h < th: low_H_count += 1

	t1 = time.perf_counter()
	return low_H_count, t1-t0

# create a random chromosome
seq = []
alph = ['A', 'C', 'G', 'T']
for i in range(int(1e5)):
	seq.append(alph[random.randint(0,3)])
seq = ''.join(seq)

# test speed at various word sizes
W = [7, 15, 100]
for w in W:
	cs, ts = entropy_slow(seq, w, 1)
	cf, tf = entropy_fast(seq, w, 1)
	assert(cs == cf) #ensures both answers are the same
	print(tf / ts)
