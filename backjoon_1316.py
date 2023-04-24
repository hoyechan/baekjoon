N = int(input())
flag = 0
b = 0
c = 0 
for i in range(N):
    flag = 0
    b = 0
    list1 =[]
    list2 =[] 
    x = input()
    for j in range(len(x)):
        if j == 0 :
            list1.append(x[j])
        elif j !=0 and x[j]== x[j-1] :
            list1.append(x[j])
        elif j !=0 and x[j] != x[j-1] :
            list2.append(list1)
            list1=[]
            list1.append(x[j])
    list2.append(list1)
    for i in range(len(list2)):
        for j in range (len(list2)):
            if set(list2[i]) & set(list2[j]) == set(list2[i]) and i != j:
                flag += 1
            else:
                continue 
        if flag > 0 :
            b += 1
        else:
            continue
    if b == 0 :
        c +=1
print(c) 
