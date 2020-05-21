n, m = map(int, input().split())
roads = []
for i in range(0, m):
    roads.append(list(map(int, input().split())))

q = int(input())
queries = []
for i in range(0, q):
    queries.append(list(map(int, input().split())))

qory = [set([]) for i in range(n)]                                     # Each set for a vertex represents which query numbers have the vertex
for i in range(q):
    qory[queries[i][0] - 1].add(i)
    qory[queries[i][1] - 1].add(i)

edges = [[] for i in range(m)]
for i in range(m):
    edges[i].append(roads[i][2])
    edges[i].extend([roads[i][0], roads[i][1]])
edges.sort()
answers = [0 for i in range(q)]
parent = [i for i in range(n)]


TE = []                                                                 # List of edges that we're adding
while len(TE) < n - 1:
    for i in edges:        
        [w,u,v] = [i[0],i[1]-1,i[2]-1]
        while u != parent[u]:
            u = parent[u]
        while v != parent[v]:
            v = parent[v]
        if u!= v:
            if len(qory[u]) < len(qory[v]):
                parent[u] = v
            else:
                parent[v] = u       
            if parent[u] == v:
                for j in qory[u]:
                    if j in qory[v]:
                        answers[j] = w
                        qory[v].remove(j)
                    else:
                        qory[v].add(j)
            else:
                for j in qory[v]:
                    if j in qory[u]:
                        answers[j] = w
                        qory[u].remove(j)
                    else:
                        qory[u].add(j)
            TE.append(i)

for i in answers:
    print(i)
