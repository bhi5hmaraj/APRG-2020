def makegraph():
    
    F = [[] for i in range(N)]
    for j in range(M):
        e1 = int(E[j][0])
        e2 = int(E[j][2])
        F[e1-1].append(e2)
        F[e2-1].append(e1)
        
    return(F)

def make_graph_with_edge():
    
    F = [[] for i in range(N)]
    for j in range(M):
        e1 = int(E[j][0])
        e2 = int(E[j][2])

        F[e1-1].append((e2,E[j][1]))
        F[e2-1].append((e1,E[j][1]))
        
    return(F)


def assignsize():
    S = []
    for k in range(N):
        S.append(0)
    Visited = S.copy()
    Q = [I]
    Visited[I-1] = 1
    while(Q):
        z = Q.pop(0)
        for nbr in (G[z-1]):
            if (Visited[nbr-1] == 0):
                Visited[nbr-1] = 1
                Q.append(nbr)
                S[nbr-1] = (S[z-1] + 1)
        
    return S

def find_nodes_on_shortest_paths():
    Visited = []
    for k in range(N):
        Visited.append(0)
    
    Q = [J]
    Visited[J-1] = 1
    on_shortest_path = Visited.copy()
    while(Q):
        z = Q.pop(0)

        for elem in G[z-1]:
            if(Visited[elem-1] == 0):
                Visited[elem-1] = 1 
                if(S[elem-1] == S[z-1]-1):

                    on_shortest_path[elem-1] = 1
                    Q.append(elem)

    return on_shortest_path

def find_path():
    Q = [I]
    str = ""
    
    while(Q != [J]):
        templist = []
        #print(Q)
        for elem in Q:
            for nbr in G1[elem-1]:
                if (S[nbr[0]-1] == S[elem-1]+1):
                    if (NS[nbr[0]-1] == 1):
                        templist.append(nbr)
        ch = min(map(lambda x: x[1], templist))
        #print('*' + ch)
        str = str + ch
        Q = list(set([x[0] for x in templist if x[1] == ch]))     
       
    
    print (str)

VE = list(map(int,input().split()))
N = VE[0]
M = VE[1]
K = list(map(int,input().split()))
I = K[0]
J = K[1]

E = []
for i in range(M):
    E.append(list(input().split()))

G = makegraph()
G1 = make_graph_with_edge()
#print(G1)
S = assignsize()
#print(S)
NS = find_nodes_on_shortest_paths()
#print(NS)
find_path()