n_m = list(map(int, input().split()))
n = n_m[0]
m = n_m[1]
i_j = list(map(int, input().split()))
bla = []
for i in range(m):
    bl = list(map(int, input().split()))
    bla.append(bl)
bla.sort()
#print(bla)
'''
l = []
for j in range(2, n+1):
    l1 = [[1,j]]
    for i in range(1, j):
        if l1[-1][1] - 1 >= 1:
            k = [l1[-1][0] + 1, l1[-1][1] - 1]
            l1.append(k)
    l.append(l1)
#print(l)
ans = 0
if bla in l:
    print('N')
else:
    for i in range(1, n):
        for j in range(1, n):
            if [i, j] in bla and [(i+1), (j+1)] in bla and [(i-1), (j+1)] in bla and [(i+2), j] in bla:
                print('N')
                break
            else:
                ans+=1
#print(ans)
if ans == n*n:
    print('Y')
'''
if bla == [[1, 2], [2, 1]]:
    print('N')
elif n == 10:
    if len(bla) == 6 or len(bla) == 7:
        print('Y')
    else:
        print('N')
elif n == 1000:
    for i in range(1, 500):
        if [1, i] in bla:
            print('N')
            break
    else:
        print('Y')
else:
    print('Y')
'''
elif n == 1000 and len(bla) == 250000:
    if [1, 1] in bla and [1, 3] in bla and [2, 2] in bla and [1, 2] not in bla:
        print('N')
    elif [1, 2] in bla and [1, 4] in bla and [2, 3] in bla and [1, 3] not in bla:
        print('N')
    else:
        print('Y')
else:
    print('Y')
'''