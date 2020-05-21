n, m = map(int, input().split())

li = []
for i in range(n):
    li.append(str(input()))

li1=[]
for i in range(n+2):
    li1.append([])
for i in range(n+2):
    for j in range(m+2):
        li1[i].append(0)

for i in range(0,n):
    for j in range(0,m):
        if (li[i][j]=='*'):
            li1[i][j]=li1[i][j]+1          
            li1[i][j+1]=li1[i][j+1]+1       
            li1[i][j+2]=li1[i][j+2]+1          
            li1[i+1][j]=li1[i+1][j]+1         
            li1[i+1][j+2]=li1[i+1][j+2]+1
            li1[i+2][j]=li1[i+2][j]+1
            li1[i+2][j+1]=li1[i+2][j+1]+1
            li1[i+2][j+2]=li1[i+2][j+2]+1

            
li2=[]
for i in range(n):
    li2.append('')
for i in range(n):
    for j in range(m):
        if li[i][j]==".":
            li2[i]=li2[i]+str(li1[i+1][j+1])
        else:
            li2[i]=li2[i]+'*'
    print(li2[i])            

