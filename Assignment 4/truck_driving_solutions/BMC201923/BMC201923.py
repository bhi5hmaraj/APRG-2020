class UnionFind:
    p=[]
    rank=[]
    def __init__(self,n):
        for i in range(n):
            self.rank.append(0)
            self.p.append(i)

    def findRoot(self,i):

        if self.p[i]==i:
            self.p[i]=i
        else:
            self.p[i]=self.findRoot(self.p[i])
        
        return self.p[i]
    

    def isSame(self,i,j):
        return self.findRoot(i)==self.findRoot(j)

    def union(self,x,y):
        if self.isSame(x,y):
            return
        i=self.findRoot(x)
        j=self.findRoot(y)
        self.p[i]=j
'''
        if self.rank[i]<self.rank[j]:
            self.p[i]=j
        elif self.rank[i]>self.rank[j]:
            self.p[j]=i
        else:
            self.p[i]=j
            self.rank[i]+=1

    def ranksort(self,u,v):
        if self.rank[u] <= self.rank[v]:
            return (u,v)
        else:
            return (v,u)
'''
def run():
    n,m=list(map(int,input().split()))
    edgelst=[]
    for i in range(m):
        u,v,w=list(map(int,input().split()))
        u-=1
        v-=1
        edgelst.append((w,u,v))
    edgelst.sort()
    foo=UnionFind(n)
    q=int(input())
    qans=[None]*q
    qvs=[]
    for i in range(n):
        qvs.append(set())

    for i in range(q):
        x,y=list(map(int,input().split()))
        x-=1
        y-=1
        qvs[x].add(i)
        qvs[y].add(i)

    for (w,u,v) in edgelst:
        if not foo.isSame(u,v):
            u,v=(foo.findRoot(u),foo.findRoot(v))
            s=qvs[u] & qvs[v]
            for x in s:
                qans[x]=w
            if len(qvs[v])>=len(qvs[u]):
                qvs[v].symmetric_difference_update(qvs[u])
                #qvs[u]=set()
                foo.union(u,v)
            else:
                qvs[u].symmetric_difference_update(qvs[v])
                #qvs[v]=set()
                foo.union(v,u)
    for x in qans:
        print(x)

    return

run()

