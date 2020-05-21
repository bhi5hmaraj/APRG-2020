l=list(map(int,input().split()))
n = l[0]
m = l[1]
x = []
i=0
while(i<n):
    x.append(input())
    x[i]=list(x[i])
    i+=1
def f(r,c):
    num=0
    for i in range(max(r-1,0), min(r+2,n)):
        for j in range(max(c-1,0), min(c+2,m)):
            if x[i][j]=="*":
                num+=1
    return num
for i in range(n):
    for j in range(m):
        if x[i][j]==".":
            x[i][j]=f(i,j)
for i in range(n):
    for j in range(m):
        print(x[i][j],end="")
    print()
