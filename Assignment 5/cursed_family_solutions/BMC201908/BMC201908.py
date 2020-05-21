import sys
sys.setrecursionlimit(10**5)

s = str(input()).split()
N = int(s[0])

Adj = [[] for j in range(N)]

for i in range(N-1):
    s = str(input()).split()
    u = int(s[0]) - 1
    v = int(s[1]) - 1
    Adj[u].append(v)

Gather = [0]*N

def DP(i):
    if Gather[i] == 0:
        
        if len(Adj[i]) == 0:
            Gather[i] = 1
        else:
            for child in Adj[i]:
                for grandchild in Adj[child]:    
                    DP(grandchild)
                DP(child)
            c = 0
            d = 0
            for child in Adj[i]:
                for grandchild in Adj[child]:
                    d = d + Gather[grandchild]
                c = c + Gather[child]
            g = max(c, d+1)
            l = max(g,1)
            Gather[i] = l

for j in range(N):
    if Gather[j] == 0:
        DP(j)

print(max(Gather))