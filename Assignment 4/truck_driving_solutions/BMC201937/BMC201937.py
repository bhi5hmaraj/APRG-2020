from array import *
from queue import PriorityQueue

class PathHead:
    def __init__(self, town, tanksize):
        self.tanksize = tanksize
        self.town = town
        
        
    def __lt__(self, other):
        if(self.tanksize < other.tanksize): 
            return True
        else: 
            return False
        

class Graph:
    
    def __init__(self,nov):
        self.N = nov
        self.roads_from_town = [[(0,0) for i in range(nov)] for j in range(nov)]
        self.Q = PriorityQueue()
        self.town_visited = [0]*nov    
                  
    def addEdge(self,u,v,w):
        self.roads_from_town[u].append((v, w));
        self.roads_from_town[v].append((u, w)); 
       
    def cleanup(self):
        self.Q = {}
        self.town_visited = {}
        self.Q = PriorityQueue()
        self.town_visited = [0]*self.N

    def findTankSize(self,src,dest):
        #PathHead head(0,0)
        self.Q.put(PathHead(src, 0))
        while not self.Q.empty():
            head = self.Q.get()
            if head.town == dest :
                break
            self.town_visited[head.town] = 1
            l = self.roads_from_town[head.town]
            for iter1 in range(len(l)):
                i,j = l[iter1]
                if(self.town_visited[i] == 0):
                    #PathHead push_head = PathHead(i(0), max(i(1), head.tanksize))
                    self.Q.put(PathHead(i, max(j, head.tanksize)))
                           
        return head.tanksize
     
n,m = map(int,input().split())

G = Graph(n)
for i in range(m):
    u,v,w = map(int,input().split())
    G.addEdge(u-1,v-1,w)
Qry = int(input())
for i in range(Qry):
    x,y = map(int,input().split())
    ts = G.findTankSize(x-1,y-1)
    print(str(ts))
    G.cleanup()

  
