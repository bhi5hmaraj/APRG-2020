n = int(input())
parent= [-1 for i in range(n)]
children= [[] for i in range(n)]
for i in range(n-1):
    li = list(map(int, input().split()))
    children[li[0]-1].append(li[1]-1)
    parent[li[1]-1] = li[0]-1
for i in range(n):
    if parent[i] == -1:
        root = i
        break
l = []
depth =[0 for i in  range(n)]
l.append(root)
c = 0
m = [[] for i  in range(n)]
m[0] = [root]
while l != []:
    v = l.pop(0)
    for i in children[v]:
        depth[i] = depth[v]  + 1
        m[depth[i]].append(i)
        c =  depth[i]
        l.append(i)       
a1 = [1 for i in  range(n)]
a2 = [0 for i in range(n)]
i = c-1
while i >=0:
    for v in m[i]:
        for j in children[v]:
            a1[v] = a1[v] + a2[j]
            a2[v] = a2[v] + max(a1[j],a2[j])
    i = i-1
print(max(a1[root],a2[root]))

    