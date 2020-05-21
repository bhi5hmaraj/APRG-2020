n,m= map(int,input().split())
mat=[]
li=[]
for i in range(n):
    mat.append(list(map(str,input())))

def change(mat,a,b):
    ct=0
    for g in range(3):
        for k in range(3):
            if((i-1+g,j-1+k) in li):
              ct=ct+1
    return (ct)
       
for i in range(n):
    for j in range(m):
        if(mat[i][j] == '*'):
           li.append((i,j))

for i in range(n):
    for j in range(m):
        if(mat[i][j] == '.'):
          mat[i][j]=change(mat,i,j)
    
for i in range(n):
    print(''.join(map(str,mat[i])))

