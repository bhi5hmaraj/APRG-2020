from queue import PriorityQueue
l=list(map(int,input().split()))
m=[1,l[0]+1]
adj=[]
adj_list={}
for i in range (1,l[0]+1):
  adj_list[i]=[]
for i in range (l[1]):
  z=list(map(int,input().split()))
  adj.append([z[0],z[1],z[2]])
  adj_list[z[0]].append((z[1],z[2]))
  adj_list[z[1]].append((z[0],z[2]))    
def spath(adj_list,n):
  q=PriorityQueue()
  q.put((0,n)) 
  dis=[10**20]*(l[0]+1) 
  dis[n]=0
  while not q.empty():
    p=q.get()
    a=p[0]
    b=p[1]
    for i in adj_list[b]:
      c=i[0]
      w=i[1]
      if dis[c]>dis[b]+w:
        dis[c]=dis[b]+w 
        q.put((dis[c],c))
  return dis 
l1=spath(adj_list,1)
ln=spath(adj_list,l[0])
edge=[]
for i in adj:
    a=i[0]
    b=i[1]
    c=i[2]
    edge.append(l1[a]+ln[b]+c)
    edge.append(l1[b]+ln[a]+c)
    edge.append(l1[a]+ln[b]+3*c)
    edge.append(l1[b]+ln[a]+3*c)
p=10**20  
for i in edge:
  if i>ln[1] and i<p:
    p=i
print(p)        
