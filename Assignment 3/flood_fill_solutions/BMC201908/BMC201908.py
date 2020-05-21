color = 0
def isWhiteAvailable(M, N):
    for i in range(0,N):
        for j in range(0,N):
            if M[i][j] == 0:
                return "N"
    return "Y"

def fillUtil(M, xw, yw, N):
    '''
    global color
    color = color - 1
    M[xw][yw] = 2
    if (xw-1>=0 and xw-1<N and yw>=0 and yw<N and M[xw-1][yw]!=1 and M[xw-1][yw]!=2):
        fillUtil(M, xw-1, yw, N)
    if (xw+1>=0 and xw+1<N and yw>=0 and yw<N and M[xw+1][yw]!=1 and M[xw+1][yw]!=2):
        fillUtil(M, xw+1, yw, N)
    if (xw>=0 and xw<N and yw-1>=0 and yw-1<N and M[xw][yw-1]!=1 and M[xw][yw-1]!=2):
        fillUtil(M, xw, yw-1, N)
    if (xw>=0 and xw<N and yw+1>=0 and yw+1<N and M[xw][yw+1]!=1 and M[xw][yw+1]!=2):
        fillUtil(M, xw, yw+1, N)
    return 
    '''
    stack = []
    stack.append((xw,yw))
    
    while stack:
        x,y = stack.pop()
        if M[x][y]!=1 and M[x][y]!=2:
            M[x][y] = 2
            if x>0:
                stack.append((x-1, y))
            if x<N-1:
                stack.append((x+1, y))
            if y>0:
                stack.append((x,y-1))
            if y<N-1:
                stack.append((x,y+1))
        

def canFillAll(M, xw, yw, N):
    fillUtil(M, xw, yw, N)
    global color
    return isWhiteAvailable(M,N)
    # if color == 0:
        # return "Y"
    # return "N"

import sys
inp1 = str(input()).strip().split(" ")
N = int(inp1[0])
b = int(inp1[1])
color = N*N - b
sys.setrecursionlimit(N*N)
inp2 = str(input()).strip().split(" ")
xw = int(inp2[0])
yw = int(inp2[1])
M = []
t = []
for i in range(0,N):
    for j in range(0,N):
        t.append(0)
    M.append(t)
    t=[]
for i in range(0,b):
    inp = str(input()).strip().split(" ")
    M[int(inp[0])-1][int(inp[1])-1] = 1  
print(canFillAll(M, xw-1, yw-1, N))
    