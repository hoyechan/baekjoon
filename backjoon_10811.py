N,M = map(int, input().split())
aa = [i+1 for i in range(0,N)]

for _ in range(0,M):
    i,j=map(int, input().split())
    list1 = aa[i-1:j]
    list1.reverse()
    aa[i-1:j]=list1[:]
print(*aa)
    
