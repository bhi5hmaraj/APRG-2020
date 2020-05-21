parent = {}




def find(vertex):
    
    while parent[vertex] != vertex:
        vertex = parent[vertex]
    return vertex


def kruskal(graph, array, n):
    
    for vertex in graph['vertices']:
        parent[vertex] = vertex
        #minimum_spanning_tree = set()
    edges = graph['edges']
    edges.sort()
    # print edges
    k = 0
    for edge in edges:
        if k < n-1:
       # print(edge)
            weight, vertex1, vertex2 = edge
        #print('####', answers, '####', array)
            root1, root2 = find(vertex1), find(vertex2)
            if root1 != root2:
                #print(parent)
                if len(array[root1]) < len(array[root2]):
                    parent[root1] = root2    
                else:
                    parent[root2] = root1
                if parent[root1] == root2:
                    for i in array[root1]:
                        if i in array[root2]:
                            answers[i] = weight
                            array[root2].remove(i)
                        else:
                            array[root2].add(i)
                        
                else:
                        
                    for j in array[root2]:
                        if j in array[root1]:
                            answers[j] = weight
                            array[root1].remove(j)
                        else:
                            array[root1].add(j)
                    
            #minimum_spanning_tree.add(edge)
                k+=1  
        else:
            break
            
            
n, m = map(int, input().split())
array = [set() for i in range(n)]
graph = {
        'vertices' : [],
        'edges' : []
        }
for i in range(n):
    graph['vertices'].append(i)
    parent[i] = i
for i in range(m):
    u, v, w = map(int, input().split())
    graph['edges'].append((w, u - 1, v - 1))

q = int(input())
for i in range(q):
    a, b = map(int, input().split())
        # print(graph.lca(a-1, b-1))
    array[a-1].add(i)
    array[b-1].add(i)
answers = [-1 for i in range(q)]
sol = kruskal(graph, array, n)
for i in range(q):
    print(answers[i])
