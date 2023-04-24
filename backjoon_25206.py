
dic = {'A+':4.5, 'A0': 4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0.0}
sum1 = 0
ahr = 0 
for i in range(20):
    a, b, c= map(str, input().split())
    if c =='P':
        continue
    else:
        c1 = dic[c]
        b = float(b)
        sum1 += c1*b
        ahr += b 
print(sum1/ahr)
