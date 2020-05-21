from collections import defaultdict
black="black"
green="green"
white="white"
def fillcolor(A,i,j):
    bfs(A,i,j)
    for x in range(1,n+1):
        for y in range(1,n+1):
            if(A[x][y]==white):
               return "N"
    return "Y"
def bfs(A,i,j):
    q=[]
    q.append((i,j))
    A[i][j]=green
    while q!=[]:
        s=q.pop(0)
        if(A[s[0]-1][s[1]]==white):
            A[s[0]-1][s[1]]=green
            q.append((s[0]-1,s[1]))
        if(A[s[0]+1][s[1]]==white):
            A[s[0]+1][s[1]]=green
            q.append((s[0]+1,s[1]))
        if(A[s[0]][s[1]+1]==white):
            A[s[0]][s[1]+1]=green
            q.append((s[0],s[1]+1))
        if(A[s[0]][s[1]-1]==white):
            A[s[0]][s[1]-1]=green
            q.append((s[0],s[1]-1))
        else:
            continue
n,b=map(int,input().split())
i,j=map(int,input().split())
A=defaultdict(list)
for m in range(n+2):
    for l in range(n+2):
        if(m==0 or m==n+1):
            A[m].append(black)
        elif(l==0 or l==n+1):
            A[m].append(black)
        else:
            A[m].append(white)
for m in range(b):
    a1,b1=map(int,input().split())
    A[a1][b1]=black
print(fillcolor(A,i,j))
