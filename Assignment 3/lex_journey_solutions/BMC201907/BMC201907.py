from collections import defaultdict

num_vert, num_edges = map(int, input().split())
start, finish = map(int, list(input().split()))
road_matrix = {}

class Graph:
   
    def __init__(self):
        self.graph = defaultdict(list)
       
    def add_edge(self, node, neighbour):
        self.graph[node].append(neighbour)
        self.graph[neighbour].append(node) #Since undirected
       
    def lexi_BFS(self, start, finish, road_matrix):
        path = {start: ""}
        visited = {start: 0}
        queue = []
        queue.append(start)
        
        while(queue):
            start = queue.pop(0)
            if (start == finish):
                break
            for i in self.graph[start]:
                if i not in visited:
                    visited[i] = visited[start] + 1
                    queue.append(i)
                    path[i] = path[start] + road_matrix[(start, i)]
                elif (i in visited) and (visited[i] == visited[start] + 1):
                    path[i] = min([path[i], path[start] + road_matrix[(start, i)]])
            path[start] = ""
        return path[finish]
    
myGraph = Graph()

for i in range(num_edges):
    raw_ver_i, road, raw_ver_j = input().split()
    ver_i, ver_j = int(raw_ver_i), int(raw_ver_j)
    myGraph.add_edge(ver_i - 1, ver_j - 1)
    road_matrix[(ver_i - 1, ver_j - 1)] = road
    road_matrix[(ver_j - 1, ver_i - 1)] = road

print(myGraph.lexi_BFS(start - 1, finish - 1, road_matrix))

