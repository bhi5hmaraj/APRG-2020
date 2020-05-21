import sys
import math
L = list(map(int,input().split()))
N = L[0]
M = L[1]
G = [[] for i in range(N)]
E = []
for i in range(M):
    l = list(map(int,input().split()))
    #print(1)
    E.append((l[2],l[0],l[1]))                      #Edges stored as (weight, end1, end2) for easy sorting.
    G[l[0]-1].append((l[1],l[2]))
    G[l[1]-1].append((l[0],l[2]))

Edges = sorted(E,key = lambda x: x[0])
#print(Edges)
InMinSpanningTree = [0 for i in range(M)]

Parent = [i+1 for i in range(N)]
Size = [1 for i in range(N)]
def find(f):
    while(Parent[f-1] != f):
        Parent[f-1] = Parent[Parent[f-1]-1]
        f = Parent[f-1]
    return f
def union(xRoot,yRoot):
    #xRoot = find(x)
    #yRoot = find(y)
    if(xRoot != yRoot):
        if(Size[xRoot-1] < Size[yRoot-1]):
            temp = xRoot
            xRoot = yRoot
            yRoot = temp
        Parent[yRoot-1] = xRoot
        Size[xRoot-1] += Size[yRoot-1]

def kruskal():
    No_of_Edges = 0
    i = 0
    while(No_of_Edges < N-1):
        #print(No_of_Edges)
        (w,u,v) = Edges[i]
        uRoot = find(u)
        vRoot = find(v)
        if(uRoot != vRoot):
            No_of_Edges += 1
            InMinSpanningTree[i] = 1
            union(uRoot,vRoot)
        i += 1

kruskal()
#print(Edges)
#print(InMinSpanningTree)
MaxLog = math.ceil(math.log2(N))
P = [[-1 for i in range(MaxLog)]for j in range(N)]
A = [[0 for i in range(MaxLog)]for j in range(N)]
Root = find(1)
MST = [[] for i in range(N)]
for i in range(M):
    if(InMinSpanningTree[i] == 1):
        K = Edges[i]
        MST[K[1]-1].append((K[2],K[0]))
        MST[K[2]-1].append((K[1],K[0]))
        
Level = [1 for i in range(N)]
Visited = [0 for i in range(N)]
parent_in_tree = [(-1,0) for i in range(N)]
def bfs():
    Q = [Root]
    while(Q):
        z = Q.pop(0)
        Visited[z-1] = 1
        for elem in MST[z-1]:
            if(Visited[elem[0]-1] == 0):
                Level[elem[0]-1] = Level[z-1]+1
                parent_in_tree[elem[0]-1] = (z,elem[1])
                Q.append(elem[0])

                     
bfs()                


#print(parent_in_tree)
#print(MST)
for i in range(N):
    P[i][0] = parent_in_tree[i][0]
    A[i][0] = parent_in_tree[i][1]

#print(PWA)
for j in range(1,MaxLog):
    for i in range(N):
        if(P[i][j-1] != -1):
            P[i][j] = P[P[i][j-1]-1][j-1]
            A[i][j] = max(A[i][j-1],A[P[i][j-1]-1][j-1])
            
#print(PWA)
    
def Tanksize(u,v):
    if(Level[u-1] < Level[v-1]):
        temp = u
        u = v
        v = temp
    #print("#")    
    #print(Level[u-1])    
    #print(Level[v-1])
    u_to_LCA = A[u-1][0] 
    v_to_LCA = A[v-1][0]
    levdif = Level[u-1] - Level[v-1]
    while(levdif > 0):
        raise_by = math.floor(math.log2(levdif))

        u_to_LCA = max(u_to_LCA,A[u-1][raise_by])
        u = P[u-1][raise_by]
        
        levdif -= (1<<raise_by)

    if (u == v):
        LCA = u
        answer = u_to_LCA    
    else:
        k = MaxLog-1
        #print("@")
        #print(PWA[u-1][k-1])
        while(k >= 0):
            if(P[u-1][k-1] != -1 and P[u-1][k-1] != P[v-1][k-1]):
                u_to_LCA = max(u_to_LCA,A[u-1][k-1])
                v_to_LCA = max(v_to_LCA,A[v-1][k-1])
                u = P[u-1][k-1]
                v = P[v-1][k-1]
            k = k-1
        LCA = parent_in_tree[u-1][0]
        answer = max(u_to_LCA,v_to_LCA,A[u-1][0],A[v-1][0])
    #print(LCA)
    print(answer)
    
q = int(input())
for i in range(q):
    l = list(map(int,input().split()))
    Tanksize(l[0],l[1])

 


