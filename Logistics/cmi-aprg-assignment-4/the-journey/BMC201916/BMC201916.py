import sys
Nk = list(map(int,input().split()))
N = Nk[0]
k = Nk[1]
T = list(map(int,input().split()))
rtes = []
for i in range(N):
    f = list(map(int,input().split()))
    if(len(f)>1):
        rtes.append(f)
    else:
        T.pop(i)
G = {}
if(rtes==[]):
    print("IMPOSSIBLE")
    sys.exit()
for i in range(len(rtes)):
    y = len(rtes[i])
    for j in range(y):
        if(j == 0):
            G[(rtes[i][j],i+1)] = [(rtes[i][j+1],(abs(rtes[i][j+1]-rtes[i][j]))*T[i],i+1)]
        elif(j==y-1):
            G[(rtes[i][j],i+1)] = [(rtes[i][j-1],(abs(rtes[i][j-1]-rtes[i][j]))*T[i],i+1)]
        else:
            G[(rtes[i][j],i+1)] = [(rtes[i][j+1],(abs(rtes[i][j+1]-rtes[i][j]))*T[i],i+1),(rtes[i][j-1], (abs(rtes[i][j-1]-rtes[i][j]))*T[i],i+1)]
L = list(G.keys())
z = len(L)
for j in range(z):
    for w in range(j+1,z):
        if (L[j][0] == L[w][0]):
            if(L[j][0] not in {0,k}):
                G[L[j]].append((L[w][0],60,L[w][1]))
                G[L[w]].append((L[j][0],60,L[j][1]))
            else:
                G[L[j]].append((L[w][0],0,L[w][1]))
                G[L[w]].append((L[j][0],0,L[j][1]))
Size = {}
l = list(G.keys())
for e in l:
    Size[e] = 9223372036854775807
start = None
end = None
for e in l:
    if (e[0] == 0):
        start = e
        break
for e in l:
    if (e[0] == k):
        end = e
        break
def assignsize():
    Visited = {}
    for i in l:
        Visited[i] = 0 
    Size[start] = 0
    minsize = 0
    Q = [start]
    while(minsize < 9223372036854775807):
        for e in Q:
            Visited[e] = 1
            for f in G[e]:
                if (Size[(f[0],f[2])] > Size[e]+f[1]):
                    Size[(f[0],f[2])] = Size[e]+f[1]
        M = list(filter(lambda x: Visited[x]==0, l))
        if(M):
            minsize = min(map(lambda y: Size[y], M))
            Q = []
            for e in M:
                if(Size[e] == minsize):
                    Q.append(e)
        else:
            break
if(start == None or end == None):
    print ("IMPOSSIBLE")
else:
    assignsize() 
    if(Size[end] != sys.maxsize):
        print (Size[end])
    else: 
        print("IMPOSSIBLE")


    
