A = []
B = []
N, M = map(int, input().split())
for i in range(0,N):
    list1 = list(map(int, input().split()))
    A.append(list1)
for i in range(N):
    list1 = list(map(int, input().split()))
    B.append(list1)
for i in range(N):
    for j in range(M):
        print(A[i][j]+B[i][j],end=' ')
    print()
