from queue import PriorityQueue
def short_path(A,s,N):
    cost=[]
    for i in range(0,N):
        cost.append(10**10000)
    Q=PriorityQueue()
    cost[s]=0
    Q.put((0,s))
    while Q.empty()!=True:
        x=Q.get()
        u=x[1]
        for j in A[u]:
            v=j[0]
            k=j[1]
            if cost[v]>cost[u]+k:
                cost[v]=cost[u]+k
                Q.put((cost[v],v))
    return cost   
x=list(map(int,input().split()))
N=x[0]
M=x[1]
A=[]
for i in range(N):
    A.append([])
for i in range(M):
    lines=list(map(int,input().split()))
    A[lines[0]-1].append((lines[1]-1,lines[2]))
    A[lines[1]-1].append((lines[0]-1,lines[2]))   
    
T=[]
q=short_path(A,N-1,N)
p=short_path(A,0,N)
for x in range(0,N):
    if p[x]+q[x]==q[0]:
        for y in A[x]:
            v=y[0]
            w=y[1]
            p3=q[v]
            if p[x]+w+p3!=q[0]:
                T.append(p[x]+w+p3)
print(min(T))            
            
                    
                    
                      
                      
                      
                      
                      
  
                      
                      
                      
