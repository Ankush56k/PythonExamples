# Enter your code here. Read input from STDIN. Print output to STDOUT

n = input()
names = list()
grades = list()
output = list()

for i in range(0,n):
    names.append(raw_input())
    grades.append(input())
    
copy_grades =list(grades)
copy_grades.sort()
temp_n = n

first = copy_grades[0]
while first == copy_grades[0]:
    copy_grades.pop(0)
    temp_n = temp_n-1
first = copy_grades[0]

for i in range(0,n):
    if(first==grades[i]):
        output.append(names[i])
        
output.sort()
len = len(output)

for i in range(0,len):
    print (output[i])
