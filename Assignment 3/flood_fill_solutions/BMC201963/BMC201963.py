import sys
sys.setrecursionlimit(10**6)
def vertex (v,n):
    x = v[0]
    y = v[1]
    if x < (n+1) and x > 0 and y < (n+1) and y > 0:
        return(True)
    else:
        return(False)
def BFS (v,n,B):
    a = []
    p = [v]
    c = [0 for i in range(n*n)]
    for i in B:
        c[(((i[0]-1)*n)+i[1]-1)] = 1
    while p:
        x = p.pop(0)
        if a == []:
            a = [x]
        else:
            a.append(x)
        c[(((x[0]-1)*n)+x[1]-1)] = 1
        u = x[0]
        v = x[1]
        m = [[u+1,v],[u,v+1],[u-1,v],[u,v-1]]   
        for i in m:
            if vertex(i,n) and c[(((i[0]-1)*n)+i[1]-1)] == 0:
                if p == []:
                    p = [i]
                else:
                    p.append(i)
                c[(((i[0]-1)*n)+i[1]-1)] = 1
    if c == [1 for j in range(n*n)]:
        return("Y")
    else:
        return("N")
a = list(map(int, input().split()))
t = list(map(int, input().split()))
b = []
n = a[0]
for i in range (a[1]):
    c = list(map(int, input().split()))
    if b == []:
        b = [c]
    else:
        b.append(c)
print(BFS (t,n,b))

    

    

