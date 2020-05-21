n = int(input())

adj = [[] for i in range(n+1)]
np =[0 for i in range(n+1)]
p = 0

for _ in range(n-1):
    x,y  = map(int, input().split())
    adj[x].append(y)
    np[y] = 1
for i in range(1,n+1):
    if np[i] == 0:
        p = i
        break

dp =  [[-1,-1] for i in range(n+1)]

def func(n,f):
    if(len(adj[n]) ==0):
        if f== 1:
            return 1
        else:
            return 0
    if(dp[n][f] == -1):
        ans = 0
        for u in adj[n]:
            if(f == 1):
                ans += func(u,0)
            else:
                ans += max(func(u,1),func(u,0))
        if f == 1:
            ans +=1
        dp[n][f] = ans
    return dp[n][f]

print(max(func(p,0),func(p,1)))         
    


