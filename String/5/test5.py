# Enter your code here. Read input from STDIN. Print output to STDOUT
str = raw_input()
l = len(str)
a = str[0].isalnum()
b = str[0].isalpha()
c = str[0].isdigit()
d = str[0].islower()
e = str[0].isupper()

for i in range(1,l):
    a = a or str[i].isalnum()
    b = b or str[i].isalpha()
    c = c or str[i].isdigit()
    d = d or str[i].islower()
    e = e or str[i].isupper()
print(a)
print(b)
print(c)
print(d)
print(e)