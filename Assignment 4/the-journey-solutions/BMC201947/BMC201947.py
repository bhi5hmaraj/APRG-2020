import collections
import heapq
import sys

def shortestPath(edges, source, sink):
    # create a weighted DAG - {node:[(cost,neighbour), ...]}
    graph = collections.defaultdict(list)
    for l, r, c in edges:
        graph[l].append((c,r))
    # create a priority queue and hash set to store visited nodes
    
    queue, visited = [(0, source, 0)], set()
    heapq.heapify(queue)
    # traverse graph with BFS
    M = 0
    N1 = 0
    store = sys.maxsize
    Path = {source : 0}
    r = {source:0}
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            path = path + 1
            Path[node]=path
            
            for i in range(N):
                if node == (i,sink) :
                    Path[node] = path
                    M = path
                    N1 = cost
                    if N1 < store:
                        store = N1
                    
            r[node]=cost
            for c, neighbour in graph[node]:
                if neighbour not in visited:
                    heapq.heappush(queue, (cost+c, neighbour, path))
        elif node in visited and path+1<(Path[node]):
            Path[node]=path+1
        elif cost==N1 and cost==r[node] and node in visited:
            if M > (path):
                Path[node] = path + 1
                M = (Path[node])

    if N1==0 : 
        return(-1)
    else:
        return(store)
#last = []
if __name__ == "__main__":
    edges = []
    N,k1 = map(int,input().split())
    weight = []
    weight = [int(x) for x in input().split()]
    l = []
    for i in range(N):
        l.append([])
        l[i]= l[i]+[int(x) for x in input().split()]
        for j in range(len(l[i])-1):
            edges.append(((i,l[i][j]),(i,l[i][j+1]),weight[i]*(abs(l[i][j+1]-l[i][j]))))
            edges.append(((i,l[i][j+1]),(i,l[i][j]),weight[i]*(abs(l[i][j+1]-l[i][j]))))
    for i in range(N):
        for j in range(len(l[i])):
            for k in range(N):
                if l[i][j] in l[k] and i!= k and l[i][j] != k1:
                    a = l[k].index(l[i][j])
                    edges.append(((i,l[i][j]),(k,l[k][a]),60))
                    edges.append(((k,l[k][a]),(i,l[i][j]),60))
    mini = sys.maxsize
    for i in range(N):
        if l[i][0] == 0 : 
            ll = shortestPath(edges, (i,0), k1)
            if (mini > ll):
                mini = ll
    if (mini == -1) or mini==sys.maxsize:
        print("IMPOSSIBLE")
    else:
        print(mini)

