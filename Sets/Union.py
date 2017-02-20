n1 = input()
e = raw_input()
el = e.split()
es = set(el)

n2 = input()
f = raw_input()
fl = f.split()
fs = set(fl)

E = es.difference(fs)
F = fs.difference(es)
I = es.intersection(fs)
result = E.union(F)

print(len(result)+len(I))
