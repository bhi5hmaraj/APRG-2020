from collections import defaultdict
def distancee(start,b,mark):
    b[start]=0
    mark[start]=1
    q=[start]
    while(q!=[]):
        s=q.pop(0)
        for i in graph[s]:
            if mark[i]==1:
                continue
            else:
                b[i]=b[s]+1
                mark[i]=1
                q.append(i)
    
N,M=map(int,input().split())
graph=defaultdict(list)
d=defaultdict(int)
x=defaultdict(int)
t=defaultdict(lambda:"")
mark1=defaultdict(int)
mark2=defaultdict(int)
X,Y=map(int,input().split())
m=[]
p1=""
d1=""
dict=defaultdict(int)
for i in range(M):
    p,a,q=input().split()
    graph[int(p)].append(int(q))
    graph[int(q)].append(int(p))
    t[(int(p),int(q))]=a
    t[(int(q),int(p))]=a
distancee(X,d,mark1)
distancee(Y,x,mark2)
for i in range(N+1):
    if x[i]+d[i]!=d[Y]:
        for j in graph[i]:
            graph[j].remove(i)
        graph[i]=[]
current=X
dict[current]=1
while(True):
    d1=""
    if Y in graph[current]:
        p1=p1+t[(current,Y)]
        break
    for j in graph[current]:
        if (dict[j]!=1):
            if(d1=="" or d1>t[(current,j)]):
                d1=t[(current,j)]
                curr=j
                dict[j]=1
    p1=p1+d1
    current=curr
print(p1)
