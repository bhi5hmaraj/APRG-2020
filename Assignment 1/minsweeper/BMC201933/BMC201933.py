x = list(map(int, input().split()))
m = x[0]
n = x[1]
a = [[0 for i in range(n+2)] for j in range(m+2)]
p = [[]]
p = []
for i in range(m):
    p.append(list(input()))

for i in range(m):
    for j in range(n):
        if p[i][j] == '*':
            a[i+1][j+1] = '*'
            for k in range(i,i+3):
                for l in range(j,j+3):
                    if a[k][l] == '*':
                        a[k][l] = '*'
                    else: 
                        a[k][l]= a[k][l] + 1
y = [[] for i in range(m+1)]
                    
for i in range(1,m+1):
    print(''.join(str(a[i][j]) for j in range(1,n+1)))
