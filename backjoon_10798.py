list1 = []
result = ''
k = 0
list3 = []
for i in range(5):
    list2 = list(input())
    list1.append(list2)
for i in range(len(list1)):
    list3.append(len(list1[i]))
max1 = max(list3)

for i in range(max1):
    for j in range(len(list1)):
        if len(list1[j]) <= i :
            continue
        else:
            result += list1[j][i]
print(result)

    
    
    

