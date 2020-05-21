# Flood Fill

l1 = list(map(int, input().split()))
N = l1[0]
b = l1[1]

l2 = list(map(int, input().split()))

l3=[]
for i in range(b):
    l3.append(list(map(int, input().split())))

M= [[0 for i in range(N)] for j in range(N)]

def convert(c):
    return M[c[0]][c[1]]

for c in l3:
    M[c[0]-1][c[1]-1] = 1

import queue

def nbd(c):
    nbd=[]
    if c[0]-1 >=0:
        nbd.append([c[0]-1,c[1]])
    if c[0]+1 < N:
        nbd.append([c[0]+1,c[1]])
    if c[1]-1 >=0:
        nbd.append([c[0],c[1]-1])
    if c[1]+1 <N:
        nbd.append([c[0],c[1]+1])
    return nbd

def flFill(c):
    
    M[c[0]][c[1]] = -1
    
    explore = queue.Queue()
    explore.put(c)

    def exploring(c):
        for i in nbd(c):
            if convert(i)==0:
                M[i[0]][i[1]] = -1
                explore.put(i)

    while not(explore.empty()):
        x = explore.get()
        exploring(x)

def findWhite(M):
    for i in M:
        for j in i:
            if j==0:
                return True
    return False


flFill([l2[0]-1,l2[1]-1])

if findWhite(M):
    print('N')
else:
    print('Y')