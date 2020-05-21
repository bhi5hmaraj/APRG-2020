from queue import PriorityQueue
def djkistra(A,s):
    cost={}
    for i in range(0,100):
        for j in range(1,N+1):
             cost[(i,j)]=10**1000
    Q=PriorityQueue()
    cost[s]=0
    Q.put((0,s))
    while Q.empty()==False:
        x=Q.get()
        u=x[1]
        for j in A[u]:
            w=j[0]
            k=j[1]
            if cost[w]>cost[u]+k:
                cost[w]=cost[u]+k
                Q.put((cost[w],w))    
    return cost
in1=list(map(int,input().split()))
N=in1[0]
k=in1[1]
T=list(map(int,input().split()))
X={}
A={}
for z in range(0,100):
    for w in range(1,N+1):
        A[(z,w)]=[]
for i in range(1,N+1):
    lines=list(map(int,input().split()))
    X[i]=lines
for j in range(1,N+1):
    t=len(X[j])
    for i in range(0,t-1):
        a=X[j][i]
        b=X[j][i+1]
        c=(b-a)*T[j-1]
        A[(a,j)].append(((b,j),c))
        A[(b,j)].append(((a,j),c))
for a in range(0,100):
    for i in range(1,N+1):
        for j in range(1,N+1):
            A[(a,i)].append(((a,j),60))
            A[(a,j)].append(((a,i),60))
Answer=[]  
chc=10**1000
for i in range(1,N+1):
    H=djkistra(A,(0,i))
    temp=H[(k,1)]
    for j in range(1,N+1):
        if temp>=H[k,j]:
            temp=H[k,j]
    if chc>=temp:
        chc=temp
if chc==10**1000:
    print("IMPOSSIBLE")
else:
    print(chc)
            
        
            
            
        

    
    



