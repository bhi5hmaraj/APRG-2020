def wAdj(x, y):
    l = [(x,y)]
    def isWhite(a,b):
        if 1 <= a <= n and 1 <= b <= n and (a,b) not in blackCells:
            return True
        else:
            return False
    if isWhite(x-1,y):
        l.append((x-1,y))
    if isWhite(x+1,y):
        l.append((x+1,y))
    if isWhite(x,y-1):
        l.append((x,y-1))
    if isWhite(x,y+1):
        l.append((x,y+1))
    return l

def bfs(s):
    p ={s:0}
    q =[s]
    while q:
        wCell = q.pop(0)
        for i in wAdj(wCell[0],wCell[1]):
            if i not in p:
                p[i] = p[wCell] + 1
                q.append(i)
            else:
                continue
    return p

l1 = list(map(int,input().split()))
n = l1[0]
m = l1[1]
l2 = list(map(int,input().split()))
src = (l2[0],l2[1])
blackCells = {}
for i in range(m):
    l3 = list(map(int,input().split()))
    blackCells[(l3[0],l3[1])] = False
fList= bfs(src)
v = True
for i in range(n):
    for j in range(n):
        if (i+1,j+1) not in blackCells and (i+1,j+1) not in fList:
            v = False
            break
if v == False:
    print('N')
else:
    print('Y')
        
