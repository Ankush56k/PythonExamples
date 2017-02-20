n = input()
p = raw_input()

l = p.split()
li = map(int,l)
s = set(li)
sum = 0.0

for i in s:
    sum = sum + {i}.pop()
    
avg = sum/len(s)
print(avg)

