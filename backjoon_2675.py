T = int(input())
for i in range(0,T):
    R,S= map(str, input().split())
    R= int(R)
    for j in range(0,len(S)):
        if j == len(S)-1:
            
            print(S[j]*R)
        else :
            print(S[j]*R,end='')
