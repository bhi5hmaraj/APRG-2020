from collections import defaultdict
class my_gr:
   
    def bfs(self, a, b, c, B):
          dict1 = {}
          dict1[a] = ""
          dict2 = {}
          dict2[a] = 0
        
          queue=[]
          queue.append(a)
       
        
          while(queue):
               a = queue.pop(0)
               if(a==c):
                    break
               for i in self.gr[a]:
                        if i not in dict2:
                                    dict2[i]=dict2[a]+1
                                    queue.append(i)
                                    dict1[i]=dict1[a]+B[(a,i)]
                    
                        elif i in dict2 and (dict2[i]==dict2[a]+1):
                                dict1[i]=min([dict1[i],dict1[a]+B[(a,i)]])
               dict1[a]=""
          return dict1[c]
        
    def __init__(self):
        self.gr = defaultdict(list)
       
    def addEdge(self,u,v):
        self.gr[u].append(v)
            
        
     
gr = my_gr()
b,M = map(int,input().split())
X,c = map(int,input().split())
d = {}
for i in range(M):
    e =input().split()
    gr.addEdge((int)(e[0])-1,(int)(e[2])-1)
    gr.addEdge((int)(e[2])-1,(int)(e[0])-1)
    d[((int)(e[2])-1,(int)(e[0])-1)] = e[1]
    d[((int)(e[0])-1,(int)(e[2])-1)] = e[1]
   

flights = gr.bfs(X-1,b,c-1,d)
print(flights)
