N = int(input())
list1 =[]
for i in range(0,N):
    x =' '* ((N-1)-i)+'*'*(i*2+1)
    list1.append(x)
    print(x)
for i in range(N-2,-1,-1):
    print(list1[i])
        
              
