n = int(input()) # no of family members
parent = [0]*(n+1)
children = [[]for i in range(n+1)]
u = 0
for i in range(n-1):
    u, v = map(int, input().split())
    children[u].append(v)
    parent[v] = u
while parent[u]!= 0:
    u = parent[u]
def nextGen(lis):
    temp = []
    for i in lis:
        for j in children[i]:
            temp.append(j)
    return temp
gen = [[u]]
T = [1 for i in range(n+1)]
while nextGen(gen[-1]) != []:
    gen.append(nextGen(gen[-1]))
g = len(gen)
def sumAllGrandChildren(j):
    temp =[]
    for i in children[j]:
        for k in children[i]:
            temp.append(k)
    if temp==[]:
        return 0
    ans = 0
    for i in temp:
        ans += T[i]
    return ans
def sumAllChildren(j):
    if children[j]==[]:
        return 0
    ans = 0
    for i in children[j]:
        ans += T[i]
    return ans
for i in range(g-1, -1, -1):
    if i == g-1:
        for j in gen[-1]:
            T[j] = 1
    else:
        for j in gen[i]:
            if children[j]==[]:
                T[j] = 1
            # T[j] = all children c of children[node] T[c] + 1, all children c of node T[c]
            
            else:
                T[j] = max(sumAllGrandChildren(j) + 1, sumAllChildren(j))
print(T[u])
