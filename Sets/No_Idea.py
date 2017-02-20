n = raw_input()
sn = n.split()
sn_map = map(int,sn)

l = raw_input()
sl = l.split()
sl_map = map(int,sl)

A = raw_input()
sA = A.split()
sA_map = map(int,sA)

B = raw_input()
sB = B.split()
sB_map = map(int,sB)

A_set = set(sA_map)
B_set = set(sB_map)
AB_Inter = A_set.intersection(B_set)
A_set = A_set.difference(AB_Inter)
B_set = B_set.difference(AB_Inter)
count_A = 0
count_B = 0
for i in sl_map:
    for j in A_set:
            if [i].pop() == {j}.pop() :
                count_A = count_A+1
            
for i in sl_map:            
    for k in B_set:
            if [i].pop() == {k}.pop():
                count_B = count_B+1
    
print(count_A-count_B)

