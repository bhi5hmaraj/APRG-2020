L1 = list(map(int, input().split()))
M = list(map(int, input().split()))
E = list(map(int, input().split()))
n = L1[0]
d = L1[1]
r = L1[2]
M = sorted(M)
E = sorted(E, reverse = True)
minovertime = 0
for i in range(n):
    if(M[i]+E[i]-d > 0):
        minovertime += r*(M[i]+E[i]-d)

print(minovertime)
    
