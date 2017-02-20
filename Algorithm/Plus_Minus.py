import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
pos = 0
neg = 0
zero = 0

for i in range(0,n):
    if arr[i]>0:
        pos+=1
    if arr[i]<0:
        neg+=1
    if arr[i]==0:
        zero+=1
        
pos1=(float(pos)/float(n))  
neg1=(float(neg)/float(n))
zero1=(float(zero)/float(n))
print("%.6f" %pos1)
print("%.6f" %neg1)
print("%.6f" %zero1)
