import heapq

n, K = map(int, input().split())
T = list(map(int, input().split()))
blu = [list(map(int, input().split())) for i in range(n)]

red = [[] for i in range(n*100)]
alp = dict()

for i in range(n):
    for j in range(len(blu[i])-1):
        u, v = 100*i + blu[i][j], 100*i + blu[i][j+1]
        red[u].append(v)
        red[v].append(u)
        alp[(u,v)] = alp[(v,u)] = (v-u) * T[i]
        
    for j in range(len(blu[i])):
        if blu[i][j] == 0: continue
        u = 100*i + blu[i][j]
        for k in range(i+1, n):
            w = 100*k + blu[i][j]
            if blu[i][j] in blu[k]:
                red[u].append(w)
                red[w].append(u)
                alp[(u,w)] = alp[(w,u)] = 60



def dijkstra(x, k): 
    dist = [10**10] * (n*100)
    dist[x] = 0
    mark = [False] * (n*100)
    qu = [(0, x)]
    while qu:
        d, v = heapq.heappop(qu)
        if mark[v]: continue
        mark[v] = True
        for u in red[v]:
            alt = dist[v] + alp[(v, u)]
            if alt < dist[u]:
                dist[u] = alt
                heapq.heappush(qu, (alt, u))

    return min([dist[100*z + k] for z in range(n)])


ans = 10**10
for i in range(n):
    if red[100*i]:
        ans = min(ans, dijkstra(100*i, K))

if ans == 10**10:
    print("IMPOSSIBLE")
else:
    print(ans)
        
        
        

