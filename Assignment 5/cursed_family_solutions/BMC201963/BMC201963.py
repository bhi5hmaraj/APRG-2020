n = int(input())
children = [[] for i in range(n)]
parentof = {}
for i in range(n-1):
    m = list(map(int, input().split()))
    children[m[0]-1].append(m[1])
    if parentof == {}:
        parentof = {m[1]}
    else:
        parentof.add(m[1])
nat = {(i+1) for i in range(n)}
s = nat.difference(parentof)
y = tuple(s)[0]
level = [0 for i in range(n)]
b = [y]
level = [0 for i in range(n)]
while b:
    t = b.pop(0)
    for i in children[(t-1)]:
        if b == []:
            b = [i]
        else:
            b.append(i)
        level[(i-1)] = level[(t-1)] + 1
def f (v):
    return(level[v-1])
vertexlist = [(i+1) for i in range(n)]
vertexlist.sort(reverse = True, key = f)
maxset = [0 for i in range(n)]
for i in vertexlist:
    if children[i-1] == []:
        maxset[i-1] = 1
    else:
        g = 0
        h = 0
        for j in children[i-1]:
            g = g + maxset[j-1]
            for k in children[j-1]:
                h = h + maxset[k-1]
        maxset[i-1] = max(1 + h,g)
print(maxset[y-1])