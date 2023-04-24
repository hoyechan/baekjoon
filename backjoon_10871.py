

N,X = map(int, input().split())
list1 = list(map(int,input().split()))
aa = []
for i in range(0,N):
    k = min(list1[i],X)
    if k != X :
        aa.append(k)
    else:
        continue
for j in range(0,len(aa)):
    print(aa[j],end=' ')

# for 문에서 range( ) 가 들어가는자리에 리스트가 들어가도 된다
