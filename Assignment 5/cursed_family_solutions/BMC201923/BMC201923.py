n=int(input())
tree=[]
for i in range(n):
    tree.append([])

for i in range(n-1):
    u,v=list(map(int,input().split()))
    u-=1
    v-=1
    tree[u].append(v)
    tree[v].append(u)
dp={}

def dfs(u,p,take):
    if (u,p,take) in dp:
        return dp[(u,p,take)]
    
    ans=int(take)
    for v in tree[u]:
        if v != p:
            if take == True:
                ans+=dfs(v,u,False)
            else:
                ans+=max(dfs(v,u,True),dfs(v,u,False))
    dp[(u,p,take)]=ans
    return ans

print(max(dfs(0,0,True),dfs(0,0,False)))
