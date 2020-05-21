inputm = list(map(int, input().split()))
n = inputm[0]
m = inputm[1]
minesweeper=[]
for i in range (n):
    minesweeper.append(input())
def count(i,j):
    c=0
    if (i+1 < n and j+1 < m and minesweeper[i+1][j+1]=='*'):
        c+=1
    if (0<= i-1 < n and j+1 < m and minesweeper[i-1][j+1]=='*'):
        c+=1
    if (i < n and j+1 < m and minesweeper[i][j+1]=='*'):
        c+=1
    if (i+1 < n and 0<= j-1 < m and minesweeper[i+1][j-1]=='*'):
        c+=1
    if (0<= i-1 < n and 0<= j-1 < m and minesweeper[i-1][j-1]=='*'):
        c+=1
    if (i < n and 0<= j-1 < m and minesweeper[i][j-1]=='*'):
        c+=1
    if (i+1 < n and j < m and minesweeper[i+1][j]=='*'):
        c+=1
    if (0<= i-1 < n and j < m and minesweeper[i-1][j]=='*'):
        c+=1
    return c
for i in range (n):
    printl = ""
    for j in range (m):
            if minesweeper[i][j]=='*': 
                printl = printl + "*"
            else:
                printl = printl + str(count(i,j))
    print(printl)
    

    
