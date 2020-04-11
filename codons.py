#!/usr/bin/env python3

# Print out all the codons for the sequence below in reading frame 1
# Use a 'for' loop

dna = 'ATAGCGAATATCTCTCATGAGAGGGAA'
'''
#for 1 frame
for i in range(0, len(dna), 3): #range(start letter, lenth of seq, print 3 @ a time)
    codon = (dna[i:i+3])
    print(codon)

#f1
for i in range(1, len(dna)-2, 3):
    codon = (dna[i:i+3])
    print(codon)
'''
    
#for all frames
for f in range(3): #for number of ranges
    print('frame', f)
    for i in range(f, len(dna) -2, 3): #generic: len(dna) -k +2
        codon = dna[i:i+3] #define codon in case of loop
        print(codon)

"""
frame 0
ATA
GCG
AAT
ATC
TCT
CAT
GAG
AGG
GAA

frame 1
TAG
CGA
ATA
TCT
CTC
ATG
AGA
GGG
"""
