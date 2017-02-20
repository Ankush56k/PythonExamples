# Enter your code here. Read input from STDIN. Print output to STDOUT
str = raw_input()
substring = raw_input()
l = len(str)
sl = len(substring)
count = 0
count1 = 0

for i in range(0,l-sl+1):
    for j in range(0,sl):
        if (str[i+j]==substring[j]):
            count = count+1
    if count == sl:
        count1 = count1+1
    count = 0    
print(count1)
