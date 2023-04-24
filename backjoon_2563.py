# x좌표 y좌표

N = int(input())
matrix = [[ 0 for _ in range(100)] for _ in range(100)]

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y,y+10):
            matrix[i][j] = 1
print(sum([sum(matrix[i]) for i in range (100)]))
