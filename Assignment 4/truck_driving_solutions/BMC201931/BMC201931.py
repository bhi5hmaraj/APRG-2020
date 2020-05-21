import math

n,m=map(int, input().split())
gr=[]
gr0=[]
for i in range(m):
  gr.append(list(map(int,input().split())))
  gr0.append([gr[i][0],gr[i][1]])
g=int(input())




def printpath(s, d, visited, graph, path, sum0, lol):
  visited.append(s)
  path.append(s)
  if s==d:
    lol.append(max(sum0))
  else:
    for i in range(n+1):
      if [s,i] in graph and i not in visited:
        sum0.append(gr[graph.index([s,i])][2])
        printpath(i, d, visited, graph, path, sum0, lol)
      else:
        continue
  sum0.pop()
  path.pop()
  visited.pop()
  return lol

for i in range(g):
  o,p=map(int, input().split()) 
  visited=[]
  path=[]
  sum0=[0]
  lol=[]
  if o <=p:
    printpath(o,p,visited,gr0, path, sum0,lol)
    print(min(lol))
  else:
    min(printpath(p,o,visited,gr0, path, sum0,lol))
    print(min(lol))
  


