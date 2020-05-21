m, n = map(int,input().split())
a, b = map(int,input().split())
matrix = []
for i in range(0, n):
    matrix.append(list(map(int, list(input().split()))))
    
matrixr =  [[0 for x in range(m)] for y in range(m)]

for i in matrix:
    matrixr[i[0]-1][i[1]-1] = 2
            

def ifposssible(l):
    if l[0] in range(0, m) and l[1] in range(0,m):
        return True

def neighbour(i,j):
    t = []
    for k in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
        if ifposssible(k):
            t.append(k)
    return t

matrixr[a-1][b-1] = 1
q = [[a-1,b-1]]
while q:
    a1 = q.pop(0)
    for i in neighbour(a1[0],a1[1]):
        if matrixr[i[0]][i[1]] == 0:
            matrixr[i[0]][i[1]] = 1
            q.append(i)

s = 0
r = 0
for i in range(0, m):
    for j in range (0,m):
        if matrixr[i][j] == 1:
            s = s + 1
        elif matrixr[i][j] == 2:
            r = r + 1

if s == m**2 - r:
    print('Y')
else:
    print('N')

                  
