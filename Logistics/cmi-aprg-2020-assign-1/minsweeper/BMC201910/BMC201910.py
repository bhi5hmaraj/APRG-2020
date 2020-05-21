def check(mat, i, j ):
    c=0
    if (mat[i+1][j+1]=='*'):
        c=c+1
    if (mat[i+1][j]=='*'):
        c=c+1
    if (mat[i+1][j-1]=='*'):
        c=c+1
    if (mat[i][j+1]=='*'):
        c=c+1    
    if (mat[i][j-1]=='*'):
        c=c+1
    if (mat[i-1][j+1]=='*'):
        c=c+1
    if (mat[i-1][j]=='*'):
        c=c+1
    if (mat[i-1][j-1]=='*'):
        c=c+1
    return(c)

l = map(int,raw_input().split())
n = l[0]
m = l[1]
mat = [[0]*(m+2)]
for i in range(n):
    temp = map(str,raw_input().split())
    temp = list(temp[0])
    temp = ['0']+temp+['0']
    mat = mat+[temp]
mat = mat+[[0]*(m+2)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if mat[i][j]!='*':
            mat[i][j]=check(mat,i,j)
        
for i in range(1,n+1):
    y=""
    for j in range(1,m+1):
        y=y+str(mat[i][j])
    print(y)
            
        
    
    

