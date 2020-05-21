n_m =  [int(x) for x in input().split()]
n = n_m[0]
m =  n_m[1]
start = [int(x) for x in input().split()]
blackpixl = []
for i in range(m):
    blackpixl.append(list(map(int, input().split())))
pixl_map = [[1]*(n+2)] + [[1] + [0]*n + [1] for i in range(n)] + [[1]*(n+2)]
for sink, source in blackpixl:
    pixl_map[sink][source] = 1

def fill(pixelmap, r, c):
    queue = [(r, c)]
    while queue != []:
        x, y = queue.pop(0)
        if pixelmap[x][y] == 0:
            pixelmap[x][y] = "#"
            if pixelmap[x - 1][y] == 0:
                queue.append((x-1, y))
            if pixelmap[x][y - 1] == 0:
                queue.append((x, y-1))
            if pixelmap[x + 1][y] == 0:
                queue.append((x+1,y))
            if pixelmap[x][y + 1] == 0:
                queue.append((x, y+1))
    return pixelmap

fill(pixl_map, start[0], start[1])

def isfilled(pixelmap):
    if (any(0 in x for x in pixelmap)):
        print("N")
    else:
        print("Y")
isfilled(pixl_map)

