N,M=map(int,input().split())
list1 =[]
for i in range(0,N):
    list1.append(i+1)
for _ in range(0,M):
    i,j = map(int,input().split())
    ii = list1[i-1]
    jj = list1[j-1]
    list1[i-1] = jj
    list1[j-1] = ii
for i in range(0,N):
    print(list1[i],end=' ')
