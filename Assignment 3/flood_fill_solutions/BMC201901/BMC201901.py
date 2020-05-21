
inNb = list(map(int, input().split()))
n = inNb[0]
b = inNb[1]

u = list(map(int, input().split()))
u[0] -= 1
u[1] -= 1

color = []
visited = []
for i in range(0,n):
    color.append([])
    visited.append([])

for i in range(0,n):
    for j in range(0,n):
        color[i].append(0)
        visited[i].append(0)

totB = 0
for i in range(0, b):
    inB = list(map(int, input().split()))
    if(color[inB[0] - 1][inB[1] - 1] == 0):
        color[inB[0] - 1][inB[1] - 1] = 1
        totB += 1

visited[u[0]][u[1]] = 1
totVisits = 1

def unvisitedNeighborList(v):
    neighbors = []
    if(v[0] != 0 and v[0] != n-1):
        if(v[1] != 0 and v[1] != n-1):
            if(color[v[0] -1][v[1]] == 0 and visited[v[0] -1][v[1]] == 0):
                neighbors.append([v[0] - 1, v[1]])
                visited[v[0] - 1][v[1]] = 1
            if(color[v[0] +1][v[1]] == 0 and visited[v[0] +1][v[1]] == 0):
                neighbors.append([v[0] + 1, v[1]])
                visited[v[0] + 1][v[1]] = 1
            if(color[v[0]][v[1] - 1] == 0 and visited[v[0]][v[1] - 1] == 0):
                neighbors.append([v[0], v[1] -1])
                visited[v[0]][v[1] - 1] = 1
            if(color[v[0]][v[1] + 1] == 0 and visited[v[0]][v[1] +1] == 0):
                neighbors.append([v[0], v[1] +1])
                visited[v[0]][v[1] + 1] = 1

        elif(v[1] == 0):
            if(color[v[0] -1][v[1]] == 0 and visited[v[0] -1][v[1]] == 0):
                neighbors.append([v[0] - 1, v[1]])
                visited[v[0] - 1][v[1]] = 1
            if(color[v[0] +1][v[1]] == 0 and visited[v[0] +1][v[1]] == 0):
                neighbors.append([v[0] + 1, v[1]])
                visited[v[0] + 1][v[1]] = 1
            if(color[v[0]][v[1]+1] == 0 and visited[v[0]][v[1]+1] == 0):
                neighbors.append([v[0], v[1] + 1])
                visited[v[0]][v[1] + 1] = 1

        elif(v[1] == n-1):
            if(color[v[0] -1][v[1]] == 0 and visited[v[0] -1][v[1]] == 0):
                neighbors.append([v[0] - 1, v[1]])
                visited[v[0] - 1][v[1]] = 1
            if(color[v[0] +1][v[1]] == 0 and visited[v[0] +1][v[1]] == 0):
                neighbors.append([v[0] + 1, v[1]])
                visited[v[0] + 1][v[1]] = 1
            if(color[v[0]][v[1]-1] == 0 and visited[v[0]][v[1]-1] == 0):
                neighbors.append([v[0], v[1] - 1])
                visited[v[0]][v[1] - 1] = 1    

    elif(v[0] == 0):
        if(v[1] != 0 and v[1] != n-1):
            if(color[v[0]][v[1] + 1] == 0 and visited[v[0]][v[1] + 1] == 0):
                neighbors.append([v[0] , v[1] + 1])
                visited[v[0]][v[1]+1] = 1
            if(color[v[0] +1][v[1]] == 0 and visited[v[0] +1][v[1]] == 0):
                neighbors.append([v[0] + 1, v[1]])
                visited[v[0] + 1][v[1]] = 1
            if(color[v[0]][v[1]-1] == 0 and visited[v[0]][v[1]-1] == 0):
                neighbors.append([v[0], v[1] - 1])
                visited[v[0]][v[1] - 1] = 1            

        elif(v[1] == 0):
            if(color[v[0]][v[1] + 1] == 0 and visited[v[0]][v[1] + 1] == 0):
                neighbors.append([v[0] , v[1] + 1])
                visited[v[0]][v[1]+1] = 1
            if(color[v[0] +1][v[1]] == 0 and visited[v[0] +1][v[1]] == 0):
                neighbors.append([v[0] + 1, v[1]])
                visited[v[0] + 1][v[1]] = 1

        elif(v[1] == n-1):
            if(color[v[0]][v[1] - 1] == 0 and visited[v[0]][v[1] - 1] == 0):
                neighbors.append([v[0] , v[1] - 1])
                visited[v[0]][v[1]-1] = 1
            if(color[v[0] +1][v[1]] == 0 and visited[v[0] +1][v[1]] == 0):
                neighbors.append([v[0] + 1, v[1]])
                visited[v[0] + 1][v[1]] = 1

    elif(v[0] == n-1):
        if(v[1] != 0 and v[1] != n-1):
            if(color[v[0]][v[1] + 1] == 0 and visited[v[0]][v[1] + 1] == 0):
                neighbors.append([v[0] , v[1] + 1])
                visited[v[0]][v[1]+1] = 1
            if(color[v[0] -1][v[1]] == 0 and visited[v[0] -1][v[1]] == 0):
                neighbors.append([v[0] - 1, v[1]])
                visited[v[0] - 1][v[1]] = 1
            if(color[v[0]][v[1]-1] == 0 and visited[v[0]][v[1]-1] == 0):
                neighbors.append([v[0], v[1] - 1])
                visited[v[0]][v[1] - 1] = 1            

        elif(v[1] == 0):
            if(color[v[0]][v[1] + 1] == 0 and visited[v[0]][v[1] + 1] == 0):
                neighbors.append([v[0] , v[1] + 1])
                visited[v[0]][v[1]+1] = 1
            if(color[v[0] -1][v[1]] == 0 and visited[v[0] -1][v[1]] == 0):
                neighbors.append([v[0] - 1, v[1]])
                visited[v[0] - 1][v[1]] = 1

        elif(v[1] == n-1):
            if(color[v[0]][v[1] - 1] == 0 and visited[v[0]][v[1] - 1] == 0):
                neighbors.append([v[0] , v[1] - 1])
                visited[v[0]][v[1]-1] = 1
            if(color[v[0] -1][v[1]] == 0 and visited[v[0] -1][v[1]] == 0):
                neighbors.append([v[0] - 1, v[1]])
                visited[v[0] - 1][v[1]] = 1

    return neighbors


update = True
currentLevel = 0
levelQueue = [[u]]
while(update):
    update = False
    for currentVertex in range(0, len(levelQueue[currentLevel])):
        levelQueue.append([])
        v = levelQueue[currentLevel][currentVertex]
        for i in unvisitedNeighborList(v):
            update = True
            levelQueue[currentLevel + 1].append(i)
            totVisits += 1
    currentLevel += 1    

if(totVisits == n*n - totB):
    print("Y")
else:
    print("N")    


