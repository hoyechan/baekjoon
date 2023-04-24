# 변수 지정#
sum1 =0
list1 = []
x = ''
list2 = []
# 메인 코드 #
x = input()
list1 = [ chr(i) for i in range(65, 91)]
for i in range (0,len(x)):
    
    if x[i] in list1[0:3]:
        list2.append(2)
    elif x [i] in list1[3:6]:
        list2.append(3)
    elif x [i] in list1[6:9]:
        list2.append(4)
    elif x [i] in list1[9:12]:
        list2.append(5)
    elif x [i] in list1[12:15]:
        list2.append(6)
    elif x [i] in list1[15:19]:
        list2.append(7)
    elif x [i] in list1[19:22]:
        list2.append(8)
    elif x [i] in list1[22:]:
        list2.append(9)
    else:
        continue
print(sum(list2)+len(list2))
