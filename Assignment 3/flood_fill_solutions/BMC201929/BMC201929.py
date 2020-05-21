class pixel:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.color = 'W'
        self.neighbours = [] 

[N, b] = input().split()
N = int(N)
b = int(b)
M = []
for j in range(N):
    list = []
    for k in range(N):
        P = pixel(j+1, k+1)
        list.append(P)
    M.append(list)
    
start = input().split()

for x in range(b):
    [i, j] = input().split()
    i = int(i) - 1
    j = int(j) - 1
    M[i][j].color = 'B'
    
def updateneighbours(P):
    if P.i < N:
        P.neighbours.append(M[P.i][P.j - 1])
    if P.j < N:
        P.neighbours.append(M[P.i - 1][P.j])
    if P.i > 1:
        P.neighbours.append(M[P.i - 2][P.j - 1])
    if P.j > 1:
        P.neighbours.append(M[P.i - 1][P.j - 2])
    return P

for i in range(N):
    for j in range(N):
        M[i][j] = updateneighbours(M[i][j])
            
            

def printgrid(M):
    for x in range(N):
        for y in range(N):
            print(M[x][y].color, end = " ")
        print('\n')
            
i = int(start[0])
j = int(start[1])
start = M[i-1][j-1]
def floodfill(M, start):
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node.color == 'W':
            node.color = 'G'
            for neighbour in node.neighbours:
                queue.append(neighbour)
    
floodfill(M, start)
k = 0
for m in range(N):
    for n in range(N):
        if M[m][n].color == 'W':
            k = 1
if k == 0:
    print('Y')
else:
    print('N')
    
