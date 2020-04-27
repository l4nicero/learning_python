#!/usr/bin/env python3

from math import sqrt
import fileinput

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import any other modules!

num = []

for line in fileinput.input():
    if line.startswith('#'): continue
    line = line.rstrip() #remove newline (return character)
    num.append(float(line)) #store data

num.sort()

#for: Counts, Min, Max, Mean
i = 0
sum1 = 0
for i in range(len(num)):
	sum1 += num[i]
i += 1
avg = sum1 / len(num)

#for Std. dev
stdv = 0
for j in range(len(num)):
    stdv += (num[j] - avg) * (num[j] - avg) #for every loop add this
stdv = sqrt(stdv / int(i))

#for Median
if i % 2 == 0: #if there is even numb of data
    medn1 = num[int(i / 2) -1]
    medn2 = num[int(i / 2)]
    medn  = (medn1 + medn2) / 2
else:
    medn  = num[int(i / 2) -1]

print(f'Counts: {i}')
print(f'Minimum: {num[0]}')
print(f'Maximum: {num[-1]}')
print(f'Mean: {avg}')
print('Std. dev: ''%.3f' % (stdv))
print(f'Median: {medn}')


"""
python3 stats.py numbers.txt
Count: 10
Minimum: -1.0
Maximum: 256.0
Mean: 29.147789999999997
Std. dev: 75.777
Median 2.35914
"""
