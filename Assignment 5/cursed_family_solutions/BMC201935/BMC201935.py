n = int(input())
edges = [[] for i in range(n+1)]
for i in range(n-1):
    x, y = input().split()
    x = int(x)
    y = int(y)
    edges[x].append(y)
include_root = []
exclude_root = []
from itertools import chain
def max_node():
    for i in range(n+1):
        if edges[i]:
            t = i
            if t not in chain(*edges):
                return t
def max(x, y):
    if(x > y): 
        return x 
    else: 
        return y 
def maximum(parent,include_root,exclude_root):
    for child in edges[parent]:
        maximum(child,include_root,exclude_root)
    include_root[parent] = 1 + sum(exclude_root[kid] for kid in edges[parent])    
    exclude_root[parent] = sum([max(include_root[kid],exclude_root[kid]) for kid in edges[parent]])
    return max(include_root[parent],exclude_root[parent])
print(maximum(max_node(),[0]*(n+1),[0]*(n+1)))

