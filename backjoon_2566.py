import sys 
list1 = []
list3 = []
for i in range(9):
    list2 = list(map(int, sys.stdin.readline().split()))
    list1.append(list2)
for i in range(9):
    list3.append(max(list1[i]))
max1 = max(list3)
print(max1)
index = list3.index(max1)
print(index+1,list1[index].index(max1)+1)
