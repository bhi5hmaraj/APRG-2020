class node:
    def __init__(self):
        self.parent=None
        self.children=set()
        self.v1=None
        self.v2=None
rank=dict()
v=0
Node=dict()
def dfs(m,t):
    global v
    global rank
    rank[t].add(m)
    if v<t:
        v=t
    if len(m.children)==0:
        m.v1=1
        m.v2=0
        return(0)
    else:
        for i in m.children:
            dfs(i,t+1)

def choose(r):
    global rank
    global Node
    global v
    i=v
    while i>=0:
        for j in rank[i]:
            if len(j.children)==0:continue
            t1=0
            t2=0
            d=0
            for l in j.children:
                t1=t1+max(l.v1,l.v2)
                if max(l.v1,l.v2)==l.v1:
                    d=1
                t2=t2+l.v2
            j.v1=t2+1
            if d==0:
                j.v2=t2
            else:
                j.v2=t1
        i=i-1
    return(max(r.v1,r.v2))

def run():
    global rank
    a=list(map(int,input().split()))
    k=a[0]
    while k>0:
        Node[k]=node()
        rank[k-1]=set()
        k=k-1
    while a[0]>1:
        b=list(map(int,input().split()))
        Node[b[0]].children.add(Node[b[1]])
        Node[b[1]].parent=Node[b[0]]
        if Node[b[0]].parent==None:
            r=Node[b[0]]
        a[0]=a[0]-1
    dfs(r,0)
    print(choose(r))
run()