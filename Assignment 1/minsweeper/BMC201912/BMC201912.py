def getl():
    s = str(input())
    l = s.split()
    return list(map(int, l))

l1 = getl()
m = l1[0]
n = l1[1]

def load():
    mat = [[0 for y in range(n+2)] for x in range(m+2)]
    for i in range(m):
        s = str(input())
        for j in range(n):
            if (s[j] == '*'):
                mat[i+1][j+1] = 1
    return mat

mat = load()
def calc():
    nat = [0 for x in range(m)]
    for i in range(m):
        s = ""
        for j in range(n):
            if (mat[i+1][j+1] == 1):
                s = s+"*"
            else:
                su = 0
                for x in [i, i+1, i+2]:
                    for y in [j, j+1, j+2]:
                        su += mat[x][y]
                s = s + str(su)
        nat[i] = s
    return nat
ans = calc()
for i in ans:
    print(i)
