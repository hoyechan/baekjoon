list1 = list(map(str,input().split()))
for i in range(0,2):
    
    list1[i] = ''.join(reversed(list1[i]))
list1 = map(int, list1)
print(max(list1))
