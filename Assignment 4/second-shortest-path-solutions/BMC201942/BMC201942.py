from sys import maxsize as inf
from collections import defaultdict


class Graph:
    def __init__(self, n):
        self.vertices = n
        self.adj = defaultdict(list)

    def add_edge(self, a, b, w):
        self.adj[a].append((b, w))
        self.adj[b].append((a, w))

    def sec_shortest_path(self, start, end):
        cost = defaultdict(lambda: (inf, inf))
        cost[start] = (0, inf)
        queue = {start: (0, inf)}
        # cost[end] = inf
        visited = [False for i in range(self.vertices)]
        # prev = {start: None, end: None}
        while queue:

            curr = min(queue, key=queue.get)
            '''if curr == end:
                return sec_dist[end]'''
            mincost = queue.pop(curr)

            # visited[curr] = True
            for (a, w) in self.adj[curr]:

                if cost[a][0] > mincost[0] + w:
                    cost[a] = (mincost[0] + w, cost[a][0])
                    # if not visited[a]:
                    queue[a] = cost[a]

                elif cost[a][1] > mincost[0] + w > cost[a][0]:
                    cost[a] = (cost[a][0], mincost[0] + w)
                    queue[a] = cost[a]

                '''elif cost[a][1] > mincost[1] + w > cost[a][0]:
                    cost[a] = (cost[a][0], mincost[1] + w)
                    queue[a] = cost[a]'''
        dist = {}
        for a in range(self.vertices):
            dist[a] = cost[a][1]
        for i in range(n):
            curr = min(dist, key=dist.get)
            mincost = dist.pop(curr)
            for (a, w) in self.adj[curr]:
                if cost[a][1] > mincost + w > cost[a][0]:
                    cost[a] = (cost[a][0], mincost + w)

        return cost[end][1]

n, m = map(int, input().split())
graph = Graph(n)
for i in range(m):
    a, b, w = map(int, input().split())
    graph.add_edge(a-1, b-1, w)
print(graph.sec_shortest_path(0, n-1))
