#!/usr/bin/env python3

import fileinput
import json
import random

puncs =  '.,1?!:;-*"_()[]{}<>/1234567890—“”’‘–' # you may need to add more
spaces = ' ' * len(puncs)

first = {}
scnd = {}
for rawline in fileinput.input():

	# convert to lowercase
	lower = rawline.lower()
	
	# convert punctuation to spaces
	table = lower.maketrans(puncs, spaces)
	line = lower.translate(table)
	
	# start work here
	for word in line.split():
		modword = word + '*'
		
		#place first letter of each word into dict
		letter = modword[0]
		if letter in first: first[letter] += 1
		else:				first[letter] = 1
		
		#place second letter into a dict
		for i in range(1, len(modword)):
			c1 = modword[i-1]
			c2 = modword[i]
			if c1 not in scnd: scnd[c1] = {}
			if c2 not in scnd[c1]: scnd[c1][c2] = 1
			else:                scnd[c1][c2] += 1
			
#print(json.dumps(scnd, indent=4))
	
#start word creation
# make list for first letter options
pool = []
for letter in first:
	for i in range(first[letter]):
		if first[letter] > 1: pool.append(letter)
#print(pool)
	
pool2= {}
for c1 in scnd:
	stuff = []
	for c2 in scnd[c1]:
		for i in range(scnd[c1][c2]):
			stuff.append(c2)
	pool2[c1] = stuff

#choose first letter
word = []
for i in range(30):
	word = []
	word.append(random.choice(pool))
	for j in range(1,15):
		prv = word[j-1]
		nxt = random.choice(pool2[prv])
		if nxt == '*': break
		word.append(nxt)
	if len(word) > 1:
		print(''.join(word))