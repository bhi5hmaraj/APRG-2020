from queue import Queue

#size and number of black nodes
line = list(input().split())
N = int(line[0])
b = int(line[1])

#initial position
line = list(input().split())
init1 = int(line[0])
init2 = int(line[1])

#making the grid, 0 will a white node , 1 will mean a black node
#and 2 will mean a colored node 
grid = []
for i in range(N):
    grid.append([])
    for j in range(N):
        grid[i].append(0)
for i in range(b):
    line = list(input().split())
    grid[int(line[0]) - 1][int(line[1]) - 1] = 1

#bfs
def bfs(x , y):
    queue = Queue()
    queue.put((x , y))
    grid[x][y] = 2
    while (queue.empty() != 1):
        pair = queue.get()
        i = pair[0]
        j = pair[1]
        if (j - 1 >= 0 and grid[i][j - 1] == 0):
            grid[i][j - 1] = 2
            queue.put((i , j - 1))
        if (j + 1 < N and grid[i][j + 1] == 0):
            grid[i][j + 1] = 2
            queue.put((i , j + 1))
        if (i - 1 >= 0 and grid[i - 1][j] == 0):
            grid[i - 1][j] = 2
            queue.put((i - 1 , j))
        if (i + 1 < N and grid[i + 1][j] == 0):
            grid[i + 1][j] = 2
            queue.put((i + 1 , j))
bfs(init1 - 1 , init2 - 1)

#final check
flag = 0
for i in range(N):
    for j in range(N):
        if(grid[i][j] == 0):
            flag = 1
            break
    if flag: 
        print("N")
        break
if (not flag):
    print("Y")