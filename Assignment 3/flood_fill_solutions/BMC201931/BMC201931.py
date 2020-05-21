from queue import Queue

n=list(map(int,input().split()))
m=list(map(int,input().split()))
m[0]=m[0]-1
m[1]=m[1]-1

lol = [[0] * n[0] for i in range(n[0])]

for i in range(n[1]):
    x=list(map(int,input().split()))
    x[0]=x[0]-1
    x[1]=x[1]-1
    lol[x[0]][x[1]]=1

def f(x,y):
    k = Queue()
    lol[x][y]=1
    k.put((x,y))
   
    while not k.empty():
        i,j=k.get()
        if check(i+1,j):
            k.put((i+1,j))
        if check(i,j+1):
            k.put((i,j+1))
        if check(i-1,j):
            k.put((i-1,j))
        if check(i,j-1):
            k.put((i,j-1))
    return

def check(i,j):
    if i < 0 or j < 0 or i >= n[0] or j >= n[0]:
        return False
    if lol[i][j]==1:
        return False
    lol[i][j]=1
    return True

f(m[0],m[1])
if sum(list(map(sum,lol)))==(n[0]*n[0]):
    print('Y')
else:
    print('N')