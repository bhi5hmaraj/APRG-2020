from collections import defaultdict 

class Graph:
     def __init__(self):
          self.nodes = set()
          self.edges = defaultdict(list)
          self.distances = {}

     def add_node(self, value):
          self.nodes.add(value)

     def add_edge(self, from_node, to_node, distance):
          self.edges[from_node].append(to_node)
          self.edges[to_node].append(from_node)
          self.distances[(from_node, to_node)] = distance
          self.distances[(to_node, from_node)] = distance

def dijkstra(graph, initial):
     visited = {initial: 0}
     path = {}

     nodes = set(graph.nodes)

     while nodes: 
          min_node = None
          for node in nodes:
               if node in visited:
                    if min_node is None:
                         min_node = node
                    elif visited[node] < visited[min_node]:
                         min_node = node

          if min_node is None:
               break

          nodes.remove(min_node)
          current_weight = visited[min_node]

          for edge in graph.edges[min_node]:
               weight = current_weight + graph.distances[(min_node, edge)]
               if edge not in visited or weight < visited[edge]:
                    visited[edge] = weight
                    path[edge] = min_node
     try:
          return visited[(0,k)]
     except KeyError:
          return "IMPOSSIBLE"
  
def intrsct(L1, L2): 
     L3 = [value for value in L1 if value in L2] 
     return L3
  
N,k = map(int, input().split())     
T = list(map(int, input().split()))     
G = Graph()
l = []
for b in range(N):
     l.append(list(map(int, input().split())))   
G.add_node("start")
G.add_node("finish")
for b in range(N):    
     for s in l[b]:  
          G.add_node((b,s))      
for b in range(N):
     for i in range(len(l[b])):
          for j in range(i+1,len(l[b])):
               G.add_edge((b,l[b][i]),(b,l[b][j]),T[b]*(l[b][j]-l[b][i]))  
for b1 in range(N):
     for b2 in range(b1+1,N):
          for s in intrsct(l[b1],l[b2]):
               G.add_edge((b1,s),(b2,s),60) 
for b in range(N):
     G.add_edge("start",(b,0),0)
     G.add_edge("finish",(b,k),0)

print(dijkstra(G,"start"))
            
