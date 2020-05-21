from collections import defaultdict

g = defaultdict(list)
       
def add(u,v):
        g[u].append(v)

(N,M)=map(int,input().split())
(X,Y)=map(int,input().split())
K={}
for k in range(M):
    I=input().split()
    add(int(I[0]),int(I[2]))
    add(int(I[2]),int(I[0]))
    K[(int(I[0]),int(I[2]))]=I[1]
    K[(int(I[2]),int(I[0]))]=I[1]
    
    
    
dist={X:0}
prev={X:""}
    
#visited={}
queue=[]

def bfs(g, source, target):
  #visited[source]=1
  queue.append(source)
  
  while queue:
    s = queue.pop(0) 
    if(s==Y):
        break
    
    for neighbour in g[s]:
      if(neighbour not in dist):
        dist[neighbour]=dist[s] +1
        #visited[neighbour]=1
        queue.append(neighbour)
        prev[neighbour]=prev[s] + K[(s,neighbour)]

      elif(neighbour in dist and dist[neighbour]==dist[s]+1):
          prev[neighbour]= min(prev[neighbour], prev[s]+K[(s,neighbour)])
          
    prev[s]=""
    
  print(prev[Y]) 
  
  
'''      alt=dist[s-1] + 1
      if(alt<=dist[neighbour - 1]):
        dist[neighbour-1]=alt   
            
  A={}
  for vertex in prev[target-1]:
      queue.append(vertex)
      A[vertex] = 1
  while queue:
      s=queue.pop(0)
      for node in prev[s-1]:
        if node not in A:
          A[node] = 1
          queue.append(node)      
         
  l=len(A)+1
  print(l)
'''
 
  
bfs(g,X,Y)