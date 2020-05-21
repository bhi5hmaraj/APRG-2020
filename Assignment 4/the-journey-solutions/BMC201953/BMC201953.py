#defining infinity
infty = 100000000000

#taking N and K
inp = list(input().split())
N = int(inp[0])
K = int(inp[1])

#taking the timings
inp = list(input().split())
timings = []
for i in range(N):
    timings.append(int(inp[i]))

#adj matrix and labels
adj = []
shor = []
label = []
occurences = []
for i in range(100):
    occurences.append([])
#making the input array
inparray = []
counter = -1
for i in range(N):
    inp = list(input().split())
    inparray.append([])
    length = len(inp)
    for j in range(length):
        counter = counter + 1
        label.append(int(inp[j]))
        occurences[int(inp[j])].append(counter)
        inparray[i].append(int(inp[j]))
#making the adjacency matrix and the shortest path array
for i in range(counter + 1):
    shor.append([])
    for j in range(counter + 1):
        if (i == j):
            shor[i].append(0)
        else:
            shor[i].append(infty)
#filling the adjacency matrix
tcounter = -1
for i in range(N):
    length = len(inparray[i])
    for j in range(length):
        tcounter = tcounter + 1
        if (j + 1 < length):
            shor[tcounter][tcounter + 1] = (inparray[i][j + 1] - inparray[i][j]) * timings[i]
            shor[tcounter + 1][tcounter] = (inparray[i][j + 1] - inparray[i][j]) * timings[i]
for i in range(100):
    length = len(occurences[i])
    for j in range(length):
        for k in range(j + 1 , length):
            p1 = occurences[i][j]
            p2 = occurences[i][k]
            shor[p1][p2] = 60
            shor[p2][p1] = 60
            
#running floyd-warshall
#vertices are numbered 0 to counter
def floydw():
    for k in range(counter + 1):
        for i in range(counter + 1):
            for j in range(counter + 1):
                if (shor[i][k] + shor[k][j] < shor[i][j]):
                    shor[i][j] = shor[i][k] + shor[k][j]
floydw()
temp = infty
l1 = len(occurences[0])
l2 = len(occurences[K])
for i in range(l1):
    for j in range(l2):
        temp = min(temp , shor[occurences[0][i]][occurences[K][j]])
if (temp < infty):
    print(temp)
else:
    print("IMPOSSIBLE")

