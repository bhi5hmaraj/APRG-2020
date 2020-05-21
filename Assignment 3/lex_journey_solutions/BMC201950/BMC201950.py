from collections import defaultdict
class Graph:
   
    def __init__(self):
        self.graph = defaultdict(list)
       
    def addEdge(self,u,v):
        self.graph[u].append(v)
       
    def BFS(self, s, N, Y,B):
        P={s:""}
        W={s:0}
        
        queue=[]
        queue.append(s)
       
        
        while(queue):
            s = queue.pop(0)
            if(s==Y):
                break
            for i in self.graph[s]:
                if i not in W:
                    W[i]=W[s]+1
                    queue.append(i)
                    P[i]=P[s]+B[(s,i)]
                    
                elif i in W and (W[i]==W[s]+1):
                    P[i]=min([P[i],P[s]+B[(s,i)]])
            P[s]=""
        return P[Y]
    
    
G=Graph()
p,q = map(int,input().split())
x,y = map(int,input().split())
list = {}

for i in range(q):
    edges =input().split()
    G.addEdge((int)(edges[0])-1,(int)(edges[2])-1)
    G.addEdge((int)(edges[2])-1,(int)(edges[0])-1)
    list[((int)(edges[2])-1,(int)(edges[0])-1)] = edges[1]
    list[((int)(edges[0])-1,(int)(edges[2])-1)] = edges[1]
   

s = G.BFS(x-1,p,y-1,list)
print(s)

