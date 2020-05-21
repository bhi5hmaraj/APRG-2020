def bfs (Adj,src,dst):
    level = { src: 0 }
    parent = { src: [] }
    path = {src: "" }
    i = 1
    f = [src]
    while f:
        next = [ ]
        for u in f:
            for (x,y) in Adj[u]:
                if x not in level: 
                    level[x] = i
                    parent[x] = [u]
                    path[x] = path[u] + y
                    next.append(x)
                elif x in level and level[x] == level [u] + 1:
                    path[x] = min([path[x],path[u]+y])
            if u == dst:
                break
            else:
                path[u]= ""
        f = next
        i += 1
        
    return (path)
def addEdge(edges, u, v, rank): 
    edges[u-1].append((v,rank))  
    edges[v-1].append((u,rank)) 


    
a = list(map(int,input().split()))
n = a[0]
m = a[1]
b = list(map(int,input().split()))
u = b[0]
v = b[1]
edges = [[] for i in range(n)]

for i in range(m):
    l = list(input().split())
    addEdge(edges,int(l[0]),int(l[2]),l[1])


Adj = {}
for i in range(n):
    Adj[i+1] = edges[i]

print(bfs(Adj,u,v)[v])