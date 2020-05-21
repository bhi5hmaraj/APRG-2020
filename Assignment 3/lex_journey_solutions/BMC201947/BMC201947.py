from collections import defaultdict

class Graph:
    
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
        
    def BFS(self, src, n, Y, Roads):
        Dist = {src : 0}
        Path = {src:""}
        queue=[]
        queue.append(src) 
        while(queue):
            src = queue.pop(0)
            #if the starting position is the destination
            if(src==Y):
                break
            for i in self.graph[src]: 
                #checking for better paths
                if i not in Dist :
                    Dist[i]=Dist[src]+1
                    queue.append(i) 
                    Path[i] = Path[src] + Roads[(src,i)]
                #if there are multiple shortest paths
                elif (Dist[i]==Dist[src]+1) and i in Dist :
                    # take the path with minimum weight
                    Path[i] = min(Path[i],Path[src]+Roads[(src,i)])
            Path[src] = ""
        return Path[Y]

g=Graph()
Roads = {}
N1,M1 = input().split()
N = int(N1)
M = int(M1)
X1,Y1 = input().split()
X = int(X1)
Y = int(Y1)
for i in range(M):
    weight = input().split()
    #adding both directional edges
    g.addEdge((int)(weight[0])-1,(int)(weight[2])-1)
    g.addEdge((int)(weight[2])-1,(int)(weight[0])-1)
    Roads[((int)(weight[0])-1,(int)(weight[2])-1)] = weight[1]
    Roads[((int)(weight[2])-1,(int)(weight[0])-1)] = weight[1]

Road = g.BFS(X-1,N,Y-1,Roads)
print(Road)
