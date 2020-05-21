n, m = input().split();
n = int(n)
m = int(m)
A = []
for i in range(n+2):
    b = []
    for j in range(m+2):
        b.append(0)
    A.append(b)
B = []
for i in range(1,n+1):
    x = input()
    for j in range(1, m+1):
        if(x[j-1] == '*'):
            A[i-1][j-1] += 1
            A[i-1][j] += 1
            A[i-1][j+1] += 1
            A[i][j-1] += 1
            A[i][j+1] += 1
            A[i+1][j-1] += 1
            A[i+1][j] += 1
            A[i+1][j+1] += 1
    B.append(x)
for i in range(0,n):
    for j in range(m):
        if(B[i][j] == '*'):
            A[i+1][j+1] = '*'
            
for i in range(1,n+1):
    print(''.join(str(x) for x in A[i][1:m+1]))


            
        

