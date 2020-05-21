import sys
sys.setrecursionlimit(10**6)
K,b=input().split()
K,b=int(K),int(b)
x,y=input().split()
x,y=int(x),int(y)
s = [[1] * (K+2)] + [[1] + [0] * K + [1] for i in range(K)] + [[1] * (K+2)] 
for i in range(b):
    k,l=input().split()
    k,l=int(k),int(l)
    s[k][l] = 1 
f = [(x,y)]
s[x][y] = 2   
while f:
    fi = []
    for (m, n) in f:
        ne = [(m+1,n),(m-1,n),(m,n+1),(m,n-1)]
        for (p,q) in ne:
            if not s[p][q]:
                s[p][q] = 2
                fi.append((p,q))
    f = fi[:]    
R  =[]
for line in s:
    if 0 in line:
        R.append(1)       
if R:
    print("N")
else:
    print("Y")