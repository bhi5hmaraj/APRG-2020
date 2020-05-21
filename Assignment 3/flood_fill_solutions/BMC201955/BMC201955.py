import sys

lst = list(map(int,input().split(" ")))
lst1 = list(map(int,input().split(" ")))
(m,n) = (lst[0],lst[1])
(p,q) = (lst1[0],lst1[1])
matrix = []
for i in range(n):
    matrix.append(list(map(int,input().split(" "))))

lsst = [[0]*m]*m
for i in range(n):
        a = matrix[i][0]
        b = matrix[i][1]
        lsst[a-1][b-1] = 2
lsst[p-1][q-1] = 1

def func(lsst1):
    m1 = len(lsst1)
    for i in range(m1):
        for j in range(m1):
            if lsst1[i][j] == 1:
                if ((i-1) in range(m1)) and (lsst1[(i-1)][j] == 0):
                    lsst1[(i-1)][j] = 1
                elif ((i+1) in range(m1)) and (lsst1[(i+1)][j] == 0):
                    lsst1[(i+1)][j] = 1
                elif ((j-1) in range(m1)) and (lsst1[i][(j-1)] == 0):
                    lsst1[i][(j-1)] = 1
                elif ((j+1) in range(m1)) and (lsst1[i][(j+1)] == 0):
                    lsst1[i][(j+1)] = 1
    return(lsst1)

for i in range(m):
    for j in range(m):
        if lsst[i][j] == 0:
            lsst = func(lsst)

t = "Y"
for i in range(m):
    for j in range(m):
        if lsst[i][j] == 0:
            t = "N"
            break
sys.stdout.write(t)
