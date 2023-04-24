aa = []
for i in range (1,31):
    aa.append(i)
for i in range(0,28):
    x = int(input())
    index = aa.index(x)
    del(aa[index])
for i in range(0,2):
    print(aa[i])
