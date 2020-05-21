from queue import PriorityQueue
l=list(map(int,input().split()))
a=l[0]
b=l[1]
N=a
M=b
z=[]
adj_list={}
for i in range (1,l[0]+1):
  adj_list[i]=[]
for i in range (l[1]):
  x=list(map(int,input().split()))
  z.append((x[2],x[0],x[1]))
x=[]

def findset(x,set1):
  if set1[x]==x:
    return x
  else:
    return findset(set1[x],set1)
def unionset(set1,rank,x1,y1):
   if rank[x1]<rank[y1]:
     set1[x1]=y1
   elif rank[x1]>rank[y1]:
     set1[y1]=x1 
   else:
     set1[y1]=x1
     rank[x1]+=1
   return (set1,rank)  
def mst(z):
  e=0
  parent=[]
  rank=[]
  q=PriorityQueue()
  for i in z:
    q.put(i)
  for i in range (l[0]+1):
    parent.append(i)
    rank.append(1)  
  while e<l[0]-1:
    p=q.get()
    w=p[0]
    u=p[1]
    v=p[2]
    x=findset(u,parent)
    y=findset(v,parent)
    if x != y:
      e=e+1
      adj_list[u].append((v,w))
      adj_list[v].append((u,w))
      unionset(parent,rank,x,y)
  return (adj_list)   
a=mst(z)
adj={}
for i in range(N):
    adj[i+1]=[]
path={1:0}
parent={1:0}
level={1:0}
q=[1]
while q:
    u=q.pop(0)
    for j in a[u]:
        if j[0] not in level:
            level[j[0]]=level[u]+1
            parent[j[0]]=u
            path[j[0]]=j[1]
            q.append(j[0])
            adj[u].append(j[0])
anc=[]
wgt=[]
for i in range(N):
    a=[]
    for j in range(20):
        a.append(0)
    anc.append(a)
for i in range(N):
    b=[]
    for j in range(20):
        b.append(0)
    wgt.append(b)
for i in range(1,len(anc)):
    anc[i][0]=parent[i+1]
    wgt[i][0]=path[i+1]
q=[1]
while q:
    u=q.pop(0)
    for v in adj[u]:
        i=v
        for j in range(2,21):
            anc[i-1][j-1]=anc[anc[i-1][j-2]-1][j-2]
            wgt[i-1][j-1]=max([wgt[anc[i-1][j-2]-1][j-2],wgt[i-1][j-2]])
        q.append(i)
q=[1]

parent=[]
def find_change(l,a,c,d):
    i=0
    while l[i]!=a[i]:
        i+=1
    return max([c[i],d[i]])
q=int(input())
for i in range(q):
    x,y=map(int,input().split())
    if level[x]>=level[y]:
        a=x
        b=y
    else:
        a=y
        b=x
    t=level[a]-level[b]
    r=0
    if t!=0:
        m=bin(t)
        r=0
        for i in range(0,len(m)-2):
            if int(m[i+2])==1:
                r=max([r,wgt[a-1][len(m)-3-i]])
                a=anc[a-1][len(m)-3-i]
    if  a==b:
        print(r)
    else:
        print(max([r,find_change(anc[a-1],anc[b-1],wgt[a-1],wgt[b-1])]))