n, m = map(int, input().split())
A = [['.'] * (m + 2)] + [['.'] + list(input()) + ['.'] for i in range(n)] + [['.'] * (m + 2)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if A[i][j] == '*': continue
        cnt = 0
        for x in range(i - 1, i + 2):
            for y in range(j - 1, j + 2):
                if A[x][y] == '*': cnt += 1
        A[i][j] = str(cnt)

for i in range(1, n + 1):
    print(''.join(A[i][1 : m+1]))

                
