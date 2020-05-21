l=list(map(int,input().split()))
l1=l[0]
l2=l[1]
m=list(map(int,input().split()))
a=m[0]
b=m[1]
adj_list={}
for i in range(l1):
  adj_list[i+1]={}
for i in range (l2):
  x=input().split()
  adj_list[int(x[0])][int(x[2])]=x[1]
  adj_list[int(x[2])][int(x[0])]=x[1]
def bfs(adj_list,a,b):
  e=[False]*(l1+1)
  dis=[0]*(l1+1)
  q=[a]
  e[a]=True 
  path={}
  for i in range (1,l1+1):
    path[i]=''
  while q:
    p=q.pop(0)
    if p==b:
      break
    else:
      for i in adj_list[p]:
        y=adj_list[p][i]
        if e[i]==False:
          dis[i]=dis[p]+1
          e[i]=True
          path[i]=path[p]+y
          q.append(i)
        elif e[i]==True and dis[i]==dis[p]+1:
          path[i]=min([path[i],path[p]+y]) 
    path[p]=''    
  return path[b]
print(bfs(adj_list,a,b))        