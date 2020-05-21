import heapq

def tree(graph,dist,x,length):
    m=set()
    m1=[(0,x)]
    while m1:
        c=heapq.heappop(m1)
        if c[1] in m: continue
        length[c[1]]=c[0]
        m.add(c[1])
        for i in graph[c[1]]:
            if i not in m:
                heapq.heappush(m1,(min(dist[(i,c[1])])+c[0],i))
    return(length)
                
def run():
    a= list(map(int,input().split()))
    m=set()
    length=dict()
    length1=dict()
    graph=dict()
    dist=dict()
    dist1=dict()
    j=a[0]-1
    while j>=0:
        length[j+1]=10000000000000000000000
        length1[j+1]=10000000000000000000000
        graph[j+1]=set()
        j=j-1
    i= a[1]-1
    while i>=0:
        d=list(map(int,input().split()))
        d1=(d[0],d[1])
        d2=(d[1],d[0])
        d3=d[2]
        if d1 not in m:
            dist[d1]=set()
            dist[d2]=set()
            m.add(d1)
            m.add(d2)
        dist[(d[0],d[1])].add(d3)
        dist[(d[1],d[0])].add(d3)
        dist1[d3,d1]=d1
        dist1[d3,d2]=d2
        graph[d[0]].add(d[1])
        graph[d[1]].add(d[0])
        i=i-1
    v=10000000000000000000
    c=tree(graph,dist,1,length)
    c1=tree(graph,dist,a[0],length1)
    e= c[a[0]]
    for i in dist1:
        if c[i[1][0]]+c1[i[1][1]]+i[0]<v and c[i[1][0]]+c1[i[1][1]]+i[0] >e:
            v=c[i[1][0]]+c1[i[1][1]]+i[0]
    print(v)
    
run()
