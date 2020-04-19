#!/usr/bin/env python3

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places
# Use all three formatting methods

#method 1: printf()
dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT' # feel free to change
GC_count = 0
print('method 1: printf()')
for i in range(0, len(dna)):
    if dna[i] == 'G' or dna[i] == 'C':
        GC_count +=1
print('%.2f' % (GC_count / len(dna))) #'what you want printed' % 'math you want performed'

print( )

#method 2:
dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT'
GC_count = 0
print('method 2: str.format')
for i in range(0, len(dna)):
    if dna[i] == 'G' or dna[i] == 'C':
        GC_count += 1
print('{:.2f}'.format(GC_count / len(dna)))

print( )

#method 3: f-strings
dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT'
GC_count = 0
print('method 3: f-strings')
for i in range(0, len(dna)):
    if dna[i] == 'G' or dna[i] == 'C':
        GC_count += 1
print(f'{GC_count / len(dna) :.2f}') #can perform math inside { }

"""
0.42
0.42
0.42
"""