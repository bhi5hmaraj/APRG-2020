
inNM = list(map(int, input().split()))
n = inNM[0]
m = inNM[1]

inXY = list(map(int, input().split()))
X = inXY[0] - 1
Y = inXY[1] - 1

AdList = []
AdListRank = []
for i in range(0, n):
    AdList.append([])
    AdListRank.append([])

for i in range(0, m):
    inUV = list(input().split())
    AdList[int(inUV[0]) - 1].append(int(inUV[2]) - 1)
    AdList[int(inUV[2]) - 1].append(int(inUV[0]) - 1) 
    AdListRank[int(inUV[0]) - 1].append(inUV[1])
    AdListRank[int(inUV[2]) - 1].append(inUV[1])

# print("*******")
levelQueue = [[X]]
levelTracker = []
for i in range(0, n):
    levelTracker.append(-2)
levelTracker[X] = 0

visited = 1
update = True
currentLevel = 0
while(update):
    update = False
    for currentVertex in range(0, len(levelQueue[currentLevel])):
        levelQueue.append([])
        v = levelQueue[currentLevel][currentVertex]
        for i in range(0, len(AdList[v])):
            if(levelTracker[AdList[v][i]] == -2):
                update = True
                levelQueue[currentLevel + 1].append(AdList[v][i])
                levelTracker[AdList[v][i]] = currentLevel + 1
    currentLevel += 1

level = levelTracker[Y]
accounted = []
for i in range(0, n):
    accounted.append(False)

accounted[Y] = True

def neighbours(u, v):
    for i in range(0, len(AdList[u])):
        if(AdList[u][i] == v):
            return True
    return False

relevantLevels = []
for i in range(0, levelTracker[Y] + 1):
    relevantLevels.append([])

relAdList = []
relRanks = []
for i in range(0, n):
    relAdList.append([])
    relRanks.append([])

relevantLevels[level].append(Y) 
while(level > 0):
    for j in range(0, len(relevantLevels[level])):
        for i in range(0, len(AdList[relevantLevels[level][j]])):
            if(levelTracker[AdList[relevantLevels[level][j]][i]] == (level - 1)):
                relAdList[AdList[relevantLevels[level][j]][i]].append(relevantLevels[level][j])
                relRanks[AdList[relevantLevels[level][j]][i]].append(AdListRank[relevantLevels[level][j]][i])
                if(accounted[AdList[relevantLevels[level][j]][i]] == False):
                    accounted[AdList[relevantLevels[level][j]][i]] = True
                    relevantLevels[level - 1].append(AdList[relevantLevels[level][j]][i])
    level -= 1

'''for i in range(0, len(relAdList)):
    for j in range(0, len(relAdList[i])):
        print(i+1, relRanks[i][j], relAdList[i][j] + 1)'''

# for i in range(0, n):
#     for j in range(0, len(relAdList[i])):
#         print(i+1, relAdList[i][j] + 1, relRanks[i][j])

toPrint = ""
activeVertices = [X]
nextInLine = []
level = 0
visitTrack = []
for i in range(0, n):
    visitTrack.append(0)

while(level < levelTracker[Y]):
    min = "z"
    edits = 1
    for j in range(0, len(activeVertices)):
        for i in range(0, len(relAdList[activeVertices[j]])):
            if(relRanks[activeVertices[j]][i] < min):
                nextInLine = []
                min = relRanks[activeVertices[j]][i]
                edits += 1
            if(relRanks[activeVertices[j]][i] == min and not(visitTrack[relAdList[activeVertices[j]][i]] == edits)):
                nextInLine.append(relAdList[activeVertices[j]][i])
                visitTrack[relAdList[activeVertices[j]][i]] = edits

    toPrint += min
    # for i in range(0, len(activeVertices)):
    #     print(level, activeVertices[i] + 1)
    activeVertices = nextInLine
    nextInLine = []
    level += 1

print(toPrint)







