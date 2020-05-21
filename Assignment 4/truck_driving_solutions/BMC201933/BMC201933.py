li = list(map(int, input().split()))
n = li[0]
m = li[1]
A = []
for i in range(m):
    li = list(map(int, input().split()))
    A.append((li[2],li[0]-1,li[1]-1))
Q = [set() for i in range(n)]
q = int(input())
for i in range(q):
    li = list(map(int, input().split()))
    Q[li[0]-1].add(i)
    Q[li[1]-1].add(i)
parent = [i for i in range(n)]
distance = [0 for i in range(q)]
def root(v):
    if parent[v] == v:
        return v
    else:
        return root(parent[v])
distance = [0 for i in range(q)]
A.sort()
for i in range(m):
    x = root(A[i][1])
    y = root(A[i][2])
    if x != y:
        if len(Q[x]) < len(Q[y]):
        
            z = x
            x = y
            y = z
        if len(Q[x]) >= len(Q[y]):
            for query in Q[y]:
                if query in Q[x]:
                    distance[query] = A[i][0]
                    Q[x].remove(query)
                else:
                    Q[x].add(query)
            parent[y] = x

for i in range(q):
    print(distance[i])