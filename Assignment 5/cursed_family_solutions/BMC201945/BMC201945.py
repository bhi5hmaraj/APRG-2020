n=int(input())
parent={}
child={}
for i in range (1,n+1):
  parent[i]=0
  child[i]=[]
for i in range (n-1):
  x=list(map(int,input().split()))
  parent[x[1]]=x[0]
  child[x[0]].append(x[1]) 
for i in range (1,n+1):
  if parent[i]==0:
    root=i
    break  
ans=[0] *(n+1) 
def f(child,parent,a):
  if not child[a]:
    ans[a]=1
    return 1
  if ans[a] != 0:
    return ans[a]  
  x=0
  y=0
  for u in child[a]:
    x +=f(child,parent,u)
  for u in child[a]:
    for v in child[u]:
      y += f(child,parent,v)
  y=y+1
  ans[a]=max(x,y)
  return ans[a]      
print (f(child,parent,root))  