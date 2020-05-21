from queue import PriorityQueue as pq
N,M = list(map(int, input().split()))
vertex = [[] for i in range(N+1)]

Max = 9999
vrt_c = [Max for _ in range(N+1)]

for i in range(M):
	x,y,w = list(map(int, input().split()))
	vertex[y].append((x,w))
	vertex[x].append((y,w))

def dijkstra(d):
	w = pq()
	w.put((0,d))
	vrt_c[d] = 0
	while not w.empty():
	    	u = w.get()
	    	for x in vertex[u[1]]:
			        if vrt_c[u[1]] + x[1] < vrt_c[x[0]]:
				            vrt_c[x[0]] = vrt_c[u[1]] + x[1]
				            w.put((vrt_c[x[0]],x[0]))

dijkstra(1)
dmn = vrt_c[N]
dist = vrt_c[:]
vrt_c = [Max for _ in range(N+1)]
dijkstra(N)
for u in range(N):
	for v in vertex[u+1] : 
	    x = dist[u+1] + v[1] + vrt_c[v[0]]
	    if Max > x and x > dmn : Max = x

print(Max)
