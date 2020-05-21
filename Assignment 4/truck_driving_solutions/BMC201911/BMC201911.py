from queue import PriorityQueue
N,M=map(int,input().split())
l=PriorityQueue()
for i in range(M):
    m1,m2,m3=map(int,input().split())
    l.put((m3,m1-1,m2-1))
q=int(input())
m=[]
for i in range (q):
    x=list(map(int,input().split()))
    m.append((x[0]-1,x[1]-1))
def root(x,l):
    if l[x]==x:
        return x
    else:
        return root(l[x],l)
def merge(x,y,l,r):
    if r[x]>r[y]:
        l[y]=x
    elif r[x]<r[y]:
        l[x]=y
    else:
        l[y]=x
        r[x] +=1
mintree={}
weight={}
edge=0
p=[]
r=[]
for i in range (N):
    p.append(i)
    r.append(0)
    mintree[i]=[]
while edge<N-1:
    w,u,v=l.get()
    u1=root(u,p)
    v1=root(v,p)
    if u1 !=v1:
        edge +=1
        mintree[u].append(v)
        mintree[v].append(u)
        weight[(u,v)]=w
        weight[(v,u)]=w
        merge(u1,v1,p,r)
def f(a,b):
    explored=[0]*N
    l=[0]*N
    explored[a]=1
    q=[a]
    while q:
        p=q.pop(0)
        for v in mintree[p]:
            if explored[v]==0:
                explored[v]=1
                l[v]=max(l[p],weight[(p,v)])
                q.append(v)
    return l[b]
for i in range (len(m)):
    print(f(m[i][0],m[i][1]))
#print(mintree)
#print(weight)
        
        
    