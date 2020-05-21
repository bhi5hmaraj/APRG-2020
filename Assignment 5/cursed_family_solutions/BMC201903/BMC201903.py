n = int(input())
family={}
for i in range(1,n+1):
    family[i]=[]
papa={}
for i in range(1,n+1):
    papa[i]=[]




for i in range((n-1)):
    x = input().split()
    u = int(x[0])
    v = int(x[1])
    family[u].append(v)
    papa[v].append(u)

dp = {}
for i in range(1,n+1):
    dp[i]=0

def independent():
    for vertex  in family:
        if family[vertex]==[]:
            dp[vertex]=1
        else:
            i1 =0
            i2=0
            for no in family[vertex] :
                i1 = i1 + dp[no]
            for t in family[vertex]:
                if family[t]==[]:
                    i2 =i2
                else:
                    for m in family[t]:
                        i2 =i2 + dp[m]

            dp[vertex]=max(i1,1+i2)

    return dp

for pop in papa:
    if papa[pop]==[]:
        root = pop

while dp[root] != independent()[root]:
    dp = independent()

print((dp[root]))