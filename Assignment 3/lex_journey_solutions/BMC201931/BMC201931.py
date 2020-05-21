from queue import Queue
n,m = list(map(int,input().split()))
x,y = list(map(int,input().split()))

x=x-1
y=y-1
lol=[]
lol0={}
for i in range(0,n):
    lol.append([])

for z in range(0,m):
    i,r,j=input().split()
    i=int(i)-1
    j=int(j)-1
   
    lol[i].append(j)
    lol[j].append(i)
    lol0[(i,j)]=r
    lol0[(j,i)]=r


def f(u,grp):
    n = len(grp)
    q=Queue()
    q.put(u)
    distence=[-1]*n
    distence[u]=0
    while not q.empty():
        v=q.get()
       
        for w in grp[v]:
            if distence[w]==-1:
                distence[w]=distence[v]+1
                q.put(w)
    return distence

def f0(x,y,lol):
    n=len(lol)
    worthy=[0]*n
    distence = list(map(lambda x,y: x + y,f(x,lol),f(y,lol)))
    slen = distence[x]
    for v in range(0,n):
        if distence[v]==slen:
            worthy[v]=1

    for i in range(0,n):
        if worthy[i]!=1:
            lol[i]=[]
       
        l=[]
        for v in lol[i]:
            if worthy[v]==1:
                l.append(v)
        lol[i]=l
    return

def f1(x,y,lol,lol0):
    f0(x,y,lol)
    distence=f(x,lol)
    s=[x]
    n=max(distence)
    a=""
    for i in range(0,n):
        arr=s
        m='z'
        curlev=distence[arr[0]]
        for u in arr:
            for v in lol[u]:
                if distence[v]==curlev+1:
                    m=min(m,lol0[(u,v)])
        out=set()
        for u in arr:
            for v in lol[u]:
                if lol0[(u,v)] == m and distence[v] == curlev+1:
                    out.add(v)
        out=list(out)
        s=out
        a=a+m
   
    return a


print(f1(x,y,lol,lol0))
   