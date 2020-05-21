def kruskal(vertices):
    Parent = []
    (i,e) = (0,0)
    for j in range(vertices):
        Parent.append(j)
    while e != vertices - 1:
        A = Edges[i]
        (u,v,w) = (A[0],A[1],A[2])
        i = i + 1
        while u != Parent[u]:
            u = Parent[u]
        while v != Parent[v]:
            v = Parent[v]
        if u != v:
            e = e+1
            if len(set_queries[v]) > len(set_queries[u]):
                Parent[u] = v
            else:
                Parent[v] = u
            if Parent[u] == v:
                for ll in set_queries[u]:
                    if ll in set_queries[v]:
                        answer[ll] = w 
                        set_queries[v].remove(ll)
                    else:
                        set_queries[v].add(ll)
            else:
                for ll in set_queries[v]:
                    if ll in set_queries[u]:
                        answer[ll] = w 
                        set_queries[u].remove(ll)
                    else:
                        set_queries[u].add(ll)

s = str(input()).split()
N,M = int(s[0]),int(s[1])
Edges = []
for i in range(M):
    s = str(input()).split()
    (u,v,w) = (int(s[0]) - 1, int(s[1])-1, int(s[2]))
    Edges.append([u,v,w])
    Edges.append([v,u,w])
Edges.sort(key = lambda x : x[2])
s = str(input()).split()
Q = int(s[0])
set_queries = [set([]) for j in range(N)]
answer = [-1]*Q
for i in range(Q):
    s = str(input()).split()
    u,v = int(s[0]) - 1, int(s[1]) - 1
    set_queries[u].add(i)
    set_queries[v].add(i)
kruskal(N)
for i in range(Q):
    print(answer[i])