#!/bin/python

import sys


n,k,q = raw_input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = map(int,raw_input().strip().split(' '))

temp1 = 0
for i in range(0,k):
    last = a[n-1]
    temp = a[0]
    for j in range(0,(len(a)-1)): 
        temp1 = a[j+1]
        a[j+1] = temp
        temp = temp1
    a[0] = last                      

for a0 in xrange(q):
    m = int(raw_input().strip())
    print(a[m])
    
