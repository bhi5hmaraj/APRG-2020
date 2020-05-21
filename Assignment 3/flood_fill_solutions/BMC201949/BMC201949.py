from queue import *
def bfs_color(z,Map):
    Q=Queue()
    Q.put(z)
    Map[z[0]][z[1]]=2 
    while Q.empty()!=True:
        w=Q.get()
        u=w[0]
        v=w[1]
        A=[(u+1,v),(u,v+1),(u-1,v),(u,v-1)]
        for x in A:
            if Map[x[0]][x[1]]<1:
                Map[x[0]][x[1]]=2
                Q.put(x)
                    
        
    
info=input().split()
N=int(info[0])
b=int(info[1])
x=input().split()
Map=[]
for i in range(0,N+2):
    Map.append([])
    for j in range(0,N+2):
        Map[i].append(0)
                     
    
for i in range(b):
    y=input().split()
    p1=int(y[0])
    p2=int(y[1])
    Map[p1][p2]=1
for k in range(0,N+2):
    Map[0][k]=1
    Map[k][0]=1
    Map[N+1][k]=1
    Map[k][N+1]=1
a=int(x[0])
b=int(x[1])
bfs_color((a,b),Map)
flag=0
for i in range(N):
    if flag==1:
        break
    for j in range(N):
        if Map[i][j]<1:
            flag=1
            break
if flag==0:
    print("Y")
else:
    print("N")
            
            
            
        
        

    
    
    
    

    
            
        
    


    
            
    


