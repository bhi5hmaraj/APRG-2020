first_Line = list(map(int,input().split()))
n = first_Line[0]

parent = [0 for i in range(n+1)]
childList = [[] for i in range(n+1)]
gchildList = [[] for i in range(n+1)]
Adj = [[] for i in range(n+1)]
for i in range(n-1):
    (u,v) = map(int,input().split())
    parent[v] = u
    childList[u].append(v)
    Adj[u].append(v)
    Adj[v].append(u)

for i in range(1,n+1):
    for j in childList[i]:
        for k in childList[j]:
            gchildList[i].append(k)


level = [0 for i in range(n+1)]
visited = [0 for i in range(n+1)]
root = 0
for i in range(1,n+1):
    if (parent[i] == 0):
        root = i

leaf = {}
for i in range(n+1):
    if (childList[i] == []):
        leaf[i] = 1

            
levelSet = [[] for i in range(n+1)] 
Q = []
visited[root] = 1
levelSet[0].append(root)
Q.append(root)
while (Q != []):
    v = Q.pop()
    t = level[v]+1
    for i in Adj[v]:
        if (visited[i] == 0):
            visited[i] = 1
            level[i] = level[v]+1
            levelSet[t].append(i)
            Q.append(i)
    visited[v] = 2
m = max(level)

c = [0 for i in range(n+1)]

for n in leaf:
    c[n] = 1
for i in range(1,m+1):
    for j in levelSet[m-i]:
        if (j not in leaf):
            sum1 = 0
            sum2 = 1
            for k in childList[j]:
                sum1 = c[k] + sum1
            for t in gchildList[j]:
                sum2 = c[t] + sum2
            c[j] = max (sum1,sum2)
print (c[root])