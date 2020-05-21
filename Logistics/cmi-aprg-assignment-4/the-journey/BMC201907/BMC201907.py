from collections import defaultdict 

num_buses, destination = map(int, input().split())     
time_list = list(map(int, input().split()))   
consec_list = []

for i in range(num_buses):
    consec_list.append(list(map(int, input().split())))

class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = defaultdict(list)
        self.weights = {}

    def addNode(self, value):
        self.vertices.add(value)

    def addEdge(self, node, neighbour, weight):
        self.edges[node].append(neighbour)
        self.edges[neighbour].append(node)
        self.weights[(node, neighbour)] = weight
        self.weights[(neighbour, node)] = weight


def dijsktra(graph, initial):
  visited = {initial: 0}
  path = {}

  list_vert = set(graph.vertices)

  while list_vert: 
    min_node = None
    for node in list_vert:
      if node in visited:
        if min_node is None:
          min_node = node
        elif visited[node] < visited[min_node]:
          min_node = node

    if min_node is None:
      break

    list_vert.remove(min_node)
    current_weight = visited[min_node]

    for edge in graph.edges[min_node]:
      weight = current_weight + graph.weights[(min_node, edge)]
      if edge not in visited or weight < visited[edge]:
        visited[edge] = weight
        path[edge] = min_node

  return visited, path
  
def intersection(list1, list2): 
    return([x for x in list1 if x in list2])

myGraph = Graph()
    
myGraph.addNode("start")
myGraph.addNode("finish")

for bus in range(num_buses):    
    for stop in consec_list[bus]:  
        myGraph.addNode((bus, stop))  
        
for bus in range(num_buses):
    for i in range(len(consec_list[bus])):
        for j in range(i + 1, len(consec_list[bus])):
            myGraph.addEdge((bus, consec_list[bus][i]), (bus, consec_list[bus][j]), time_list[bus]*(consec_list[bus][j] - consec_list[bus][i]))  

for bus1 in range(num_buses):
    for bus2 in range(bus1 + 1, num_buses):
        for stop in intersection(consec_list[bus1],consec_list[bus2]):
            myGraph.addEdge((bus1, stop), (bus2, stop), 60)
            
for bus in range(num_buses):
    myGraph.addEdge("start", (bus, 0), 0)
    myGraph.addEdge("finish", (bus, destination), 0)

final_tup = dijsktra(myGraph,"start")
visited = final_tup[0]
path = final_tup[1]

try:
    if (path.get(0, destination) != (0, 0)):
        print(visited[(0, destination)])

except:
    print("IMPOSSIBLE")
