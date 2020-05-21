import sys
from collections import defaultdict

(N,k)=map(int,input().split())
T={}
M=list(map(int,input().split()))
for m in range(len(M)):
    T[m+1]=M[m]
    
G={}
W=defaultdict(int)
A=[]
B=[]
for i in range(N):
    L=list(map(int,input().split()))
    if L[0]==0:
        A.append(i+1)
    l=len(L)
    for j in range(l):    
        if L[j]==k:
            B.append(i+1)
        if (L[j],i+1) not in G:
            G[(L[j],i+1)]=[]
        if j<l-1:
            G[(L[j],i+1)].append((L[j+1],i+1))
            W[((L[j],i+1),(L[j+1],i+1))]=T[i+1]*(L[j+1]-L[j])
            W[((L[j+1],i+1),(L[j],i+1))]=T[i+1]*(L[j+1]-L[j])
        if j>0:
            G[(L[j],i+1)].append((L[j-1],i+1))
            W[((L[j],i+1),(L[j-1],i+1))]=T[i+1]*(L[j]-L[j-1])
            W[((L[j-1],i+1),(L[j],i+1))]=T[i+1]*(L[j]-L[j-1])
    for g1 in G:
        for g2 in G:
            if g1[0]!=0 and g1[0]==g2[0]:
                G[g1].append(g2)
                G[g2].append(g1)
                W[(g1,g2)]=60
                W[(g2,g1)]=60 

def timeSetter(t): 
    
    P=sys.maxsize
    
    for x in range(len(A)):
        for y in range(len(B)):
            visited={}
            cost={}
            for station in G:
                cost[station]=sys.maxsize

            def leastCost(f):
                least=sys.maxsize
                c=0
                for vertex in f:
                    if cost[vertex]<least:
                        least=cost[vertex]
                        leastInd=vertex
                        c=1
    
                if c==1: 
                    return leastInd
                else:
                    return -1
        

            def costSetter(s,t):
                
                cost[s]=0
                f={}
                f[s]=1
                visited[s]=1
                
    
                while s!=(-1):
                    s=leastCost(f)
                    if s==-1:
                        break
        
    
                    else:  
                        f.pop(s)
                        for neighbour in G[s]:
                            a=cost[s] + W[(s,neighbour)]
                            if a<=cost[neighbour]:
                                cost[neighbour]=a
                                f[neighbour]=1
                                visited[neighbour]=1
                                
                if t in  visited:
                    return cost[t]
                else:
                    return -1
                    
            if costSetter((0,A[x]),(t,B[y]))!=-1:
                if costSetter((0,A[x]),(t,B[y]))<P:
                    P=costSetter((0,A[x]),(t,B[y]))
                
            
    
    if P==sys.maxsize:
        print("IMPOSSIBLE")
        
    else:
        print(P)
       
timeSetter(k)
