n=int(input())
child={}
parent={}
grand_child={}
for i in range(n):
    child[i+1]=[]
    grand_child[i+1]=[]
    parent[i+1]=0
for i in range(n-1):
    a,b=map(int,input().split())
    child[a].append(b)
    parent[b]=a
for i in range(n):
    a=[]
    for j in child[i+1]:
        for k in child[j]:
            a.append(k)
    grand_child[i+1]=a
for root in parent:
    if parent[root]==0:
        break
level={root:0}
level_set={0:[root]}
Q=[root]
while Q:
    i=Q.pop(0)
    for j in child[i]:
        level[j]=level[i]+1
        if level[j] not in level_set:
            level_set[level[j]]=[j]
        else:
            level_set[level[j]].append(j)
        Q.append(j)
level={}
m=max(level_set)
Q=level_set[m]
while Q:
    for i in Q:
        if i not in level:
            if not child[i]:
                level[i]=1
            else:
                a=0
                b=1
                for j in child[i]:
                    a+=level[j]
                for j in grand_child[i]:
                    b+=level[j]
                level[i]=max([a,b])
    m-=1
    if m>=0:
        Q=level_set[m]
    else:
        Q=[]
print(level[root])