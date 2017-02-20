def array_left_rotation(a, n, k):
   
    for i in range(0,k):
        first = a[0]
        temp = a[n-1]
        for j in range(n-1,-1,-1):
            temp1 = a[j-1]
            a[j-1] = temp
            temp = temp1
        a[n-1] = first    
    return a            
            
        
  

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))
