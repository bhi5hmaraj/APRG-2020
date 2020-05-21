from array import *

m, n=map(int,input().split())

A = []
for i in range(m):
    inp = input()
    A.append(inp)

B  = [['0' for i in range (n+2)] for j in range (m+2)]

for r in range(m):
    for c in range(n):
        if A[r][c]=='*':
            B[r+1][c+1]='*'
            if B[r][c]!='*':
                B[r][c]=(chr)((ord)(B[r][c])+1)
            if B[r+2][c+2]!='*':
                B[r+2][c+2]=(chr)((ord)(B[r+2][c+2])+1)
            if B[r+1][c+2]!='*':
                B[r+1][c+2]=(chr)((ord)(B[r+1][c+2])+1)
            if B[r][c+2]!='*':
                B[r][c+2]=(chr)((ord)(B[r][c+2])+1)
            if B[r+2][c+1]!='*':
                B[r+2][c+1]=(chr)((ord)(B[r+2][c+1])+1)
            if B[r][c+1]!='*':
                B[r][c+1]=(chr)((ord)(B[r][c+1])+1)
            if B[r+2][c]!='*':
                B[r+2][c]=(chr)((ord)(B[r+2][c])+1)
            if B[r+1][c]!='*':
                B[r+1][c]=(chr)((ord)(B[r+1][c])+1)



for r in range(1,m+1):
    c=""
    for x in range(1,n+1):
        c+=B[r][x]
    print(c)
        

