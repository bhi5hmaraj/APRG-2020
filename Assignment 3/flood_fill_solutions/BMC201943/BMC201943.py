inp = list(map(int,input().split()))
N = inp[0]
b = inp[1]
def Adj(i,j):
    l = []
    if (i == 1) and (j == N):
        l = [(1,N-1),(2,N)]
        
    elif (i == N) and (j == 1):
        l = [(N-1,1),(N,2)]
        
    elif (i == 1) and (j == 1):
        l = [(2,1),(1,2)] 
         
    elif (i == N) and (j == N):
        l = [(N-1,N),(N,N-1)]
         
    elif (i == 1):
        l = [(1,j-1),(1,j+1),(2,j)]
         
    elif (i == N):
        l = [(N,j-1),(N,j+1),(N-1,j)]
        
    elif (j == 1):
        l = [(i-1,1),(i+1,1),(i,2)]
        
    elif (j == N):
        l = [(i-1,N),(i+1,N),(i,N-1)]
        
    else:
        l = [(i-1,j),(i+1,j),(i,j+1),(i,j-1)]
    return (l)

color = [[0 for i in range(N+1)] for j in range(N+1)]

(a,c) = map(int,input().split())

for i in range(b):
    (j,k) = map(int,input().split())
    color[j][k] = 1
#print (color[3][1])
   
def bfs(i,j):
    Q = []
    #print (Adj(i,j))
    color[i][j]=2
    Q.append((i,j))
    while (Q != []):
        (v,u) = Q.pop(0)
        for k in Adj(v,u):
            if (color[k[0]][k[1]] == 0):
                color[k[0]][k[1]] = 2
                Q.append(k)
        
        
bfs(a,c)
            
flag = 0
for i in range(1,N+1):
    for j in range(1,N+1):
        if (color[i][j] == 0) and (flag == 0):
            print ('N')
            flag = 1
            break
if (flag == 0):
    print('Y')