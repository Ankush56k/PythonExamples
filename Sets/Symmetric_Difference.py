n1 = input()
s1 = raw_input()
s1l = s1.split()
s1l_map = map(int,s1l)

n2 = input()
s2 = raw_input()
s2l = s2.split()
s2l_map = map(int,s2l)

first_set = set(s1l_map)

second_set = set(s2l_map)
dif1 = first_set.difference(second_set)

dif2 = second_set.difference(first_set)

result = sorted(dif1.union(dif2))
for i in result:
    print({i}.pop())
