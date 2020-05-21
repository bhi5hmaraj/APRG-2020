def floodfill(grid, x, y, n):
    color = []
    color.append((x,y))
    while len(color) != 0:
        (a,b) = color.pop()
        grid[a][b] = "green"
        if a > 0:
            if grid[a-1][b] == "white":
                color.append((a-1,b))
        if a < n-1:
            if grid[a+1][b] == "white":
                color.append((a+1,b))
        if b > 0:
            if grid[a][b-1] == "white":
                color.append((a,b-1))
        if b < n-1:
            if grid[a][b+1] == "white":
                color.append((a,b+1))


s = str(input()).split()
n = int(s[0])
b = int(s[1])

s = str(input()).split()
start_x = int(s[0]) - 1
start_y = int(s[1]) - 1

black_nodes = []
for i in range(b):
    s = str(input()).split()
    x = int(s[0]) - 1
    y = int(s[1]) - 1
    black_nodes.append([x,y])

if n == 1:
    print("Y")
    exit()

grid = [["white" for i in range(n)] for j in range(n)] 
for i in range(b):
    x = black_nodes[i][0]
    y = black_nodes[i][1]
    grid[x][y] = "black"

floodfill(grid, start_x, start_y, n)

for i in range(n):
    for j in range(n):
        if grid[i][j] == "white":
            print("N")
            exit()

print("Y")