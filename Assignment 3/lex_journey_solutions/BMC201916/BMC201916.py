ln1 = list(map(int,input().split()))
ln2 = list(map(int,input().split()))
n,m,x,y = ln1[0], ln1[1], ln2[0], ln2[1]
li = []
for i in range(m):
    li.append(list(input().split()))
    
G = [[] for i in range(n)]
G1 = [[] for i in range(n)]
for j in range(m):
    G[int(li[j][0])-1].append(int(li[j][2]))
    G[int(li[j][2])-1].append(int(li[j][0]))
    G1[int(li[j][0])-1].append((int(li[j][2]),li[j][1]))
    G1[int(li[j][2])-1].append((int(li[j][0]),li[j][1]))
l = []
for k in range(n):
    l.append(0)
visited = l
ll = [x]
visited[x-1] = 1
while(ll):
    z = ll.pop(0)
    for i in (G[z-1]):
        if (visited[i-1] == 0):
            visited[i-1] = 1
            ll.append(i)
            l[i-1]=(l[z-1]+1)
Vis=[]
for k in range(n):
    Vis.append(0)
ll=[y]
Vis[y-1] = 1
sp = Vis.copy()
while(ll):
    z = ll.pop(0)
    for elem in G[z-1]:
        if(Vis[elem-1] == 0):
            Vis[elem-1] = 1 
            if(l[elem-1] == l[z-1]-1):
                sp[elem-1] = 1
                ll.append(elem)
ll=[x]
str=""
while(ll != [y]):
    l1 = []
    for elem in ll:
        for i in G1[elem-1]:
            if (l[i[0]-1] == l[elem-1]+1):
                if (sp[i[0]-1] == 1):
                    l1.append(i)
    st = min(map(lambda t: t[1], l1))
    str = str + st
    ll = list(set([t[0] for t in l1 if t[1] == st]))     
print(str)