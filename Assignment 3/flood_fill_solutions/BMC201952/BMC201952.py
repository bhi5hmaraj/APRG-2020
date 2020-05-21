x = input().split()
y = input().split()
N = int(x[0])
b = int(x[1])
screen = [[1]*(N+2)] + [[1] + [0]*N + [1] for i in range(N)] + [[1]*(N+2)]

for i in range(b):
    z = input().split()
    screen[int(z[0])][int(z[1])] = 1
    
m,n = int(y[0]),int(y[1])
floodfill = [(m,n)]
screen[m][n] = 2

while floodfill:
    coloured = []
    for (x,y) in floodfill:
        neighbours = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
        for (a,b) in neighbours:
            if not screen[a][b]:
                screen[a][b] = 2
                coloured.append((a,b))
    floodfill = coloured[:]
    
notcoloured = []
for line in screen:
    if 0 in line:
        notcoloured.append(1)
        
if notcoloured:
    print('N')
else:
    print('Y')