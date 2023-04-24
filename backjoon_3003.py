list1 =list(map(int, input().split()))
list2 =[1,1,2,2,2,8]
list3 =[]
for i in range(len(list2)):
    list3.append(list2[i] - list1[i])
print(*list3)
