n = input()
n = int(n)
tree = {}
parent = {}
for i in range(n):
    tree.update({(i + 1) : []})
for i in range(n - 1):
    [x, y] = input().split()
    x = int(x)
    y = int(y)
    list = tree[x]
    list.append(y)
    tree[x] = list
    parent.update({y: x})

dp = []
for i in range(n):
    dp.append([-1, -1])
    
def func(node, select):
    if dp[node - 1][select] != -1:
        return dp[node - 1][select]
    ans = 0
    if select == 1:
        ans = 1
        
    for i in range(len(tree[node])):
        if select == 1:
            ans = ans + func(tree[node][i], 0)
        else:
            ans = ans + max(func(tree[node][i],0),func(tree[node][i],1))
    
    dp[node - 1][select] = ans
    return ans
for i in range(n):
    if (i + 1) not in parent.keys():
        root = i+1

answer = max(func(root,0),func(root,1))
print(answer)
