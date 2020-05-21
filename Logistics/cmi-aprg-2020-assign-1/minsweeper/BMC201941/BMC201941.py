input1 = list(map(int,input().split()))
n = input1[0] 
m = input1[1] 
s = []
for i in list(range(1,n+1)):
    s.append(list(input()))
for i in list(range(0,n)):
    for j in list(range(0,m)):
        count=0
        if s[i][j]==".":
            for k in list(range((max(i-1,0)),min(i+2,n))):
                for l in list(range(max(j-1,0),min(j+2,m))):
                    if s[k][l]=="*":
                        count+=1
            s[i][j] = count
for i in list(range(0,n)):
    for j in list(range(0,m)):
        print(s[i][j],end='')
    print()

