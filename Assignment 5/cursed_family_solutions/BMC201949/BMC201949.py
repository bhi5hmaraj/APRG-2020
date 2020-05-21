n=int(input())
A=[]
Mark=[]
for i in range(n):
    A.append([])
    Mark.append(0)
seq=[0]    
for i in range(0,n-1):
    seq.append(i+1)
    x=list(map(int,input().split()))
    p=x[0]-1
    q=x[1]-1
    A[p].append(q)
    Mark[q]=1
def height(i):
    if A[i]==[]:
        h=0
    else:
        f=0
        for j in A[i]:
            f=max(f,height(j))
        h=1+f
    return h   
seq.sort(key=height)    
dp=[]
for j in range(n):
    dp.append(-1)
def calc_gather(v,A,X):
    s1=0
    s2=0
    for w in A[v]:
        s1=s1+X[w]
        for u in A[w]:
            s2=s2+X[u]
    return(s1,s2)    
for i in range(0,n):
    k=seq[i]
    if dp[k]>0:
        continue
    else:
        if A[k]==[]:
            dp[k]=1
        else:
            (s,t)=calc_gather(k,A,dp)
            q=max(s,1+t)
            dp[k]=q
for j in range(0,n):
    if Mark[j]==0:
        print(dp[j])
        break
            

            




        
        
    
    
            
    
    
