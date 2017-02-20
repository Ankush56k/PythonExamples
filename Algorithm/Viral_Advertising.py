# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
n = input()
first = math.floor(5/2)
sum1 = 2
for i in range(1,n):
    day = first * 3
    res = int(math.floor(day/2))
    sum1=sum1+res 
    first = res
print(sum1)

