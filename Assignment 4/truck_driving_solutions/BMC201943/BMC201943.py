list_firstLine =  list(map(int,input().split()))
N = list_firstLine[0]
M = list_firstLine[1]
edges = []
for i in range(M):
    (u,v,w) = map(int,input().split())
    edges.append((w,u,v))
edges.sort()

parent = [i for i in range(N+1)]

def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])
    return parent[n]
    
q = [set() for i in range(N+1)]

freak_line = list(map(int,input().split()))
Q = freak_line[0]
for i in range(Q):
    (u,v) = map(int,input().split())
    q[u].add(i)
    q[v].add(i)
    
#kruskal part
answer = [0 for i in range(Q)]
c = 0
for edge in edges:
    if (c==N-1): break
    (w,u,v) = edge
    a = find(u)
    b = find(v)
    if (a != b):
        if (len(q[b])>len(q[a])):
                 a = a+b
                 b = a-b
                 a = a-b
        c = c+1
        for i in q[b]:
              if i in q[a]: 
                     answer[i] = w
                     q[a].remove(i)
              else: q[a].add(i)
        parent[b] = a
for i in answer:
    print (i)