def stup(arr,i,j):
    n=len(arr)
    if(i<0 or i>=n):
        return
    if(j<0 or j>=n):
        return
    if(arr[i][j]==0):
        return
    if(arr[i][j]==1):
        return    
    arr[i][j]=1
    stup(arr,i,j-1)
    stup(arr,i,j+1)
    stup(arr,i-1,j)
    stup(arr,i+1,j)
    
    
(n,b)=map(int,input().split(" "))
(i,j)=map(int,input().split(" "))
l=[]
for k in range(0,b):
    t=map(int,input().split(" "))
    l.append(list(t))
Adj=[[-1 for r in range(0,n)] for q in range(0,n)]
final=[[1 for r in range(0,n)] for q in range(0,n)]
for t in l:
    (x,y)=t
    Adj[x-1][y-1]=0
    final[x-1][y-1]=0
B=Adj
stup(B,i-1,j-1)
if(B==final):
    print("Y")
else:
    print("N")

