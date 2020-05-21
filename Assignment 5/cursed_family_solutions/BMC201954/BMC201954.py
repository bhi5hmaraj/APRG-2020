def bfs (Adj,s):
  level = { s: 0 }
  level1 = {0:[s]}
  i = 1
  f = [s]
  while f:
    next = [ ]
    for u in f:
      for v in Adj [u]:
        if v not in level: 
          level[v] = i
          if i not in level1:
            level1[i]=[v]
          else:
            level1[i].append(v)
          #parent[v] = u
          next.append(v)
    f = next
    i += 1
  return (level1)
n=int(input())
adj={}
par={}
for i in range(n):
    adj[i+1]=[]
    par[i+1]=None
for i in range(n-1):
    a,b=map(int,input().split())
    adj[a].append(b)
    par[b]=a
for i in par:
    if par[i]==None:
        break
root=i
dp={}
q=[]

def gc(i):
    a=[]
    for j in adj[i]:
        for k in adj[j]:
            a.append(k)
    return a
l=bfs(adj,root)
k=len(l)-1
dp={}
q=l[k]
while q:
    for i in q:
        if adj[i]==[]:
            dp[i]=1
        else:
            a=0
            for j in adj[i]:
                a+=dp[j]
            b=1
            for j in gc(i):
                b+=dp[j]
            dp[i]=max([a,b])
    k=k-1
    if k<0:
        q=[]
    else:
        q=l[k]
print(dp[root])