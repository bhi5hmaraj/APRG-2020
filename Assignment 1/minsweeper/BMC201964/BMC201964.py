n, m = map(int, input().split())
A = []
B = []
for i in range(n):
    C = []
    for j  in range(m):
        C.append(0)
    B.append(C)
        
for i in range(n):
    A.append(input())
for i in range(n):
    for j in range(m):
        if(A[i][j] == '*'):
            B[i][j] = '*'
        else:
            if((i> 0 and j >0) and A[i-1][j-1] == '*'):
                B[i][j] += 1
            if(i> 0 and A[i-1][j] == '*'):
                B[i][j] += 1
            if((i> 0 and j<m-1) and A[i-1][j+1] == '*'):
                B[i][j] += 1
            if((j > 0) and A[i][j-1] == '*'):
                B[i][j] += 1
            if(j < m-1 and A[i][j+1] == '*'):
                B[i][j] += 1
            if((i < n-1 and j >0) and A[i+1][j-1] == '*'):
                B[i][j] += 1
            if((i < n-1) and A[i+1][j] == '*'):
                B[i][j] += 1
            if((i < n-1 and j < m-1) and A[i+1][j+1] == '*'):
                B[i][j] += 1
for i in range(n):
        print(''.join([str(elem) for elem in B[i]]))
