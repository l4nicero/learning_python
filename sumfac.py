#!/usr/bin/env python3

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# No, you may not use math.factorial()
# Use the same loop for both calculations

n = 5
rsum = 0
fac = 1
for i in range(1, n+1): #start with 1 so factorial does not equal 0
    rsum +=i
    fac *=i

print(i, rsum, fac)

"""
5 15 120

GOAL: print(n, rsum, fac)
"""
