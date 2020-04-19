#!/usr/bin/env python3

import random
#random.seed(1) # comment-out this line to change sequence each time

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

#for prompt
length = 30
dna = ' '
at_count = 0
for i in range(length):
    r = random.random( ) #generate a random # from [0, 1)
    if r < 0.6:
        r = random.randint(0, 1)
        if r == 0: dna += 'A'
        else:      dna+= 'T'
        at_count += 1
    else:
        r = random.randint(0, 1)
        if r == 0: dna += 'C'
        else:      dna += 'G'
print(length, at_count / length, dna)

#extra stuff
length = 30
dna = ' '
at_count = 0
alphabet = 'ACGT'
for i in range(length):
    nt = random.choice(alphabet) #generate a random character
    if nt == 'A' or nt == 'T': at_count += 1
    dna += nt
print(length, at_count / length, dna)

"""
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
