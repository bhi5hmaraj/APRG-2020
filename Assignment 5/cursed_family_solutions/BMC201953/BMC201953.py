import sys
sys.setrecursionlimit(1000000000)

#taking the input
n = int(input())

#setting the tree
tree = [[]]
maxgather = [-1]
par = [-1]
for i in range(n):
    tree.append([])
    maxgather.append(-1)
    par.append(-1)
#taking the edges
for i in range(n - 1):
    inp = list(input().split())
    u , v = int(inp[0]) , int(inp[1])
    tree[u].append(v)
    par[v] = u
for i in range(1 , n + 1):
    if(par[i] == -1):
        root = i
        break

#solving maxgather for leaves
for i in range(1 , n + 1):
    if(len(tree[i]) == 0):
        maxgather[i] = 1

#top-down dp
def compMaxGather(v):
    if (maxgather[v] != -1):
        return maxgather[v]
    temp1 = 0
    temp2 = 1
    for i in range(len(tree[v])):
        neig = tree[v][i]
        p = compMaxGather(neig)
        temp1 = temp1 + p
        for j in range(len(tree[neig])):
            neig1 = tree[neig][j]
            p = compMaxGather(neig1)
            temp2 = temp2 + p
    maxgather[v] = max(temp1 , temp2)
    return maxgather[v]
print(compMaxGather(root))