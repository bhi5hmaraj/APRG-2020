input1 = [int(x) for x in input().split()]
n = input1[0]
m = input1[1]
source = [[] for i in range(n+1)]
weight={}
for i in range(m):
    x, y, w = input().split()
    x = int(x)
    y = int(y)
    w = int(w)
    source[x].append(y)
    source[y].append(x)
    weight[(x,y)] = w
    weight[(y,x)] = w
    
wthere=[[] for i in range(n+1)]
visited = [0]*(n+1)
burnt = [0] * (n + 1)
wthere[1] = [0]
     
visited[1] = 1
previous = [1]
while previous:
    newone = []
    for i in previous:
        for j in source[i]:
            for k in wthere[i]:
                wthere[j].append(k + weight[(i,j)])
            if visited[j] == 0:
                if burnt[j] == 0:
                    burnt[j] = 1
                    newone.append(j)
    previous = newone[:]
    for g in previous:
        visited[g] = 1
newmin = sorted(wthere[n])
print(newmin[1])


