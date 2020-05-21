zz=list(map(int,input().split()))
row,col,mat=zz[0],zz[1],[]
for i in range(row):
    mat.append(input())
    mat[i]=list(mat[i])
def func(r,c):
    ct=0
    for i in range(max(r-1,0), 1+min(r+1,row-1)):
        for j in range(max(c-1,0), 1+min(c+1,col-1)):
            if mat[i][j]=="*":
                ct+=1
    return ct
for i in range(row):
    for j in range(col):
        if mat[i][j]==".":
            mat[i][j]=func(i,j)
for i in range(row):
    for j in range(col):
        print(mat[i][j],end="")
    print()
