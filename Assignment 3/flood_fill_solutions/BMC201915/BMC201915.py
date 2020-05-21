N, b = list(map(int, (input().split())))
si, sj = list(map(int, (input().split())))
ar = [[0 for i in range(N)] for j in range(N)]
for i in range(b):
    x, y = list(map(int, input().split()))
    ar[x-1][y-1] = 1                   # 0 for white, 1 for black, 2 for blue
ar[si-1][sj-1] = 2
si -= 1
sj -= 1
def valid(arr):
    temp = []
    for i in arr:
        if i[0] in range(N) and i[1] in range(N):
            temp.append(i)
    return temp
def neighbour(i, j):
    return valid([[i+1,j] ,[i-1,j] ,[i,j-1], [i,j+1]])
visited = [[0 for i in range(N)] for j in range(N)]
queue = [[si, sj]]
visited[si][sj] = True
while queue:
    s = queue.pop(0)
    for i in neighbour(s[0],s[1]):
        if not visited[i[0]][i[1]] :   # ex i = [2,3] then i[0] = 2
            if ar[i[0]][i[1]] == 0:
                ar[i[0]][i[1]] = 2
                queue.append([i[0],i[1]])
            visited[i[0]][i[1]] = True

def func():
    for i in range(N):
        for j in range(N):
            if ar[i][j] == 0:
                return False
    return True
    
if func():
    print("Y")
else :
    print("N")


            
            
            
    
    