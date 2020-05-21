listDim = list(map(int, input().split()))
M=listDim[0]
N=listDim[1]

X = []
for i in range(0,M):
     X.append(list(input()))

def minesweeper(M,N,X):
    for i in range(0,M):
        for j in range(0,N):
            if X[i][j] != '*':
                X[i][j] = int(0)
    for i in range(0,M):
        for j in range(0,N):
            if X[i][j] == '*':
                if j-1>=0 and X[i][j-1]!='*':
                    X[i][j-1]=X[i][j-1]+1
                if j+1<N and X[i][j+1]!='*':
                    X[i][j+1]=X[i][j+1]+1
                if i-1>=0:
                    if X[i-1][j]!='*':
                        X[i-1][j]=X[i-1][j]+1
                    if j-1>=0 and X[i-1][j-1]!='*':
                        X[i-1][j-1]=X[i-1][j-1]+1    
                    if j+1<N and X[i-1][j+1]!='*':
                        X[i-1][j+1]=X[i-1][j+1]+1
                if i+1<M:
                    if X[i+1][j]!='*':
                        X[i+1][j]=X[i+1][j]+1
                    if j-1>=0 and X[i+1][j-1]!='*':
                        X[i+1][j-1]=X[i+1][j-1]+1    
                    if j+1<N and X[i+1][j+1]!='*':
                        X[i+1][j+1]=X[i+1][j+1]+1
    return(X)

for i in range(0,M):
    print(''.join(map(str,minesweeper(M,N,X)[i])))
