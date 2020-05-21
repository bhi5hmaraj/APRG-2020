(N, b)=map(int,input().split())
(i,j)=map(int,input().split())
A={}
for k in range(b):
    (m,n)=map(int,input().split())
    A[(m,n)]=1

from collections import defaultdict 
  
graph= defaultdict(list)   
graph={}

v = [] 
queue = []     

def bfs(v, graph, node):
  v.append(node)
  queue.append(node)
  s1=[]
  while queue:
    s = queue.pop(0) 
    s1.append(s) 
    def add(x,y): 
        graph[(x,y)]=1
  
        if( (x+1)<=N and (x+1,y) not in A and (x+1,y) not in graph):
            graph[(x+1,y)]=1
            queue.append((x+1,y))
    
        if( (y+1)<=N and (x,y+1) not in A and (x,y+1) not in graph):
            graph[(x,y+1)]=1
            queue.append((x,y+1))
    
        if( (y-1)>=1 and (x,y-1) not in A and (x,y-1) not in graph):
            graph[(x,y-1)]=1
            queue.append((x,y-1))

        if( (x-1)>=1 and (x-1,y) not in A and (x-1,y) not in graph):
            graph[(x-1,y)]=1
            queue.append((x-1,y))
    
    add(s[0],s[1])
        
  l=len(s1)
  if(l+len(A)==(N*N)):
      print("Y")
  else:
      print("N")

bfs(v, graph, (i,j))