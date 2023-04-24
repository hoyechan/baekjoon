import statistics 

N = int(input())
aa = list(map(int,input().split()))
aa.sort()
M = aa[N-1]
bb=[]
for i in aa:
    i = i/M*100
    bb.append(i)
print(statistics.mean(bb))
