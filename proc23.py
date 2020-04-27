#!/usr/bin/env python3

import fileinput

# Write a program that reads a 23andme file
# Report the number of SNPs successfully assayed
# Report the heterozygosity
# Report the failure rate
# https://opensnp.org/genotypes (make sure the data is 23andme)

for line in fileinput.input():
    if line.startswith('#'): continue # skip over comments
    cols = line.split() #break up columns
    gtype = cols[3]
    nt1 = gtype[0:1]
    nt2 = gtype[1:2]
    snps += 1
    if nt1 == '-':   errs +=1
    elif nt1 == nt2: hom +=1
    else:            het += 1
    
print(snps, errs, hom, het, het/(hom+het))
    
"""
proc23.py ~/Downloads/9572.23andme.7848
"""
