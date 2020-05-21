l1 = list(map(int, input().split()))
N = l1[0]
M = l1[1]

l2 =  list(map(int, input().split()))
vi = l2[0]-1
vf = l2[1]-1

edgeList = []
for i in range(M):
    edgeList.append(list(input().split()))

for i in range(M):
    edgeList[i][0] = int(edgeList[i][0])
    edgeList[i][2] = int(edgeList[i][2])

A= {}
for i in range(N):
    A[i] = {}

for i in edgeList:
    A[i[0]-1][i[2]-1] = i[1]
    A[i[2]-1][i[0]-1] = i[1]

import queue

visited = [0]*N
level = [-1]*N

def BFS(i):
    for j in range(N):
        visited[j] = 0
        level[j] = -1

    explore = queue.Queue()
    explore.put(i)

    visited[i] = 1
    level[i] = 0

    while not(explore.empty()):
        x = explore.get()
        for j in A[x]:
            if visited[j] == 0 :
                visited[j] = 1
                level[j] = level[x] + 1
                explore.put(j)

BFS(vi)
distvi= level[0:]
BFS(vf)
distvf = level[0:]

path = []

weight= ['|']*N

currentRank = '|'

def scanpath(cL):
    nL = []
    rL = []
    currentRank = '|'
    for u in cL:
        for v in A[u]:
            if distvi[v] == distvi[u]+1 and distvf[v] == distvf[u]-1 :
                if weight[v] == '|':
                    weight[v] = A[u][v]
                    nL.append(v)
                    currentRank = min(currentRank,A[u][v])
                else:
                    if weight[v] > A[u][v]:
                        weight[v] = A[u][v]
                        currentRank = min(currentRank,A[u][v])
    for v in nL:
        if weight[v] == currentRank:
            rL.append(v)

    return([currentRank,rL])
currentList = [vi]
while currentList != [vf]:
    l = scanpath(currentList)
    path.append(l[0])
    currentList = l[1]

print(''.join(map(str,path)))