def f(x):
    if x=='*':
        return 1
    else:
        return 0

n,m=[int(i) for i in input().split()]
a=[]
for i in range(m+2):
    a.append(0)
M=[a]+list(map(lambda l:[0]+l+[0],[list(map(f,list(map(str,list(input()))))) for i in range(n)]))+[a]
N=[]
for i in range(n):
    for j in range(m):
        if M[i+1][j+1]==1:
            N.append('*')
        else:
            N.append(M[i][j]+M[i][j+1]+M[i][j+2]+M[i+1][j]+M[i+1][j+2]+M[i+2][j]+M[i+2][j+1]+M[i+2][j+2])
for i in range(n):
    for j in range(i*m,(i+1)*m):
        print(N[j],end="")
    print()
