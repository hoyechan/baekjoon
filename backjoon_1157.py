#변수 지정 #

str1 = input()
list1 = []

# 메인 코드 #

#str1이 소문자가 된 모습을 저장

str2 = str1.lower()

#str1 을 원소만 남게 하기
newstr1 = sorted(list(set(str1.lower())))

                      
#str2에서 newstr1의 원소의 숫자 세기
for i in newstr1:
    num = str2.count(i)
    list1.append(num)
if list1.count(max(list1)) == 1 :
    index = list1.index(max(list1))
    print(newstr1[index].upper())
else:
    print("?")

