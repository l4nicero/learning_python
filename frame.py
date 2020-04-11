#!/usr/bin/env python3

# Write a program that prints out the position, frame, and letter of the DNA
# Try coding this with a single loop
# Try coding this with nested loops
 
'''
#draft 1: correct # of loops (b/c 3x3 loops) but wrong # for position
dna = 'ATGGCCTTT'
s ='012'
p = '012345678'
for i in range(len(s)):
    for j in range(len(s)):
            print(p[i], j, dna[i]) #[print letter associated with position #]

#draft 2: print correct position and letter
dna = 'ATGGCCTTT'
s ='012'
p = '012345678'
for i in range(len(dna)):
            print(p[i], dna[i])  

#draft 3: too many loops of length: dna
dna = 'ATGGCCTTT' 
i = 0
s = '012'
for c in dna:
    for j in range(3):
        print(i, j, c)
        i += 1

#draft 4: wrong printed position, too many loops   
dna = 'ATGGCCTTT' 
p = '012345678'
s = '012'
for c in dna:
    for j in range(3): #for every character in dna -> run 3 times each
        print(p, j, c)

'''

#final draft
print('single loop')
dna = '0 0 A 1 1 T 2 2 G 3 0 G 4 1 C 5 2 C 6 0 T 7 1 T 8 2 T ' #spaces count as characters
for i in range(0, len(dna), 6): #read 6 characters/loop
    frm = (dna[i:i+5]) #print out every 5 characters that are read/loop
    print(frm)

print('   ')
    
print('nested loop')
dna = 'ATGGCCTTT'
s = '012'
i = 0
for j in range(len(s)):
    for k in range(len(s)): #line 54 + 55 = 3x3 loops
        print(i, k, dna[i])
        i +=1

"""
0 0 A
1 1 T
2 2 G
3 0 G
4 1 C
5 2 C
6 0 T
7 1 T
8 2 T
"""
