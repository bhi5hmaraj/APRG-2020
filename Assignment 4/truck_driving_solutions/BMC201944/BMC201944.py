from queue import PriorityQueue

N,M = map(int, input().split())
A = []
for _ in range(M):
    a,b,w = map(int, input().split())
    A.append((w,a,b))

Q = int(input())
queryList = [set() for i in range(N+1)]
for i in range(Q):
    p,q = map(int, input().split())
    if p != q :
        queryList[p].add(i)
        queryList[q].add(i)

answerList = [0 for i in range(Q)]
parent = [i for i in range(N+1)]

def findRoot(v):
    if parent[v] != v:
        parent[v] = findRoot(parent[v])
    return parent[v]

def uniteRoot(x,y,z):
    if len(queryList[x]) < len(queryList[y]):
        parent[x] = y
        for q in queryList[x]:
            if q in queryList[y]:
                queryList[y].remove(q)
                answerList[q] = z
            else:
                queryList[y].add(q)
        queryList[x].clear()
    else:
        parent[y] = x
        for q in queryList[y]:
            if q in queryList[x]:
                queryList[x].remove(q)
                answerList[q] = z
            else:
                queryList[x].add(q)                
        queryList[y].clear()

def Kruskal(graph):
    graph.sort()

    MSTedgeCounter = 0
    edgeCounter = 0

    while MSTedgeCounter < N-1 :

        w,u,v = graph[edgeCounter]
        edgeCounter += 1
        Ru = findRoot(u)
        Rv = findRoot(v)
        
        if Ru != Rv:
            MSTedgeCounter += 1
            uniteRoot(Ru,Rv,w)        

Kruskal(A)

for i in answerList:
    print(i)