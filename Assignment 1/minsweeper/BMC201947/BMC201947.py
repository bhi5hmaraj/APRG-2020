s = list (map (int, input ().split ()))
n=s[0]
m=s[1]
l=[]
for i in range(0,n):
    l.append(str(input()))
copy=[]
for i in range(0,n+2):
    copy.append([])
for i in range(0,n+2):
    for j in range(0,m+2):
        copy[i].append(0)
for i in range(0,n):
    for j in range(0,m):
        if (l[i][j]=='*'):
            copy[i][j]=copy[i][j]+1          
            copy[i][j+1]=copy[i][j+1]+1       
            copy[i][j+2]=copy[i][j+2]+1          
            copy[i+1][j]=copy[i+1][j]+1         
            copy[i+1][j+2]=copy[i+1][j+2]+1
            copy[i+2][j]=copy[i+2][j]+1
            copy[i+2][j+1]=copy[i+2][j+1]+1
            copy[i+2][j+2]=copy[i+2][j+2]+1
l2=[]
for i in range(0,n):
    l2.append('')
for i in range(0,n):
    for j in range(0,m):
        if l[i][j]==".":
            l2[i]=l2[i]+str(copy[i+1][j+1])
        else:
            l2[i]=l2[i]+'*'
    print(l2[i])
