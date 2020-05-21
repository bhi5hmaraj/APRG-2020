s = str(input()).split()
N = int(s[0])
M = int(s[1])

Adj = []
for i in range(M):
    s = str(input()).split()
    u = int(s[0]) - 1
    v = int(s[1]) - 1
    weight = int(s[2])
    Adj.append([u,v,weight])
    Adj.append([v,u,weight])
Adj = sorted(Adj,key = lambda x : x[2])

s = str(input()).split()
Q = int(s[0])
B = [set([]) for j in range(N)]
answer = [0]*Q
for k in range(Q):
    s = str(input()).split()
    a = int(s[0]) - 1
    b = int(s[1]) - 1
    B[a].add(k)
    B[b].add(k)

def kruskal():
    i = 0
    e = 0
    P = list(range(N))
    while e < N-1:
        a = Adj[i][0]
        b = Adj[i][1]
        weight = Adj[i][2]
        i = i + 1
        
        while a != P[a]:
            a = P[a]

        while b != P[b]:
            b = P[b]
        if a != b:
            e = e+1
            r = len(B[a])
            s = len(B[b])
            if r > s:
                P[b] = a
            else:
                P[a] = b
            if P[b] == a:
                for ll in B[b]:
                    if ll in B[a]:
                        answer[ll] = weight 
                        B[a].remove(ll)
                    else:
                        B[a].add(ll)
            else:
                for ll in B[a]:
                    if ll in B[b]:
                        answer[ll] = weight 
                        B[b].remove(ll)
                    else:
                        B[b].add(ll)

kruskal()
for i in range(Q):
    print(answer[i])