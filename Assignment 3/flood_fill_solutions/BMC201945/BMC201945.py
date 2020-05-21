def adj_list(x,y,N,b):
  l=[(x,y)]
  if x>=2 and (x-1,y) not in b:
    l.append((x-1,y))
  if x<=(N-1) and (x+1,y) not in b:
    l.append((x+1,y))
  if y>=2 and (x,y-1) not in b:
    l.append((x,y-1))
  if y<=N-1 and (x,y+1) not in b:
    l.append((x,y+1))
  return l
def bfs(v,N,b):
  q=[v]
  l={}
  l[v]=0
  a=1
  while q:
    s=[]
    for i in q:
      for j in adj_list(i[0],i[1],N,b):
        if j not in l:
          l[j]=a
          s.append(j)
    q=s
    a +=1      
  return l     
l=list(map(int,input().split()))
N=l[0]
B=l[1]
m=list(map(int,input().split()))
w=(m[0],m[1])
b={}
for i in range(B):
  s=input().split()
  b[(int(s[0]),int(s[1]))]=False 
p=bfs(w,N,b) 
z=True
for i in range(N):
  for j in range(N):
    if (i+1,j+1) not in b and (i+1,j+1) not in p:
      z=False
      break
if z==False:
  print ('N')
else:
  print ('Y')           