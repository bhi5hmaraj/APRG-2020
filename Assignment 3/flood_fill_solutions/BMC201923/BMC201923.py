from queue import Queue

n,s=list(map(int,input().split()))
a,b=list(map(int,input().split()))
a-=1
b-=1

mat = [[0] * n for i in range(n)]

for i in range(0,s):
    x,y=list(map(int,input().split()))
    x-=1
    y-=1
    mat[x][y]=1
def chk(i,j):
    if i < 0 or j < 0 or i >= n or j >= n:
        return False
    if mat[i][j]==1:
        return False
    mat[i][j]=1
    return True

def fill(x,y):
    q = Queue()
    q.put((x,y))
    mat[x][y]=1
    
    while not q.empty():
        i,j=q.get()
        if chk(i+1,j):
            q.put((i+1,j))
        if chk(i,j+1):
            q.put((i,j+1))
        if chk(i-1,j):
            q.put((i-1,j))
        if chk(i,j-1):
            q.put((i,j-1))
    return

fill(a,b)
if sum(list(map(sum,mat)))==(n*n):
    print("Y")
else:
    print("N")
