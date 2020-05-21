from queue import PriorityQueue
list_firstLine =  list(map(int,input().split()))
N = list_firstLine[0]
des = list_firstLine[1]

T = list(map(int,input().split()))
T.insert(0,0)

Adj = [ [ [ ] for j in range(101) ] for i in range(N+1) ]
        
busStop = [[] for i in range(N+1)]
for i in range(1,N+1):
    busStop[i] = list(map(int,input().split()))
    
for i in range(1,N+1):
    for j in busStop[i]:
        for k in busStop[i]:
            if (k > j):
                Adj[i][j].append((T[i]*(k-j),(i,k)))
            elif (k < j):
                Adj[i][j].append((T[i]*(j-k),(i,k)))
                
myList = [[] for i in range(100)]  
              
for k in range(100):
    for j in range(1,N+1):
        if (k in busStop[j]):
            myList[k].append(j)
            
for k in range(100):
    for j in myList[k]:
        for t in myList[k]:
            if (t!=j):
                Adj[j][k].append((60,(t,k)))

dis = [ [ [ 10**15 for k in range(101) ] for j in range(N+1) ] for i in range(N+1) ]

def Dijkstra(n):
    dis[n][n][0] = 0
    Q = PriorityQueue()
    Q.put((0,(n,0)))
    while (Q.empty() == False):
        (a,(b,e)) = Q.get()
        for (w,(o,c)) in Adj[b][e]:
            if (dis[n][o][c] > dis[n][b][e] + w):
                dis[n][o][c] = dis[n][b][e] + w
                Q.put((dis[n][o][c],(o,c)))

for i in range(1,N+1):
    Dijkstra(i)




ans = 10**15
for i in range(1,N+1):
    for j in range(1,N+1):
        ans = min(ans,dis[i][j][des])
if (ans == 10**15):
    print ("IMPOSSIBLE")
else:
    print (ans)
