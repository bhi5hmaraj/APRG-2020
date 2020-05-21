trans = [(i,j) for i in [-1,0,1] for j in [-1,0,1]]
[m,n] = list(map(int,input().split()))
ground = ['.'*(n+2)]
for i in range(m):
        row = input()
        ground.append("."+row+".")
ground.append('.'*(n+2))
c = [[0 for i in range(n+2)] for j in range(m+2)]
for i in range(1,m+1):
    for j in range(1,n+1):
        if ground[i][j] == '*': c[i][j] = "*"
        else:
            for (x,y) in trans:
                if ground[i+x][j+y] == '*': c[i][j] += 1
for i in range(1,m+1): print(''.join(map(str,c[i][1:-1])))
