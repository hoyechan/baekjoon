C = int(input())
for _ in range(C):
    flag = 0 
    t = list(map(int, input().split()))
    del(t[0])
    num = sum(t)/len(t)
    for i in t:
        if i > num:
            
            flag += 1
        else:
            continue 
    print("{:.3f}%".format(flag*100/len(t)))
        
