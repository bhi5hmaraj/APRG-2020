from queue import PriorityQueue
a=list(input().split())
n=int(a[0])
m=int(a[1])
adjancy=dict()
b=[]
for i in range(1,n+1):
    adjancy[i]=[]
for i in range (m):
    #b[i]=[]
    a1=input().split()
    u=int(a1[0])
    v=int(a1[1])
    w=int(a1[2])
    adjancy[u].append([v,w])
    adjancy[v].append([u,w])
    #b[(u,v)].append(w)
    b.append([u,v,w])
def SD(adjancy,x):
    d=[10**12]*(n+1)
    d[x]=0
    lev={x:0}
    Q=PriorityQueue()
    Q.put((0,x))
    while not Q.empty():
        t=Q.get()
        for l in adjancy[t[1]]:
            b1=l[0]
            b2=l[1]
            if d[b1]>b2+d[t[1]]:
                d[b1]=b2+d[t[1]]
                Q.put((d[b1],b1))
                lev[b1]=d[b1]
    return lev
l1=SD(adjancy,1)
l2=SD(adjancy,n)
#print(l2)
Q1=[]
for l in b:
    u=l[0]
    v=l[1]
    w=l[2]
    t1=l1[u]+l2[v]+w
    t2=t1+w+w
    t3=l1[v]+l2[u]+w
    t4=t3+w+w
    Q1.append(t1)
    Q1.append(t2)
    Q1.append(t3)
    Q1.append(t4)
p=10**12
for i in range (len (Q1)):
    if Q1[i]>l1[n] and Q1[i]<p:
        p=Q1[i]
print(p)        
        


 
            

