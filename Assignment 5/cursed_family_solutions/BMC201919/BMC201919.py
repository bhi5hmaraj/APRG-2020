n=int(input())
graph=dict()
lmao=[0 for i in range(0,n)]
for i in range(0,n):
    graph[i+1]=[]
for i in range(0,n-1):
    a= list(map(int,input().split()))
    graph[a[0]].append(a[1])
    lmao[a[1]-1]=1
eh=[-1 for i in range(0,n+1)]
def dp(i):
    if(eh[i-1] != -1):
        return eh[i-1]
    if(not graph[i]):
        eh[i-1] = 1
        return eh[i-1]
    if(graph[i]):
        x=0
        y=1
        for j in graph[i]:
            x += dp(j)
        for j in graph[i]:
            if(graph[j]):
                for k in graph[j]:
                    y += dp(k)
        eh[i-1] = max(x,y)
        return eh[i-1]

l=0
for i in range(0,n):
    if(lmao[i] != 1):
        l=i
print(dp(l+1))


       
          
       