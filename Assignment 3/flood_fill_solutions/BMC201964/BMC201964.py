from queue import Queue

n,b = map(int, input().split())
u1, u2 =  map(int, input().split())

black = [[0 for i in range(n+2)] for j in range(n+2)]
vis = [[0 for i in range(n+2)] for j in range(n+2)]

for i in range(n+2):
    black[0][i] = 1
    black[i][0] = 1
    black[n+1][i] = 1
    black[i][n+1] =1

bb = 0
for _ in range(b):
    x,y =  map(int, input().split())
    if(black[x][y] == 0):
        black[x][y] = 1
        bb+=1

q = Queue()
q.put([u1,u2])
vis[u1][u2] = 1

c = 1

while(q.empty() == False):
    t = q.get()
    lis = [[t[0]-1,t[1]],[t[0]+1,t[1]],[t[0],t[1]-1],[t[0],t[1]+1]]
    for nb in lis:
        if(vis[nb[0]][nb[1]] == 0 and black[nb[0]][nb[1]] == 0):
            c += 1
            vis[nb[0]][nb[1]] = 1
            q.put([nb[0],nb[1]])


if(c == (n*n - bb)):
    print('Y')
else: print('N')