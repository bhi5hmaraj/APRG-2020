n = int(input())
father = [-1 for i in range(n)]
child = [[] for i in range(n)]
for i in range(1,n):
    l = list(map(int, input().split()))
    child[l[0]-1].append(l[1]-1)
    father[l[1]-1] = l[0]-1
for i in range(n):
    if father[i] == -1:
        root = i 
        break
y = []
dp = [0 for i in range(n)]
y.append(root)
c = 0
m = [[] for i in range(n)]
m[0] = [root]
while y != []:
    v = y.pop(0)
    for i in child[v]:
        dp[i] = dp[v] + 1
        m[dp[i]].append(i)
        c = dp[i]
        y.append(i)
l1 = [1 for i in range(n)]
l2 = [0 for i in range(n)]
i = c-1
while i >= 0:
    for v in m[i]:
        for j in child[v]:
            l1[v] = l1[v] + l2[j]
            l2[v] = l2[v] + max(l1[j],l2[j])
    i = i-1
print(max(l1[root],l2[root]))