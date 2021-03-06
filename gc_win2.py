#!/usr/bin/env python3

# Write a program that computes the GC fraction of a DNA sequence in a window
# Window size is 11 nt
# Output with 4 significant figures using whichever method you prefer
# Use no nested loops
# Describe the pros/cons of this algorith vs. nested loops

seq = 'ACGACGCAGGAGGAGAGTTTCAGAGATCACGAATACATCCATATTACCCAGAGAGAG'
w = 11

for j in range(0, len(seq) -11 +1): #making window = 11 from seq
    win = (seq[j:j+w])
    gc_count = 0
    if win[0] == 'G' or win[0] == 'C': #if character in [position] = G or C, then increase gc count by 1
        gc_count +=1
    if win[1] == 'G' or win[1] == 'C':
        gc_count +=1
    if win[2] == 'G' or win[2] == 'C':
        gc_count +=1
    if win[3] == 'G' or win[3] == 'C':
        gc_count +=1
    if win[4] == 'G' or win[4] == 'C':
        gc_count +=1
    if win[5] == 'G' or win[5] == 'C':
        gc_count +=1
    if win[6] == 'G' or win[6] == 'C':
        gc_count +=1
    if win[7] == 'G' or win[7] == 'C':
        gc_count +=1
    if win[8] == 'G' or win[8] == 'C':
        gc_count +=1
    if win[9] == 'G' or win[9] == 'C':
        gc_count +=1
    if win[10] == 'G' or win[10] == 'C':
        gc_count +=1
    print (j, win,  '%.4f' % (gc_count / w))

"""
0 ACGACGCAGGA 0.6364
1 CGACGCAGGAG 0.7273
2 GACGCAGGAGG 0.7273
3 ACGCAGGAGGA 0.6364
4 CGCAGGAGGAG 0.7273
5 GCAGGAGGAGA 0.6364
6 CAGGAGGAGAG 0.6364
7 AGGAGGAGAGT 0.5455
8 GGAGGAGAGTT 0.5455
9 GAGGAGAGTTT 0.4545
10 AGGAGAGTTTC 0.4545
11 GGAGAGTTTCA 0.4545
12 GAGAGTTTCAG 0.4545
13 AGAGTTTCAGA 0.3636
14 GAGTTTCAGAG 0.4545
15 AGTTTCAGAGA 0.3636
16 GTTTCAGAGAT 0.3636
17 TTTCAGAGATC 0.3636
18 TTCAGAGATCA 0.3636
19 TCAGAGATCAC 0.4545
20 CAGAGATCACG 0.5455
21 AGAGATCACGA 0.4545
22 GAGATCACGAA 0.4545
23 AGATCACGAAT 0.3636
24 GATCACGAATA 0.3636
25 ATCACGAATAC 0.3636
26 TCACGAATACA 0.3636
27 CACGAATACAT 0.3636
28 ACGAATACATC 0.3636
29 CGAATACATCC 0.4545
30 GAATACATCCA 0.3636
31 AATACATCCAT 0.2727
32 ATACATCCATA 0.2727
33 TACATCCATAT 0.2727
34 ACATCCATATT 0.2727
35 CATCCATATTA 0.2727
36 ATCCATATTAC 0.2727
37 TCCATATTACC 0.3636
38 CCATATTACCC 0.4545
39 CATATTACCCA 0.3636
40 ATATTACCCAG 0.3636
41 TATTACCCAGA 0.3636
42 ATTACCCAGAG 0.4545
43 TTACCCAGAGA 0.4545
44 TACCCAGAGAG 0.5455
45 ACCCAGAGAGA 0.5455
46 CCCAGAGAGAG 0.6364
"""
