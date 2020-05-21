def countstar(l):
    s = len (l)
    t = 0
    for i in range(s):
        if (l[i] == '*'): t += 1
    return t    

inp = list(map(int,input().split()))
n = inp[0]
m = inp[1]
l = [0]*m
ma=[]
for i in range(n): ma.append(l.copy())
#ma = [l.copy() for i in range(m)]
matrix = []
for i in range(n):
    matrix.append(input())
for i in range (1,n-1):
    for j in range (1,m-1):
        ma [i][j] = countstar ([matrix [i-1][j],matrix [i+1][j],matrix [i][j+1],matrix [i][j-1],matrix [i-1][j-1],matrix [i-1][j+1],matrix [i+1][j+1],matrix [i+1][j-1]])

for j in range (1,m-1):
    ma [0][j] = countstar ([matrix [0][j-1],matrix [0][j+1],matrix [1][j],matrix [1][j+1],matrix [1][j-1]])
        
for j in range (1,m-1):
    ma [n-1][j] = countstar ([matrix [n-1][j-1],matrix [n-1][j+1],matrix [n-2][j],matrix [n-2][j+1],matrix [n-2][j-1]])
      
for i in range (1,n-1):
    ma [i][0] = countstar ([matrix [i-1][0],matrix [i+1][0],matrix [i][1],matrix [i-1][1],matrix [i+1][1]])

for i in range (1,n-1):
    ma [i][m-1] = countstar ([matrix [i-1][m-1],matrix [i+1][m-1],matrix [i][m-2],matrix [i-1][m-2],matrix [i+1][m-2]])
        
ma [0][0] = countstar ([matrix [1][1],matrix [0][1],matrix [1][0]] )

ma [0][m-1] = countstar ([matrix [1][m-2],matrix [0][m-2],matrix [1][m-1]])

ma [n-1][0] = countstar ([matrix [n-2][0],matrix [n-2][1],matrix [n-1][1]])

ma [n-1][m-1] = countstar ([matrix [n-1][m-2],matrix [n-2][m-1],matrix [n-2][m-2]] )

#for row in ma: print(row)

for i in range(n):
    for j in range(m):
        if matrix[i][j] != '*': print(ma[i][j],end='')
        else: print('*',end='')
    print()
 



        
        
        
            
            
      
    

