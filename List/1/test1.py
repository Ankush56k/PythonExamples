# Enter your code here. Read input from STDIN. Print output to STDOUT
a = input()
b = input()
c = input()
d = input()
l = list()
for a in range(0,a+1):
    for b in range(0,b+1):
        for c in range(0,c+1):
            if(a+b+c!=d):
                l1 = list()
                l1.append(a)
                l1.append(b)
                l1.append(c)
                l.append(l1)
                
print (l)               
