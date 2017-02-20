n = input()
s = set(map(int, raw_input().split())) 

com = input()
for i in range(0,com):
    a = raw_input()
    l = a.split()
    if l[0] == "pop":
        s.pop()
    if l[0] == "remove":
        s.remove(int(l[1]))
    if l[0] == "discard":
        s.discard(int(l[1]))
sum=0        
for i in s:
    sum = sum + {i}.pop()
    
print(sum)
