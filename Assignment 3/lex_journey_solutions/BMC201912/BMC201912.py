from queue import Queue
v,e = [int(i) for i in input().split()]
x,y = [int(i) for i in input().split()]
adjl = [[] for i in range(v+1)]
rval = {}
def mikiri(c):
    return ord(c) - ord('a')
def sekiro(d):
    return chr(d + ord('a'))
for i in range(e):
    l = list(input().split())
    u = int(l[0])
    w = int(l[2])
    c = mikiri(l[1])
    adjl[u].append(w)
    adjl[w].append(u)
    rval[(u,w)] = c
    rval[(w,u)] = c
def bfs(x): #code is taken from Lecture 14
    dist = [None]*(v+1)
    isdisc = [False]*(v+1)
    bfsque = Queue()
    isdisc[x] = True
    dist[x] = 0
    bfsque.put(x)
    while (bfsque.empty() == False):
        u = bfsque.get()
        for w in adjl[u]:
            if (isdisc[w] == False):
                isdisc[w] = True
                dist[w] = dist[u] + 1
                bfsque.put(w)
    return (dist, isdisc)
dist1, isdisc1 = bfs(x)
dist2, isdisc2 = bfs(y)
d = dist1[y]
def cmin(z):
    return (dist1[z] + dist2[z] == d)
def iterate():
    optl = []
    s = [x]
    for i in range(1, d+1):
        pval = set()
        for j  in s:
            for k in adjl[j]:
                if (cmin(k) and (dist1[k] == i)):
                    pval.add(rval[(j,k)])
        oc = min(pval)
        optl.append(oc)
        t = set()
        for j in s:
            for k in adjl[j]:
                if (cmin(k) and (rval[(j,k)]==oc) and (dist1[k] == i)):
                    t.add(k)
        s = []
        for j in t:
            s.append(j)
    s = ''.join(list(map(sekiro, optl)))
    print(s)
iterate()

