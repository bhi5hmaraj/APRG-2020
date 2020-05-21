
a=list(input().split())
n=int(a[0])
m=int(a[1])
b=list(input().split())
x=int(b[0])
y=int(b[1])
adjancy={}
for i in range(1,n+1):
  adjancy[i]=[]
for i in range(m):
  a=input().split()
  u=int(a[0])
  ch=a[1]
  v=int(a[2])
  adjancy[u].append([v,ch])
  adjancy[v].append([u,ch])            
#now starts the bfs
def BFS(adjancy,x,y):
  track=[0]*(n+1)  
  lev={x:0}
  start=[x]
  track[x]=1
  pathque={}
  for i in range (1,n+1):
    pathque[i]=''
  while len(start) !=0:
    tempath=start.pop(0)
    if tempath==y:
      break
    else:
      for i  in adjancy[tempath]:
        b=i[0]
        c=i[1]
        if track[b]==0:
          lev[b]=lev[tempath]+1
          track[b]=1
          pathque[b]=pathque[tempath]+c
          start.append(b)
        elif track[b]==1 and lev[b]==lev[tempath]+1:
          pathque[b]=min(pathque[b],pathque[tempath]+c)
      pathque[tempath]=''  
  return pathque[y]
s=BFS(adjancy,x,y)  
print(s)
