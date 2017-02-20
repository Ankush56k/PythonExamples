#!/bin/python

import sys


n = int(raw_input().strip())
a = []
dig = 0
indig = 0
final = 0
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)
    
for i in range(0,n):
    for j in range(0,n):
        if i==j:
            dig+=a[i][j]
        if i+j==n-1:
            indig+=a[i][j]

print(abs(dig-indig))  
