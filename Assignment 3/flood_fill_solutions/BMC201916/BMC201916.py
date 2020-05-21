L = list(map(int,input().split()))
N, b = L[0], L[1]
ini = list(map(int,input().split()))
l1 = []
for i in range(b):
    l1.append(list(map(int,input().split())))
K = [[0 for i in range(N)] for j in range(N)]
for e in l1:
    i,j = e[0], e[1]
    K[i-1][j-1]+=2
def func(v):
    q = []
    v[ini[0]-1][ini[1]-1] = 1
    q.append(ini)
    while(q):
        z = q.pop(0)
        i = z[0]
        j = z[1]
        r = [[i-1,j],[i,j-1],[i+1,j],[i,j+1]]
        for e in r:
            a = e[0]
            b = e[1]
            if(0<a<=N and 0<b<=N and v[a-1][b-1] == 0):
                v[a-1][b-1] = 1
                q.append(e)
    ct = 0           
    for i in range(N):
        for j in range(N):
            if(v[i][j] == 0):
                ct += 1
                break
    if(ct):
        return ("N")
    else:
        return ("Y")    
    
if(b!=len(l1)):
    b=len(l1)
if(ini in l1):
    print("N")
else:
    print(func(K))