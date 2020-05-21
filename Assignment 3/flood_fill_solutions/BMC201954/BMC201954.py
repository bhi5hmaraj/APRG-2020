r=input().split()
N=int(r[0])
b=int(r[1])
d=input().split()
s=(int(d[0]),int(d[1]))
black={}
for i in range(b):
  d=input().split()
  black[(int(d[0]),int(d[1]))]=1
def f(i,j):
  a=[(i,j)]
  if i-1>0 and (i-1,j)not in black:
    a.append((i-1,j))
  if i+1<N+1 and (i+1,j)not in black:
    a.append((i+1,j))
  if j-1>0 and (i,j-1)not in black:
    a.append((i,j-1))
  if j<N and (i,j+1)not in black:
    a.append((i,j+1))
  return a
#def bfs (Adj,s):
level = { s: 0 }
parent = {s : None }
i = 1
g = [s]
while g:
  next = [ ]
  for u in g:
    for v in f(u[0],u[1]):
      if v not in level: 
        level[v] = i
        parent[v] = u
        next.append(v)
  g = next
  i += 1
#print(level)
n=0
for i in range(1,N+1):
  for j in range(1,N+1):
    if (i,j)not in black and (i,j) not in level:
      n=1
      break
if n==1:
  print('N')
else:
  print('Y')