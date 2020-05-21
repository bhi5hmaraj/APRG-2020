n = int(input())
g = [[] for i in range(n)]

for _ in range(n - 1):
    u, v = [int(x) - 1 for x in input().split()]
    g[u].append(v)
    g[v].append(u)

dp = [[0, 0] for i in range(n)]

def dfs(v, p):
    sum0, sum1 = 0, 0
    for u in g[v]:
        if u != p:
            dfs(u, v)
            sum0 += dp[u][0]
            sum1 += dp[u][1]
    dp[v][0] = max(1 + sum1, sum0)
    dp[v][1] = sum0

dfs(0, -1)
print(max(dp[0][0], dp[0][1]))