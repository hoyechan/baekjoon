list1 = ['c=','c-','dz=','d-','lj','nj','s=','z=']
x= input()
n=0
flag = 0 
while n <= len(x)-1:
    if x[n:n+2] in list1:
        flag += 1
        n += 2
    elif x[n:n+3] in list1:
        flag+=1
        n+=3
    else:
        flag += 1
        n += 1
print(flag)

#문자열에서 범위를 지정하여 출력할때 뒷범위가 문자열의 길이를 벗어나도 상관이없다. 앞범위만 맞추면 됨.
#ex) str = 'print' 일때 내가 print(str[4:6]) 을 입력한다면 t의 index는 4인데 그것을 넘긴 6이 있어서
#오류가 나지 않을까 하는 생각이 들수도 있다. 하지만 결과로 't'가 출력이 되면서 오류없이 진행된다.
#하지만 print(str[5:6[])이런식으로 친다면 오류가 날 것이다. 
