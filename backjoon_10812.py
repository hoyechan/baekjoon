N,M = map(int , input().split())
list1 = [ i for i in range(1,N+1)]
list2 = []

for _ in range (0,M):
    i,j,k = map(int, input().split())
    list2 = list1[k-1:j]
    list1[k-1:j] = []
    for l in range(0,len(list2)):
        list1.insert(l+(i-1),list2[l])
print(*list1)
