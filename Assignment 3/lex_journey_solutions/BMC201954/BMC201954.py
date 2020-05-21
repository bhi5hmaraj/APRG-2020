nn=input().split()
n1=int(nn[0])
n2=int(nn[1])
adj={}
for i in range(1,n1+1):
  adj[i]=[]
a=input().split()
a1=int(a[0])
a2=int(a[1])
for k in range(n2):
  i=input().split()
  adj[int(i[0])].append([i[1],int(i[2])])
  adj[int(i[2])].append([i[1],int(i[0])])
def bfs (Adj,s,b):
  level = { s: 0 }
  path = {}
  for i in range(1,n1+1):
    path[i]=''
  i = 1
  f = [s]
  while f:
    next = [ ]
    for u in f:
      if u==b:
        a=path[u]
        break
      else:
        for v in Adj [u]:
          if v[1] not in level: 
            level[v[1]] = i
            path[v[1]]=path[u]+v[0]
            #path[u]=''
            next.append(v[1])
          elif v[1]  in level and level[v[1]]==level[u]+1:
            path[v[1]]=min([path[v[1]],path[u]+v[0]])
            #path[u]=[]
      path[u]=''
    f = next
    i += 1
  level={}
  return (a)
d=bfs(adj,a1,a2)
print(d)