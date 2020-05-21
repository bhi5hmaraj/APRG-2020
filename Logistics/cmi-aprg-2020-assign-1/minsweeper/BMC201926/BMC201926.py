import sys

m ,n = map(int,input().split())
matrixr = []
for i in range (0,m):
    matrixr.append(input())
    
def func(a):
    if a == '*':
        return 1
    else:
        return 0

str1 = []
matrix2 = []
for j in range(0, n):
    str1.append(1)
for i in range(0, m):
    matrix2.append(str1[:])

for i in range(0, m):
    for j in range(0, n):
        if matrixr[i][j] == '*':
            matrix2[i][j] = '*'
        elif i == 0 and j == 0:
            matrix2[i][j] = func(matrixr[i][j+1]) + func(matrixr[i+1][j]) + func(matrixr[i+1][j+1])
        elif i == 0 and j == (n-1):
            matrix2[i][j] = func(matrixr[i+1][j]) + func(matrixr[i][j-1]) + func(matrixr[i+1][j-1])
        elif i == (m-1) and j == 0:
            matrix2[i][j] = func(matrixr[i][j+1]) + func(matrixr[i-1][j]) + func(matrixr[i-1][j+1])
        elif i == (m-1) and j == (n-1):
            matrix2[i][j] = func(matrixr[i-1][j-1]) + func(matrixr[i][j-1]) + func(matrixr[i-1][j])
        elif i == 0:
            matrix2[i][j] = func(matrixr[i][j + 1]) + func(matrixr[i + 1][j]) + func(matrixr[i + 1][j + 1]) + func(matrixr[i][j-1]) + func(matrixr[i+1][j-1])
        elif i == (m-1):
            matrix2[i][j] = func(matrixr[i][j + 1]) + func(matrixr[i - 1][j]) + func(matrixr[i - 1][j + 1]) + func(matrixr[i-1][j-1]) + func(matrixr[i][j-1])
        elif j == 0:
            matrix2[i][j] = func(matrixr[i][j + 1]) + func(matrixr[i + 1][j]) + func(matrixr[i + 1][j + 1]) + func(matrixr[i-1][j]) + func(matrixr[i-1][j+1])
        elif j == (n-1):
            matrix2[i][j] = func(matrixr[i + 1][j]) + func(matrixr[i][j - 1]) + func(matrixr[i + 1][j - 1]) + func(matrixr[i-1][j-1]) + func(matrixr[i-1][j])
        else:
            matrix2[i][j] = func(matrixr[i+1][j]) + func(matrixr[i-1][j]) + func(matrixr[i][j+1]) + func(matrixr[i][j-1]) + func(matrixr[i-1][j-1]) + func(matrixr[i+1][j+1]) + func(matrixr[i-1][j+1]) + func(matrixr[i+1][j-1])

for i in range(0, m):
    for j in range(0, n):
        if j == (n-1):
            print(matrix2[i][j])
        else:
            print(matrix2[i][j], end='')
    

    
    
    

