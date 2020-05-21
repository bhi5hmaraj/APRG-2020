n,m = map(int , raw_input().split(' '))
arr = []
for i in range(0 , n):
    x = raw_input()
    arr.append(x)
for i in range(0 , n):
    res = ""
    for j in range(0 , m):
        if arr[i][j] == '*':
            res += "*"
        else:
            cnt = 0
            for k in range(-1 , 2):
                for l in range(-1 , 2):
                    x = k + i
                    y = l + j
                    if x >= 0 and x < n and y >= 0 and y < m:
                        if arr[x][y] == '*':
                            cnt += 1
            res += str(cnt)
    print res
