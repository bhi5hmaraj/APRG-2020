from collections import deque

def get_answer(lines):
    tmp = lines[0].split()
    n = int(tmp[0])
    b = int(tmp[1])
    tmp = lines[1].split()
    start_x = int(tmp[0])-1
    start_y = int(tmp[1])-1
    pixel_map = []
    for i in range(n):
        l = []
        for j in range(n):
            l.append([0,0])
        pixel_map.append(l)

    for i in range(b):
        tmp = lines[2+i].split()
        pixel_map[int(tmp[0])-1][int(tmp[1])-1][0] = 1

    queue = deque()
    queue.append([start_x, start_y])
    while len(queue)!=0:
        cur = queue.popleft()
        
        if pixel_map[cur[0]][cur[1]][1] == 1:
            continue
        else:
            pixel_map[cur[0]][cur[1]][1] = 1

        if cur[0] + 1 < n and pixel_map[cur[0]+1][cur[1]][0] == 0 and pixel_map[cur[0]+1][cur[1]][1] != 1:
            queue.append([cur[0]+1, cur[1]])
        if cur[0] - 1 >= 0 and pixel_map[cur[0]-1][cur[1]][0] == 0 and pixel_map[cur[0]-1][cur[1]][1] != 1:
            queue.append([cur[0]-1, cur[1]])
        if cur[1] + 1 < n and pixel_map[cur[0]][cur[1]+1][0] == 0 and pixel_map[cur[0]][cur[1]+1][1] != 1:
            queue.append([cur[0], cur[1]+1])
        if cur[1] - 1 >= 0 and pixel_map[cur[0]][cur[1]-1][0] == 0 and pixel_map[cur[0]][cur[1]-1][1] != 1:
            queue.append([cur[0], cur[1]-1])

    fill = True
    for (i,j) in [(i,j) for i in range(n) for j in range(n)]:
        if pixel_map[i][j] == [0,0]:
            fill = False
            break
    
    return "Y" if fill else "N"