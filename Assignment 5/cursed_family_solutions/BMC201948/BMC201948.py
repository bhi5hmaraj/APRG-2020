from queue import Queue

n = int(input())
ftree = [[] for j in range(0, n)]
fam = [0 for i in range(0, n)]
wcount = 0
    

for i in range(0, n-1):
    u, v = [int(i) - 1 for i in input().split()]
    ftree[u].append(v)
    ftree[v].append(u)

l = Queue()
l.put((0, 1))

while not(l.empty()):
    (v, vc) = l.get()    
    if vc == 1:
        wcount += 1
    fam[v] = 1
    for nb in ftree[v]:
        if fam[nb] ==0:
            l.put((nb, (vc + 1) % 2))

print(max(wcount, n - wcount))
    



        
    