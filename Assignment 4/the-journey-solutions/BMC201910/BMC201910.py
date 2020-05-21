ls=list(map(int,input().split()))
N= ls[0]
K=ls[1]
l=list(map(int,input().split()))
Times=[]
for i in range(N):
    Times.append(l[i])
Graph3=[]
for i in range(N):
    Graph3.append(list(map(int,input().split())))
    
for p in Graph3:
    for i in range(len(p)):
        if p[i]!=0:
            p[i]=(p[i],Graph3.index(p))
        else:
            p[i]=(0,0)

        


Graph1=[]
for route in Graph3:
    for busStop in route:
        if busStop != route[-1]:
            Graph1=Graph1+[[busStop,route[route.index(busStop)+1],((route[route.index(busStop)+1][0])-busStop[0])*(Times[Graph3.index(route)])]]
            
for l in Graph3:
    if l!=Graph3[-1]:
        for k1 in l:
            for p in Graph3[Graph3.index(l):]:
                for k2 in p:
                    if (k1[0]!=0) and (k1[0]==k2[0]) and (k1[1]!=k2[1]):
                        Graph1.append([k1,k2,60])

            
Graph={}
for l in Graph1:
    Graph[l[0]]={}
    Graph[l[1]]={}

for l in Graph1:
    Graph[l[0]].update({l[1]:l[2]})
    Graph[l[1]].update({l[0]:l[2]})
    
visited={(0,0):0}
path = {}
nodes=[]
for k in Graph:
    nodes.append(k)
while nodes:
    min_node=None
    for node in nodes:
        if node in visited:
            if min_node is None:
                min_node=node
            elif visited[node] < visited[min_node]:
                min_node=node
                
    if min_node is None:
        break
        
    nodes.remove(min_node)
    current_weight=visited[min_node]
    
    for edge in Graph[min_node]:
        weight = current_weight + Graph[min_node][edge]
        if (edge not in visited) or (weight < visited[edge]):
            visited[edge] = weight
            path[edge] = min_node
            
    
                
    
'''if y in path:
    print(str(path[y]-1)+' '+str(visited[y]))
else:
    print('IMPOSSIBLE')'''

if K in [mn[0] for mn in path]:
    print(min([visited[jkl] for jkl in Graph if jkl[0]== K]))
else:
    print('IMPOSSIBLE')

            






    
    
    
    

#print(Graph3)
#print(Graph1)
#print(K)
#print(Graph)
#print(nodes)
#print(path)
