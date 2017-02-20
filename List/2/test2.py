# Enter your code here. Read input from STDIN. Print output to STDOUT

n = input()
str = raw_input()
sl = str.split()
l = map(int,sl)
l.sort()
last = l[n-1]
while(last == l[n-1]):
    l.pop()
    n=n-1
last = l[n-1]    
print(last)
