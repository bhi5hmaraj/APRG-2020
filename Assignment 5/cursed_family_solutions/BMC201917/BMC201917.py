import sys
sys.setrecursionlimit(10**6)
from collections import defaultdict
G=defaultdict(list)
def add_child(G,u,v):
    G[u].append(v)
n=int(input())
x=n*(n+1)//2
for i in range(n-1):
    a,b=map(int,input().split())
    x=x-b
    add_child(G,a,b)
I=defaultdict(dict)
def parent_absent(vertex):
    if G.get(vertex):
        if I.get(vertex) and I[vertex].get(0):
            return I[vertex][0]
        else:
            I[vertex][0]=sum(max(parent_absent(child),parent_present(child)) for child in G[vertex])
            return I[vertex][0]
    else:
        return 0
def parent_present(vertex):
    if G.get(vertex):
        if I.get(vertex) and I[vertex].get(1):
            return I[vertex][1]
        else:
            I[vertex][1]=1+sum(parent_absent(child) for child in G[vertex])
        return I[vertex][1]
    else:
        return 1
print(max(parent_absent(x),parent_present(x)))