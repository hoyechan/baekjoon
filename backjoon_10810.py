import sys

N,M=map(int, input().split())
bagu = []
for _ in range(0,N):
    bagu.append(0)
for _ in range(0,M):
    i,j,k = map(int, sys.stdin.readline().split())
    bagu[i-1:j]=[k]*(j-(i-1))
for i in range(0,len(bagu)):
    print(bagu[i],end=' ')
