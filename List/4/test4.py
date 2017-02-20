# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()

final_dict = {}

for i in range(0,n):
    str = raw_input()
    temp_str = str.split()
    name = temp_str[0]
    maths = float(temp_str[1])
    physics = float(temp_str[2])
    chemistry = float(temp_str[3])
    percent = float((maths+physics+chemistry)/3)
    final_dict.update({name : '%.2f' % percent})
    
val = raw_input()    
    
print (final_dict.get(val))    
