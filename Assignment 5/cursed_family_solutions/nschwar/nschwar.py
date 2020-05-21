from collections import defaultdict
def indep(i):
    while(i!=0):
        for x in generation[i]:
            if children[x]==[]:
                val1[x]=1
            else:
                for j in children[x]:
                    val1[x]=val1[x]+val1[j]
                    if children[j]!=[]:
                        for t in children[j]:
                            val2[x]=val2[x]+val1[t]
            val1[x]=max(val1[x],val2[x])
        i=i-1
n=int(input())
children=defaultdict(list)
generation=defaultdict(list)
marked=[0]*(n+1)
val1=[0]*(n+1)
val2=[1]*(n+1)
for j in range(n-1):
    u,v=map(int,input().split())
    children[u].append(v)
    marked[v]=1
for j in range(1,n+1):
    if marked[j]==0:
        break
generation[1]=[j]
i=1
while(True):
    i=i+1
    for t in generation[i-1]:
        generation[i].extend(children[t])
    if generation[i]==[]:
        break
indep(i-1)
print(val1[j])
