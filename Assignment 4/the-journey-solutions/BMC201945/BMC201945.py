from queue import PriorityQueue
l=list(map(int,input().split()))
m=list(map(int,input().split()))
adj_list={}
for i in range(100):
    for j in range(l[0]):
        adj_list[(i,j+1)]=[]
for i in range(1,l[0]+1):
  d=list(map(int,input().split()))
  for j in range(len(d)):
    if j >0:
      adj_list[(d[j],i)].append((d[j-1],i,m[i-1]))
      adj_list[(d[j-1],i)].append((d[j],i,m[i-1]))
    if j<len(d)-1:
      adj_list[(d[j],i)].append((d[j+1],i,m[i-1]))
      adj_list[(d[j+1],i)].append((d[j],i,m[i-1]))
def spath(adj_list,x):
    dis={}
    q=PriorityQueue()
    for i in range(100):
        for j in range(l[0]):
            if i==x:
                q.put((0,i,j+1))
                dis[(i,j+1)]=0
            else:
                dis[(i,j+1)]=10**20
    while not q.empty():
        p=q.get()
        a1=p[0]
        a2=p[1]
        a3=p[2]
        for i in adj_list[(a2,a3)]:
            b1=i[0]
            b2=i[1]
            b3=i[2]
            a=abs(a2-b1)*b3+a1
            if a<dis[(b1,b2)]:
                dis[(b1,b2)]=a
                q.put((dis[(b1,b2)],b1,b2))
        for j in range(l[0]):
            if a3==j+1:
                a=a1
            else:
                a=a1+60
            if a<dis[(a2,j+1)]:
                dis[(a2,j+1)]=a
                q.put((dis[(a2,j+1)],a2,j+1))
    return(dis)
d=spath(adj_list,0)
a=[]
for i in range(l[0]):
    a.append(d[(l[1],i+1)])
r=min(a)
if r==10**20:
    print('IMPOSSIBLE')
else:
    print(r)
