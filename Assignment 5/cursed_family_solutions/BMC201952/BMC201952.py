from collections import defaultdict
n = int(input())
Fam_parent = [0]*(n+1)
Fam_children = defaultdict(list)
for i in range(n-1):
    u, v = map(int, input().split())
    Fam_parent[v] = u
    Fam_children[u].append(v)
Fam_parent[0] = n+1
rootFather = Fam_parent.index(0)
start = [rootFather]
FamTreeLevels = []
while start:
    treebuilder = []
    FamTreeLevels.append(start[:])
    for node in start:
        treebuilder.extend(Fam_children[node])
    start = treebuilder[:]
MaxIndSet = [0]*(n+1)
while FamTreeLevels:
    recentlevel = FamTreeLevels.pop()
    for child in recentlevel:
        (x, y) = (1,0)
        for grandchild in Fam_children[child]:
            x += MaxIndSet[grandchild][1]
            y += max(MaxIndSet[grandchild])
        MaxIndSet[child] = (x, y)
FinalAns = max(MaxIndSet[rootFather])
print(FinalAns)