from sys import maxsize as inf
from collections import defaultdict


class BusNetwork:
    def __init__(self, n, m):
        self.stops = n
        self.travel_time = [inf for i in range(m)]
        self.routes = defaultdict(list)

    def add_route(self, a, b, t):
        self.routes[a].append((b, t))
        self.routes[b].append((a, t))

    def min_cost_path(self, start, end):
        queue = {start: 0}
        bus = {start: -1}
        dist = [inf for i in range(self.stops)]
        dist[start] = 0
        visited = [False for i in range(self.stops)]

        prev = {start: None, end: None}
        while queue:
            
            curr = min(queue, key=queue.get)
            queue.pop(curr)
            
            visited[curr] = True
            for (a, b) in self.routes[curr]:                     # a - bus stop, b - service provider to that stop
                if not visited[a]:
                    
                    if bus[curr] == b or bus[curr] == -1:
                        if dist[a] > dist[curr] + self.travel_time[b]*abs(a-curr):
                            dist[a] = dist[curr] + self.travel_time[b]*abs(a-curr)
                            queue[a] = dist[a]
                            prev[a] = curr
                            bus[a] = b

                    else:
                        if dist[a] > dist[curr] + 60 + self.travel_time[b]*abs(a-curr):
                            dist[a] = dist[curr] + 60 + self.travel_time[b]*abs(a-curr)
                            queue[a] = dist[a]
                            prev[a] = curr
                            bus[a] = b
                    
                    if a not in queue.keys():
                        queue[a] = dist[a]

        return dist[end]#prev


m, end = map(int, input().split())
graph = BusNetwork(100, m)
graph.travel_time = list(map(int, input().split()))
for i in range(m):
    nbr = list(map(int, input().split()))
    for k in range(len(nbr)):
        for k1 in range(k+1, len(nbr)):
            graph.add_route(nbr[k], nbr[k1], i)

x = graph.min_cost_path(0, end)
if x == inf:
    print("IMPOSSIBLE")
else:
    print(x)
