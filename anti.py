#!/usr/bin/env python3

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

#for complement
dna = 'ACTGAAAAAAAAAAA'
comp = ''
for nt in dna:
    if   nt == 'A': comp += 'T'
    elif nt == 'G': comp += 'C'
    elif nt == 'C': comp += 'G'
    else:           comp += 'A'
print(dna)
print(comp)

#for anti+complement
dna = 'ACTGAAAAAAAAAAA'
comp = ''

for nt in dna:
    if   nt == 'A': comp = 'T' +comp
    elif nt == 'G': comp = 'C' +comp
    elif nt == 'C': comp = 'G' +comp
    else:           comp = 'A' +comp
print(dna)
print(comp)

"""
TTTTTTTTTTTCAGT
"""
