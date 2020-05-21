in_list = [int(x) for x in input().split()]
n = in_list[0]
m = in_list[1]
start = [int(x) for x in input().split()]
blackpixels = []
for i in range(m):
    blackpixels.append(list(map(int, input().split())))

sqpixmap = [[1]*(n+2)] + [[1] + [0]*n + [1] for i in range(n)] + [[1]*(n+2)]

for sink, source in blackpixels:
    sqpixmap[sink][source] = 1


def floodFill(matrix, sr, sc):

    queue = [(sr, sc)]
    while queue != []:
        element = queue.pop(0)
        x = element[0]
        y = element[1]
        if matrix[x][y] == 0:
            matrix[x][y] = 2
            if matrix[x - 1][y] == 0:
                queue.append((x-1, y))
            if matrix[x][y - 1] == 0:
                queue.append((x, y-1))
            if matrix[x + 1][y] == 0:
                queue.append((x+1,y))
            if matrix[x][y + 1] == 0:
                queue.append((x, y+1))

    return matrix

(floodFill(sqpixmap, start[0], start[1]))

def yesorno(matrix):
    if (any(0 in x for x in matrix)):
        print("N")
    else:
        print("Y")


yesorno(sqpixmap)
