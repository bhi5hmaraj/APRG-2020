N=int(input())
g={}
for n in range(N-1):
    (u,v)=map(int, input().split())
    if u not in g:
        g[u]=[]
    if v not in g:
        g[v]=[]
    g[u].append(v)

d=0    
for i in g:
    for j in g:
        if i not in g[j]:
            d+=1
    if d==len(g):
        R=i
        break

lm={}
def largestMem(R):  
    
    if g[R]==[]:
        lm[R]=1
        return 1
        
    else:
        A=0
        for node in g[R]:
            if node not in lm:
                lm[node]=largestMem(node)
            A=A+lm[node]
            
        B=1
        for son in g[R]:
            for grandson in g[son]:
                if grandson not in lm:
                    lm[grandson]=largestMem(grandson)
                B=B+lm[grandson]
                
        return max(A,B)
        
print(largestMem(R))