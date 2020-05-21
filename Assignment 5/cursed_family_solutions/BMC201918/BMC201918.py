n = int(input())
children = [[] for _ in range(n+1)]
parent = [0]*(n+1)
for _ in range(n-1):
    p, c = map(int, input().split())
    children[p].append(c)
    parent[c] = p

dp = [[-1]*(n+1) for _ in range(2)]

def f(t, r):
    if dp[t][r] == -1:
        s = t
        if t:
            for v in children[r]:
                s += f(0, v)
        else:
            for v in children[r]:
                s += max(f(0, v), f(1, v))
        dp[t][r] = s
    return dp[t][r]

i = 1
while parent[i] != 0:
    i = parent[i]

print(max(f(0, i), f(1, i)))