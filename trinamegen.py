#!/usr/bin/env python3

import fileinput
import json
import random

puncs =  '.,1?!:;-*"_()[]{}<>/1234567890—“”’‘–' # you may need to add more
spaces = ' ' * len(puncs)

frst = {}
scnd = {}
thrd = {}
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
		if letter in frst:	frst[letter] += 1
		else:				frst[letter] = 1
		
		#place second letter into a dict
		for i in range(1, len(modword)):
			c1 = modword[i-1]
			c2 = modword[i]
			if c1 not in scnd:		scnd[c1] = {}
			if c2 not in scnd[c1]:	scnd[c1][c2] = 1
			else:					scnd[c1][c2] += 1
			
		#place third letter into a dict 
		for i in range(1, len(modword)):
			c1 = modword[i-2]
			c2 = modword[i-1]
			c3 = modword[i]
			if c1 not in thrd:			thrd[c1] = {}
			if c2 not in thrd[c1]:		thrd[c1][c2] = {}
			if c3 not in thrd[c1][c2]:	thrd[c1][c2][c3] = 1
			else:						thrd[c1][c2][c3] += 1
		
#print(json.dumps(thrd, indent=4))
	
#start word creation
#make pool for 1st letter options
pool1 = []
for letter in frst:
	for i in range(frst[letter]):
		if frst[letter] > 1: pool1.append(letter)
#print(pool)
	
#make pool for 2nd letter options
pool2= {}
for c1 in scnd:
	stuff = []
	for c2 in scnd[c1]:
		for i in range(scnd[c1][c2]):
			stuff.append(c2)
	pool2[c1] = stuff
#print(pool2)

#make pool for 3rd letter options
pool3 = {}
for c1 in thrd:
	pool3[c1] = {}
	for c2 in thrd[c1]:
		stuff = []
		for c3 in thrd[c1][c2]:
			for i in range(thrd[c1][c2][c3]):
				stuff.append(c3)
		pool3[c1][c2] = stuff
		
#choose first letter
word = []
while True:
	word = []
	word.append(random.choice(pool1)) #choose 1st letter
	word.append(random.choice(pool2[word[0]])) #choose 2nd letter
	if word[1] == '*': continue
	j = 2
	while True:
		p2 = word[j-2]
		p1 = word[j-1]
		nxt = random.choice(pool3[p2][p1])
		j += 1
		if nxt == '*': break
		word.append(nxt)
	if len(word) > 2:
		name = ''.join(word)
		print(name.capitalize())