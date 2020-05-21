x = list(map(int,input().split()))
n = x[0]
m = x[1]
matrix = [['.']*(m+2)] 
for i in range(n):
    matrix.append(['.']+list(input())+['.'])
matrix.append(['.']*(m+2))
# print(matrix)
for i in range(1,m+1):
    for j in range(1,n+1):
        z = 0
        if matrix[j][i] == '*':
            continue
        for p in range((i-1),(i+2)):
            for q in range((j-1),(j+2)):
                if matrix[q][p] == '*':
                    z += 1
        matrix[j][i] = str(z)
for i in range(1,n+1):
    print(''.join(matrix[i][1:m+1]))
