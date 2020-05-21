li1 = list(map(int, input().split()))
n = li1[0]
b = li1[1]
x = list(map(int, input().split()))
x = [x[0] - 1, x[1] - 1]
q = []
q.append(x)
mark = [[0 for i in range(n)] for i in range(n)]
q1 = []
c = n*n - 1
for i in range(b):
    li = list(map(int, input().split()))
    if mark[li[0]-1][li[1]-1] == 0:
        mark[li[0]-1][li[1]-1] = 1
        q1.append([li[0]-1,li[1]-1])
        c = c-1
    
def floodfill(x, q1 , c):
    q = []
    q.append(x)
    if q1 == []:
        return 'Y'
    
    mark[x[0]][x[1]] = 1
    while q != []:
        v = q[0]
        for i in [-1,1]:
            if n>q[0][0] + i >-1:
                    if mark[q[0][0] + i][q[0][1]] == 0:
                            mark[q[0][0] + i][q[0][1]] = 1
                            q.append([q[0][0] + i,q[0][1]])
                            c = c -1
            if n> q[0][1] + i >-1:
                    if mark[q[0][0]][q[0][1] + i] == 0:
                            mark[q[0][0]][q[0][1] + i] = 1
                            q.append([q[0][0],q[0][1] + i])
                            c = c -1
            
            
        q.pop(0)
    if c>0:
        return 'N'
    else:
        return 'Y'
print(floodfill(x, q1, c))
"""    while q1 != [] :
        v = q1[0]
        for i in [-1,1]:
            if n>q1[0][0] + i >-1:
                    if mark[q1[0][0] + i][q1[0][1]] == 0:
                            return 'N'
            if n>q1[0][1] + i >-1:
                    if mark[q1[0][0]][q1[0][1] + i] == 0:
                            return 'N'
        q1.pop(0)
    return 'Y'
    

print(floodfill(x, q1))
for i in range(n):
    for j in range(n):
        print(mark[i][j])"""
    
                    
                
              