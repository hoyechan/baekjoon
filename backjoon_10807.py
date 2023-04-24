'''N = int(input())
str1 = input()
list1 = list(str1.split())
v = int(input())
sum1 =0
list2 = [int(x) for x in list1]
for i in range(0,N):
    if list2[i] == v:
        sum1+=1
    else:
        continue
print(sum1)'''

N = int(input())
list1 = list(map(int, input().split()))

v = int(input())

print(list1.count(v))

#map을 유도리있게 사용하자..
