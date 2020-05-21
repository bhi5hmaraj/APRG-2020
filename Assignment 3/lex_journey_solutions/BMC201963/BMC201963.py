def BFS (l,x,y,n):
    a = []
    b = [x]
    c = [0 for i in range(n)]
    d = [0 for i in range(n)]
    while b:
        t = b.pop(0)
        c[(t-1)] = 1
        q = [i[0] for i in l[(t-1)]]
        for i in q:
            if c[(i-1)] == 0:
                if b == []:
                    b = [i]
                else:
                    b.append(i)
                c[(i-1)] = 1
                d[(i-1)] = d[(t-1)] + 1
    b = [y]
    e = []
    c = [0 for i in range(n)]
    while b:
        t = b.pop(0)
        e.append(t)
        c[(t-1)] = 1
        q = [i[0] for i in l[(t-1)]]
        for i in q:
            if c[(i-1)] == 0 and (d[(i-1)] == d[(t-1)] - 1):
                if b == []:
                    b = [i]
                else:
                    b.append(i)
                c[(i-1)] = 1
    f = [0 for i in range(n)]
    for i in e:
        f[i-1] = 1
    mylist = [x]
    while mylist != [y]:
        s = []
        for i in mylist:
            for k in l[(i-1)]:
                if d[(k[0]-1)] == 1 + d[(i-1)]:
                    if f[(k[0]-1)] == 1:
                        s.append(k)
        s1 = [i[1] for i in s]
        m = min(s1)
        a = a + [m]
        mylist = list(set([x[0] for x in s if x[1] == m]))
    return (a)
a = list(map(int, input().split()))
b = list(map(int, input().split()))
u = [[] for x in range(a[0])]
for i in range(a[1]):
    c = list(input().split())
    c[0] = int(c[0])
    c[2] = int(c[2])
    u[(c[0]-1)].append((c[2],c[1]))
    u[(c[2]-1)].append((c[0],c[1]))
k = BFS(u,b[0],b[1],a[0])
for i in k:
    print(i,end = "")