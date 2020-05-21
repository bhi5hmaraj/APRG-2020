def bfs(i,j, G):
    q = [(i,j)]
    while q:
        node = q.pop(0)
        i = node[0]
        j = node[1]
        for (x,y) in [(i,j-1),(i,j+1),(i-1,j),(i+1,j)]:
            if not G[x][y]: 
                q.append((x,y))
                G[x][y] = True
[N,b] = list(map(int,input().split()))
[p,q] = list(map(int,input().split()))
G = [[True for i in range(N+2)]]
for j in range(N):
    r = [True] + [False for i in range(N)] + [True]
    G.append(r)
G.append([True for i in range(N+2)])
for i in range(b): 
    [a,b] = list(map(int,input().split()))
    G[a][b] = True
G[p][q] = True
bfs(p,q,G)
a = 'Y'
for i in range(1,N+1):
    if a=='N': break
    for j in range(1,N+1):
        if not G[i][j]:
            a = 'N'
            break
print(a)