from queue import PriorityQueue
s=10**14

X,Y=map(int,input().split())
z=list(map(int,input().split()))
l={}


for i in range(100):
    for j in range(X):
        l[(j+1,i)]=[]
for i in range(1,X+1):
  d=list(map(int,input().split()))
  for j in range(len(d)):
    if j >0:
      l[(i,d[j])].append((i,d[j-1]))
    if j<len(d)-1:
      l[(i,d[j])].append((i,d[j+1]))
    
    
    
def lmao(x):
    m={}
    q=PriorityQueue()
    for i in range(100):
        for j in range(X):
            if i==x:
                q.put((0,j+1,i))
                m[(j+1,i)]=0
            else:
                
                m[(j+1,i)]=s
    parent={x:None}
    while not q.empty():
        d,e,f=q.get()
        for i in l[(e,f)]:
            b=abs(f-i[1])*z[e-1]+d
            if b<m[i]:
                m[i]=b
                q.put((m[i],i[0],i[1]))
        for i in range(X):
            if e==i+1:
                b=d
            else:
                b=d+60
            if b<m[(i+1,f)]:
                m[(i+1,f)]=b
                q.put((m[(i+1,f)],i+1,f))
    return(m)




d=lmao(0)
p=[]
for i in range(X):
    p.append(d[(i+1,Y)])
c=min(p)
if c==s:
    print('IMPOSSIBLE')
else:
    print(c)
