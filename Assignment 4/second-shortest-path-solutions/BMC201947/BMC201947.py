import sys

from collections import defaultdict 
  
class Graph: 
    #defining graph
    def __init__(self): 
        self.graph = defaultdict(list) 
    
    #adding undirected edges in the graph
    def addEdge(self, u, v): 
        self.graph[u].append(v)
    
    #deleting edge from the graph
    def delEdge(self, u, v):
        flag=0
        for i in range(len(self.graph[u])): 
            if flag ==1: 
                self.graph[u][i-1]=self.graph[u][i]
            if (self.graph[u][i]==v): 
                flag=1
        self.graph[u].pop(-1)
    
    #for the shortest path
    def shortestPath(self, source, sink, n): 
        dist = [sys.maxsize] * n 
        #L = [[] for i in range(n)]
        dist[source] = 0
        visited = {}
        queue=[]
        heap={}
        heap[source]=1
        l = []
        for i in range(n):
            l.append([])
        for cout in range(n): 
            node = self.minDistance(dist, heap)
            # if the minimum distance is the max system value
            if(node==-1):
                return (0,[0])
                break
            visited[node] = 1
            heap.pop(node)
            if(node==sink):
                #if the pointer is at destination then break 
                break
            for i in self.graph[node]:
                #going over each node
                if i not in visited:
                    for j in range(len(Sum[(i,node)])):
                        #checking for the path with least distance
                        if(dist[i]>dist[node] + Sum[(i,node)][j]):
                            heap[i]=1
                            dist[i] = dist[node] + Sum[(i,node)][j]
                            l[i].append(node)
        c=1
        #c will work as a counter
        heap=sink
        queue.append(sink)
        queue.append(l[sink][-1])
        while(l[heap][-1]!=source):
            heap=queue[c]
            c = c+1
            queue.append(l[heap][-1])
        #print(dist[sink],queue)           
        return (dist[sink],queue)
    
    #to find the least distance of the graph
    def minDistance(self, dist, heap):
        #assign min to the maximum possible value of the system
        min = sys.maxsize
        c=0
        #in case min is indeed the minimum value
        min_index = -1
        for node in heap: 
            if dist[node]<min:
                c=1
                min = dist[node] 
                min_index = node
        #if(c==1):
        return min_index 
        #else:
        #    return -1
    
    # for the second shortest path
    def secondShortest(self,n):
        #assign min to the maximum possible value of the system
        min=sys.maxsize
        (a,b) = self.shortestPath(0,n-1,n)
        for i in range(len(b)-1):
            for i1 in self.graph[b[i+1]]:
                for i2 in range(len(Sum[(i1,b[i+1])])):
                    min2 = a + (2*Sum[i1,b[i+1]][i2])
                    if min2 < min:
                        #assign new min
                        min = min2
            #if the edge is independent of others
            if(len(Sum[(b[i],b[i+1])])==1):
                #delete the edge
                self.delEdge(b[i+1],b[i])
                self.delEdge(b[i],b[i+1])
                a1,b1=self.shortestPath(0,n-1,n)
                if(a1==a):
                    ptr = self.secondShortest(n)
                    if(ptr<min):
                        min=ptr
                #add back those deleted edges
                self.addEdge(b[i+1],b[i])
                self.addEdge(b[i],b[i+1])
            else:
                #assign min to the maximum possible value of the system
                min1=sys.maxsize
                marker=0
                for j in range(len(Sum[(b[i],b[i+1])])):
                    if Sum[(b[i],b[i+1])][j] < min1 :
                        min1 = Sum[(b[i],b[i+1])][j]
                        #mark the position
                        marker=j
                Sum[(b[i],b[i+1])].pop(marker)
                a1,b1 = self.shortestPath(0,n-1,n)
                if(a1==a):
                    ptr = self.secondShortest(n)
                    if(ptr<min):
                        min=ptr
                Sum[(b[i],b[i+1])].append(min1)
                
            if(a1==0):
                continue
            if min==a+1 :
                break
            elif a1>a and a1<min :
                min = a1
            
        return min


g = Graph()
N,M = map(int,input().split())

Sum={}
for i in range(M):
    u,v,w = map(int,input().split())
    g.addEdge(u-1,v-1)
    g.addEdge(v-1,u-1)
    if (u-1,v-1) not in Sum:
        Sum[(u-1,v-1)]=[w]
        Sum[(v-1,u-1)]=[w]
    else:
        Sum[(u-1,v-1)].append(w)
        Sum[(v-1,u-1)].append(w)

gg = g.secondShortest(N)
#print(g.secondShortest(N))
print(gg)






