from collections import defaultdict
class Graph:
   
    def __init__(self):
        self.graph = defaultdict(list)
       
    def addEdge(self,u,v):
        self.graph[u].append(v)
       
    def BFS(self, s, N, Y,B):
        P={s:""}
        W={s:0}
        #visited = [False] * N
        queue=[]
        queue.append(s)
       
        #visited[s] = True
        while(queue):
            s = queue.pop(0)
            if(s==Y):
                break
            for i in self.graph[s]:
                if i not in W:
                    W[i]=W[s]+1
                    queue.append(i)
                    P[i]=P[s]+B[(s,i)]
                    #visited[i] = True
                elif i in W and (W[i]==W[s]+1):
                    P[i]=min([P[i],P[s]+B[(s,i)]])
            P[s]=""
        return P[Y]
g=Graph()
N,M = map(int,input().split())
X,Y = map(int,input().split())
B = {}
for i in range(M):
    e =input().split()
    g.addEdge((int)(e[0])-1,(int)(e[2])-1)
    g.addEdge((int)(e[2])-1,(int)(e[0])-1)
    B[((int)(e[2])-1,(int)(e[0])-1)] = e[1]
    B[((int)(e[0])-1,(int)(e[2])-1)] = e[1]
   

K = g.BFS(X-1,N,Y-1,B)
print(K)
