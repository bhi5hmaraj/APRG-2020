
m, n = input().split()
  
m = int(m)
n = int(n)

_map = []


for i in range(0, m):
    _map.append(list(input()))


def minef(l):
    for i in range(0, m):
        for j in range(0, n):
            if l[i][j] != '*':
                a = 0
                if (i-1) >= 0:
                    if l[(i-1)][(j-1)] == '*' and (j-1) >= 0 :
                        a += 1
                    if l[(i-1)][(j)] == '*':
                        a += 1
                    if l[(i-1)][(j+1) % n] == '*' and (j+1) < n:
                        a += 1
                if l[(i)][(j-1)] == '*' and (j-1) >= 0:
                    a += 1
                if l[(i)][(j+1) % n] == '*'  and (j+1) < n:
                    a += 1

                if (i+1) < m:
                    if l[(i+1) ][(j-1)] == '*' and (j-1) >= 0:
                        a += 1
                    if l[(i+1) ][(j)] == '*':
                        a += 1
                    if l[(i+1) ][(j+1) % n] == '*'  and (j+1) < n:
                        a += 1

                l[i][j] = a            

    return l


for i in minef(_map):
    printmap = ""
    for j in i:
        printmap += str(j)
    print(printmap)



