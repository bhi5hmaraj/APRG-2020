l = list(map(int,input().split()))
r,c = l[0], l[1]
li = []
for i in range(r):
    li.append(input())
    li[i] = list(li[i])
for a in range(r):
    for b in range(c):
        if li[a][b]==".":
            count = 0
            for i in range(max(a-1,0),min(r,a+2)):
                for j in range(max(b-1,0), min(c,b+2)):
                    if li[i][j]=="*":
                        count+=1
            li[a][b]=str(count)
for i in range(r):
    for j in range(c):
        print(li[i][j],end='')
    print()
                    
