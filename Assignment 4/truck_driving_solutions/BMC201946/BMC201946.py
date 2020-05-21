def kruskal():
    i = 0
    e = 0
    for j in range(n):
        parent.append(j)
    while e < n-1:
        temp = edges[i]
        u = temp[0]
        v = temp[1]
        w = temp[2]
        i = i + 1
        x = u
        while x!=parent[x]:
            x = parent[x]
        y = v
        while y!=parent[y]:
            y = parent[y]
        if x != y:
            e = e+1
            if len(set_queries[y]) > len(set_queries[x]):
                parent[x] = y
            else:
                parent[y] = x
            if parent[x] == y:
                for ll in set_queries[x]:
                    if ll in set_queries[y]:
                        answer[ll] = w 
                        set_queries[y].remove(ll)
                    else:
                        set_queries[y].add(ll)
            else:
                for ll in set_queries[y]:
                    if ll in set_queries[x]:
                        answer[ll] = w 
                        set_queries[x].remove(ll)
                    else:
                        set_queries[x].add(ll)

s = str(input()).split()
n = int(s[0])
m = int(s[1])
edges = []
for i in range(m):
    s = str(input()).split()
    u = int(s[0]) - 1
    v = int(s[1]) - 1
    w = int(s[2])
    edges.append([u,v,w])
    edges.append([v,u,w])
edges.sort(key = lambda x : x[2])
s = str(input()).split()
q = int(s[0])
set_queries = [set([]) for j in range(n)]
answer = [-1 for i in range(q)]
for i in range(q):
    s = str(input()).split()
    u = int(s[0]) - 1
    v = int(s[1]) - 1
    set_queries[u].add(i)
    set_queries[v].add(i)
parent = []
kruskal()
for i in range(q):
    print(answer[i])