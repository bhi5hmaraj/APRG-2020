from queue import Queue

n,m = map(int, input().split())
u1, u2 = map(int, input().split())

adj = [[] for i in range(n+1)]

Xy = [-1 for i in range(n+1)]
lY = [-1 for i in range(n+1)]
vis = [0 for i in range(n+1)]



for _ in range(m):
    inp = [x for x in input().split()]
    x = int(inp[0])
    y = int(inp[2])
    w = inp[1]
    adj[x].append([y,w])
    adj[y].append([x,w])

q1 = Queue()
q2 = Queue()
q1.put(u1)
q2.put(u2)
Xy[u1] = 0
lY[u2] = 0

while not q1.empty():
    s = q1.get()
    for a in adj[s]:
        v = a[0]
        if(Xy[v] == -1):
            Xy[v] = 1+Xy[s]
            q1.put(v)    

while not q2.empty():
    s = q2.get()
    for a in adj[s]:
        v = a[0]
        if(lY[v] == -1):
            lY[v] = 1+lY[s]
            q2.put(v)

q3 = Queue()
q3.put(u1)
vis[u1] = 1
se = [[] for i in range(n+1)]
ans = []

while not q3.empty():
    s = q3.get()
    mi = 1000

    for a in adj[s]:
        v = a[0]
        c = a[1]
        if(Xy[s]+1 + lY[v] == Xy[u2] and vis[v] == 0):
            if(ord(c) <= mi):
                mi = ord(c)

    se[Xy[s]].append((chr(mi),s))

    if(q3.empty()):
        #print(Xy[s],se[Xy[s]])
        if(Xy[s] == Xy[u2]):
            break
        ss = min(se[Xy[s]])

        ans.append(ss[0])

        for el in se[Xy[s]]:
            if(el[0] == ss[0]):
                for v in adj[el[1]]:
                    if(el[0] == v[1] and Xy[el[1]]+1 + lY[v[0]] == Xy[u2] and vis[v[0]] == 0):
                        vis[v[0]] = 1
                        q3.put(v[0])
#print(se)



print(''.join(x for x in ans))

