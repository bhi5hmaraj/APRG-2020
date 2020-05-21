from queue import Queue

N, M = map(int, input().split())
Start, End = map(int, input().split())

Amatrix = []
shortest_Start = []
shortest_End = []
minimum = []
status = []
for i in range(N + 1):
    Amatrix.append([])
    shortest_Start.append(-1)
    shortest_End.append(-1)
    minimum.append(None)
    status.append(0)
for i in range(M):
    a, c, b = map(str, input().split())
    a, b = int(a), int(b)
    Amatrix[a].append([b , c])
    Amatrix[b].append([a , c])

def LexicoBFS(source):
    queue = Queue()
    if source == Start:
        shortest_Start[source] = 0
    else:
        shortest_End[source] = 0
    queue.put(source)
    while (queue.empty() == 0):
        element = queue.get()
        for i in range(len(Amatrix[element])):
            j = Amatrix[element][i][0]
            if source == Start:
                if(shortest_Start[j] == -1):
                    shortest_Start[j] = 1 + shortest_Start[element]
                    queue.put(j)
            else:
                if(shortest_End[j] == -1):
                    shortest_End[j] = 1 + shortest_End[element]
                    queue.put(j)
LexicoBFS(Start)
LexicoBFS(End)

def Min_List():
    for i in range(N + 1):
        if i == 0:
            continue
        if(shortest_Start[i] + shortest_End[i] == shortest_Start[End]):
            temporary = None
            for j in range(len(Amatrix[i])):
                k = Amatrix[i][j][0]
                l = Amatrix[i][j][1]
                if (shortest_Start[i] + 1 + shortest_End[k] == shortest_Start[End]):
                    if (temporary == None):
                        temporary = l
                    elif (l < temporary):
                        temporary = l
            minimum[i] = temporary
Min_List()

def LexyPath():
    path = ""
    Traversed = [Start]
    Empty = []
   
    while(len(Traversed) != 0):
        temporary = None
        count = 0
        for i in range(len(Traversed)):
            if(temporary == None or temporary > minimum[Traversed[i]]):
                temporary = minimum[Traversed[i]]
        path = path + temporary
        for i in range(len(Traversed)):
            if(minimum[Traversed[i]] == temporary):
                for j in range(len(Amatrix[Traversed[i]])):
                    node = Amatrix[Traversed[i]][j][0]
                    q = Amatrix[Traversed[i]][j][1]
                    if(node == End):
                        count = 1
                        break
                    if(shortest_Start[Traversed[i]] + 1 + shortest_End[node] == shortest_Start[End] and q == temporary and status[node] == 0):
                        status[node] = 1
                        Empty.append(node)
        if(count):
            break
        Traversed = Empty
        Empty = []
    return path
if(Start == End):
    print("")
else:
    print(LexyPath())