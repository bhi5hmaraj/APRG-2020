def checkBnds(r,c,i,j):
    chki = (i>=0) and (i<r)
    chkj = (j>=0) and (j<c)
    return chki and chkj

def addNebs(mat,i,j):
    addi=[-1,0,1]
    addj=[-1,0,1]
    r=len(mat)
    c=len(mat[0])
    
    for iii in range(0,3):
        for jjj in range(0,3):
            modi=i+addi[iii]
            modj=j+addj[jjj]
            if(checkBnds(r,c,modi,modj) and mat[modi][modj]!='*'):
                mat[modi][modj]=str(1+int(mat[modi][modj]))

    return mat

def solve(mat):
    r=len(mat)
    c=len(mat[0])
    
    for i in range(0,r):
        for j in range(0,c):
            if mat[i][j]=='*':
                mat=addNebs(mat,i,j)
    return mat

def start():
    r , c = input().split()
    r = int(r)
    c = int(c)
    
    inp = []
    
    for i in range(0,r):
        x=list(input())
        for j in range(0,c):
            if x[j]=='.':
                x[j]='0'
        inp.append(x)
    out=solve(inp)
    for i in range(0,r):
        print(''.join(out[i]))

    return

start()

