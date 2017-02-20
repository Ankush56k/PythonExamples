n = input()
e = raw_input()
el = e.split()
es = set(el)

q = input()
for i in range(0,q):
    s = raw_input()
    spl = s.split()
    s1 = raw_input()
    spl_array = s1.split()
    set1 = set(spl_array)
    
    if spl[0] == "intersection_update":
        es.intersection_update(set1)
    if spl[0] == "update":
        es.update(set1)
    if spl[0] == "symmetric_difference_update":
        es.symmetric_difference_update(set1)
    if spl[0] == "difference_update":
        es.difference_update(set1)    

result = map(int,es)    
sum = 0
for i in result:
    sum = sum + {i}.pop()
print(sum)
