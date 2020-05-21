from queue import Queue

#graph information
line = list(input().split())
N = int(line[0])
M = int(line[1])

#vertices X and Y
line = list(input().split())
X = int(line[0])
Y = int(line[1])

#adjacency list and shortest path lists
adj = []
shorX = []
shorY = []
xmin = []
status = []
for i in range(N + 1):
    adj.append([])
    shorX.append(-1)
    shorY.append(-1)
    xmin.append(None)
    status.append(0)
    
for i in range(M):
    line = list(input().split())
    a = int(line[0])
    b = int(line[2])
    c = line[1]
    adj[a].append([b , c])
    adj[b].append([a , c])
    
#bfs
def bfs(source):
    queue = Queue()
    if source == X:
        shorX[source] = 0
    else:
        shorY[source] = 0
    queue.put(source)
    while (queue.empty() == 0):
        felem = queue.get()
        for i in range(len(adj[felem])):
            j = adj[felem][i][0]
            if source == X:
                if(shorX[j] == -1):
                    shorX[j] = 1 + shorX[felem]
                    queue.put(j)
            else:
                if(shorY[j] == -1):
                    shorY[j] = 1 + shorY[felem]
                    queue.put(j)
#printing the path from source X
bfs(X)
bfs(Y)

#setting the xmins
#if xmin is non-none then vertex lies on a shortest path 
def setxMin():
    for i in range(N + 1):
        if i == 0:
            continue
        if(shorX[i] + shorY[i] == shorX[Y]):
            temp = None
            for j in range(len(adj[i])):
                k = adj[i][j][0]
                l = adj[i][j][1]
                if (shorX[i] + 1 + shorY[k] == shorX[Y]):
                    if (temp == None):
                        temp = l
                    elif (l < temp):
                        temp = l
            xmin[i] = temp
setxMin()

#making the path
def printPath():
    path = ""
    activeList = [X]
    blankList = []
    
    while(len(activeList) != 0):
        temp = None
        flag = 0
        for i in range(len(activeList)):
            if(temp == None or temp > xmin[activeList[i]]):
                temp = xmin[activeList[i]]
        path = path + temp
        for i in range(len(activeList)):
            if(xmin[activeList[i]] == temp):
                for j in range(len(adj[activeList[i]])):
                    qv = adj[activeList[i]][j][0]
                    q = adj[activeList[i]][j][1]
                    if(qv == Y):
                        flag = 1
                        break
                    if(shorX[activeList[i]] + 1 + shorY[qv] == shorX[Y] and q == temp and status[qv] == 0):
                        status[qv] = 1
                        blankList.append(qv)
        if(flag):
            break
        activeList = blankList
        blankList = []
    return path
if(X == Y):
    print("")
else:
    print(printPath())