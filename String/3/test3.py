# Enter your code here. Read input from STDIN. Print output to STDOUT
str = raw_input()
l = list(str)
str1 = raw_input()
str_list = str1.split()
i = int(str_list[0])
l[i] = str_list[1]

str = "".join(l)
print(str)
