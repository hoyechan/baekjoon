X = int(input())
N = int(input())
sum1=0 
for i in range(1, N+1):
    a,b=map(int,input().split())
    sum1 += a*b
print(sum1)
if (sum1 ==X):
    print('Yes')
else :
    print('No')
