n=(int)(input())

parent=[n+1 for i in range(n)]
child=[[] for i in range(n)]
count=[i for i in range(n)]
depth=[0 for i in range(n)]
deep=[(0,0) for i in range(n)]
c=[0 for i in range(n)]
for i in range(n-1):
    u,v = map(int,input().split())
    parent[v-1]=u-1
    child[u-1].append(v-1)
    c[u-1]=1
    count[v-1]=-1
    
for i in range(n):
    if count[i]!=-1:
        a=i
        break
deep[a]=(0,a)
queue=[a]
while(queue):
    z=queue.pop(0)
    for i in child[z]:
        deep[i]=(deep[z][0]+1,i)
        queue.append(i)
        
deep.sort()
#print(deep)
    

for i in range(n-1):
    z=deep[-1][1]

    if depth[parent[z]]==0 or (depth[z]%2==0 and depth[parent[z]]%2==0):
        depth[parent[z]]=depth[z]+1
    
    deep.pop(-1)
s=0        
for i in range(n):
    if depth[i]%2==0:
        s=s+1

#print(depth)        
print(s)