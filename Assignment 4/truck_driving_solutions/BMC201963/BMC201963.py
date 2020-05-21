def thirdel(l):
    return(l[2])
def likekruskal (l,n):
    p = [[0 for x in range(n)] for y in range(n)]
    c = [[(i+1)] for i in range(n)]
    for k in l:
        if c[k[0]-1] != c[k[1]-1]:
            for i in c[k[0]-1]:
                for j in c[k[1]-1]:
                    p[(i-1)][(j-1)] = k[2]
            for i in c[k[1]-1]:
                for j in c[k[0]-1]:
                    p[(i-1)][(j-1)] = k[2]
            c[k[0]-1].extend(c[k[1]-1])
            for i in c[k[0]-1]:
                if i != k[0]:
                    c[i-1] = c[k[0]-1]
    return(p)
x = list(map(int, input().split()))
t = []
for i in range(x[1]):
    a = list(map(int, input().split()))
    if t == []:
        t = [a]
    else:
        t.append(a)
s = sorted(t,key=thirdel)
q = int(input())
l = likekruskal(s,x[0])
for j in range(q):
    d = list(map(int, input().split()))
    print(l[d[0]-1][d[1]-1])