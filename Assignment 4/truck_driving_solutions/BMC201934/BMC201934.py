import heapq

find=dict()
dist2=[]
meg=dict()
dict1=dict()
parent=[]
dict2=[]
rank=[]
def line():
    global rank
    global find
    global dict1
    global dist2
    global dict2
    global parent
    while dist2:
        f=heapq.heappop(dist2)
        x=find(f[1])
        y=find(f[2])
        if x==y: continue
        m=set()
        s=dict1[x]&dict1[y]
        l1=len(dict1[x])
        l2=len(dict1[y])
        for i in s:
                dict2[i]=f[0]
        if l1>=l2:
            dict1[x].symmetric_difference_update(dict1[y])
            parent[y]=x
        else:
            dict1[y].symmetric_difference_update(dict1[x])
            parent[x]=y
        
        
def find(a):
    global parent
    m=a
    d=1
    while d!=0:
        d=m-parent[m]
        m=parent[m]
    parent[a]=m
    return(m)
    
def run():
    global rank
    global dict2
    global dict1
    global dist2
    global parent
    a=list(map(int,input().split()))
    j=0
    while j<a[0]:
        parent.append(j)
        rank.append(1)
        dict1[j+1]=set()
        j=j+1
    parent.append(a[0])
    rank.append(1)
    for j in range(a[1]):
        d=list(map(int,input().split()))
        heapq.heappush(dist2,(d[2],d[0],d[1]))
    dist2.sort()
    c=list(map(int,input().split()))
    f=0
    while f<c[0]:
        c2=list(map(int,input().split()))
        dict1[c2[0]].add(f)
        dict1[c2[1]].add(f)
        f=f+1
    dict2=[0]*c[0]
    line()
    f=0
    while f<c[0]:
        print(dict2[f])
        f=f+1
run()