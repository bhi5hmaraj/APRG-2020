from queue import Queue
v,e = [int(i) for i in input().split()]
x,y = [int(i) for i in input().split()]
adjl = [[0 for i in range(v+2)] for j in range(v+2)]
isdisc = [[False for i in range(v+2)] for j in range(v+2)]
for i in range(v+2):
    adjl[0][i] = 1
    adjl[v+1][i] = 1
    adjl[i][0] = 1
    adjl[i][v+1] = 1
for i in range(e):
    xb, yb = [int(i) for i in input().split()]
    adjl[xb][yb] = 1
def bfs(): #code is taken from Lecture 14
    bfsque = Queue()
    isdisc[x][y] = True
    bfsque.put((x,y))
    while (bfsque.empty() == False):
        xw, yw = list(bfsque.get())
        for inc in [[0,-1], [0,+1], [-1, 0], [+1,0]]:
            xn = xw + inc[0]
            yn = yw + inc[1]
            if ((adjl[xn][yn] == 0) and (isdisc[xn][yn] == False)):
                isdisc[xn][yn] = True
                bfsque.put((xn,yn))
def foobar():
    bfs()
    for i in range(1, v+1):
        for j in range(1, v+1):
            if ((adjl[i][j] == 0) and (isdisc[i][j] == False)):
                return "N"
    return "Y"

print(foobar())



