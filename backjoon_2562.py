aa=[]
for i in range(0,9):
    x = int(input())
    aa.append(x)
print(max(aa))
print(aa.index(max(aa))+1)
