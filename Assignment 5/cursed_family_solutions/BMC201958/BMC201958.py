n = int((input().split())[0])
edgelist = []
adj = {}
child = {}
parent = {}
for i in range(n):
    adj[i+1] = []
    child[i+1] = []
    parent[i+1]= []
for i in range(n-1):
    l = list(map(int, input().split()))
    edgelist.append(l)
    adj[l[0]].append(l[1])
    adj[l[1]].append(l[0])
    child[l[0]].append(l[1])
    parent[l[1]].append(l[0])
root = [x for x in parent if parent[x] == []][0]
grandchild = {}
for i in range(n):
    grandchild[i+1] = []
for i in range(n):
    for x in child[i+1]:
        grandchild[i+1].extend(child[x])

def bfs (Adj,src):
    bfslevel = { src: 0 }
    predecessor = { src: None }
    levelset ={0:[src]}
    i = 1
    f = [src]
    while f:
        levelset[i] = []
        next = [ ]
        for u in f:
            for v in Adj[u]:
                if v not in bfslevel: 
                    bfslevel[v] = i
                    predecessor[v] = u
                    levelset[i].append(v)
                    next.append(v)
        f = next
        i += 1
    return bfslevel,levelset
dic,lvl = bfs(adj,root)
k = max(dic.values())
def mis(Adj,root):
    L = [0 for i in range(n+1)]
    for i in range(k+1):
        for v in lvl[k-i]:
            if child[v]== []:
                L[v]=1
            else:
                L[v] = max(sum([L[x] for x in child[v]]), 1 +sum([L[x] for x in grandchild[v]]) )

    return (L)
print(mis(adj,root)[root])
