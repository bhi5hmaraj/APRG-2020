n,d,r = list(map(int,input().split()))
M = [0 for i in range(n)]
N = [0 for i in range(n)]
M = list(map(int,input().split()))
N = list(map(int,input().split()))
for i in range(n): N[i] = -N[i]
M.sort()
N.sort()
c = 0
for i in range(n): c += max(0,M[i]-N[i]-d)*r
print(c)