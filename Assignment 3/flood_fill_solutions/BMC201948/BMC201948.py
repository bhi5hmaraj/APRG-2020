from queue import Queue

N, b = [int(x) for x in input().split()]
istart, jstart = [(int(x)-1) for x in input().split()]
mp = [[0 for j in range(0, N)] for i in range(0, N)]

bb= 0
for i in range(0, b):
    p, q = [(int(x)-1) for x in input().split()]
    if(mp[p][q] != 1):
        mp[p][q] = 1
        bb+=1
buf = Queue()
#print(istart,jstart)

def getNb(i, j):
    c = []
    if i - 1 >= 0 and mp[i-1][j] == 0:
        c.append((i-1, j))
    if j-1>=0 and mp[i][j-1] == 0:
        c.append((i, j-1))
    if i+1 < N and mp[i+1][j] == 0:
        c.append((i+1, j))
    if j+1 < N and mp[i][j+1] == 0:
        c.append((i, j+1))
    return c

visited = 0
mp[istart][jstart] = 2
buf.put((istart, jstart))

while (not buf.empty()):
    (a,c) = buf.get()
    visited += 1
    nbs = getNb(a, c)
    for (x, y) in nbs:
        #print(a,b," : ",x,y)
        mp[x][y] = 2
        buf.put((x,y))
            
#print(visited)
if visited == (N*N - bb):
    print("Y") 
else:
    print('N')