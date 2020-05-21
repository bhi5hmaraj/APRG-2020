(M,N) = list(map(int,input().split()))
s=[]
for i in range(M):
    s.append(list(input()))

def c_mine(i,j):
    if s[i][j] =='.':
        sm=0
        for p in range(i-1,i+2):
            for q in range(j-1,j+2):
                    if p < M and p >= 0 and q < N and q >= 0:
                        if s[p][q] == '*':
                            sm = sm + 1
        return(sm)
    else:
        return('*')

for i in range(M):
    for j in range(N):
        print(c_mine(i,j),end='')
    print()
