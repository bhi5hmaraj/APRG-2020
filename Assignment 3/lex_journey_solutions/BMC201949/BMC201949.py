from queue import *
def bfs(A,s,t,n):
    dist=[]
    rank=[]
    for k in range(n):
        dist.append(0)
        rank.append('')
    Mark=[]    
    for j in range(n):
        Mark.append(0)
    Mark[s]=1
    Q=Queue()
    Q.put(s)
    while Q.empty()!=True:
        v=Q.get()
        for j in range(0,len(A[v])):
            if Mark[A[v][j][0]]==0:
                Mark[A[v][j][0]]=1        
                Q.put(A[v][j][0])
                dist[A[v][j][0]]=dist[v]+1 
                rank[A[v][j][0]]=rank[v]+A[v][j][1]
            if rank[A[v][j][0]]>rank[v]+A[v][j][1] and dist[v]+1==dist[A[v][j][0]]:
                    rank[A[v][j][0]]=rank[v]+A[v][j][1]
        if v!=t:
            rank[v]=''
    return rank
x=input().split()
n=int(x[0])
m=int(x[1])
y=input().split()
a=int(y[0])
b=int(y[1])
A=[]
for i in range(n):
    A.append([])
for k in range(0,m):
    z=input().split()
    p1=int(z[0])-1
    p2=int(z[2])-1
    A[p1].append((p2,z[1]))
    A[p2].append((p1,z[1]))
print(bfs(A,a-1,b-1,n)[b-1])              
