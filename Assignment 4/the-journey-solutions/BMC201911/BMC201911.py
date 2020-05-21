from queue import PriorityQueue
a=list(input().split())
n=int(a[0])
k=int(a[1])
T={}
adjancy={}
Stop={}
a1=list(map(int,input().split()))
for i in range (1,n+1):
    T[i]=a1[i-1]
   # T[i].append(a1[i-1])
    Stop[i]=[]
    a2=list(map(int,input().split()))
    #for j in range (len (a2)):
       # Stop[i].append(a2[j]) 
    Stop[i]=a2    
for i in range (1,n+1):
    for j in range (100):
        adjancy[(i,j)]=[]
    for j in range (len(Stop[i])-1):
        adjancy[(i,Stop[i][j])].append([(i,Stop[i][j+1]),T[i]*(Stop[i][j+1]-Stop[i][j])])
        adjancy[(i,Stop[i][j+1])].append([(i,Stop[i][j]),T[i]*(Stop[i][j+1]-Stop[i][j])])     
for i in range (1,n):
    for j in range (100):
        for k1 in range(i+1,n+1):
            adjancy[(i,j)].append([(k1,j),60])
            adjancy[(k1,j)].append([(i,j),60]) 
#print(adjancy)            
if i in adjancy:
    x=i[0]
    y=i[1]
def SD (x,y):
    d={}
    for i in adjancy:
        d[i]=10**12
    d[(x,y)]=0
  #  lev={(x,y):0}
    Q=PriorityQueue()
    Q.put((0,(x,y)))
   # r={(x,y):[(x,y)]}
    while not Q.empty():
        t=Q.get()
        for l in adjancy[t[1]]:
            b1=l[0]
            b2=l[1]
            if d[b1]>b2+d[t[1]]:
                d[b1]=b2+d[t[1]]
                Q.put((d[b1],b1))
               # lev[b1]=d[b1]
    #            r[b1]=r[t[1]]+[b1]
    return d
    
#l1=SD (1,0)
#print(l1[(1,30)])
#print(r)
S=[]
D=[]
Q1=PriorityQueue()
for i in range(1,n+1):
    if 0 in Stop[i]:
        S.append(i)
    if k in Stop[i]:
        D.append(i)
if len(S)!=0 and len(D)!=0:
    for i in range (len(S)):
        for j in range(len(D)):
            l=SD (S[i],0)
            t=l[(D[j],k)]
            Q1.put((t,t))
    p=Q1.get()
    if p[0]<10**12:
        print(p[0])
    else:
        print("IMPOSSIBLE")
else:
    print("IMPOSSIBLE")
        
  
#print(D)
        
        
        

    
          
   



