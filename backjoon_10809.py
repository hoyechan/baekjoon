list1 = [ chr(i) for i in range(97,123)]
S = input()
for i in range(0,26):
    print(S.find(list1[i]),end=' ')
