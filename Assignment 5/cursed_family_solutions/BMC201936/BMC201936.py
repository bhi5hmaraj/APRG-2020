import sys
sys.setrecursionlimit(10**6)
from collections import defaultdict
Take=defaultdict(list)
def addson(Take,One,Two):
    Take[One].append(Two)
inp=int(input())
A=inp*(inp+1)//2
for i in range(inp-1):
    X,Y=map(int,input().split())
    A=A-Y
    addson(Take,X,Y)
Let=defaultdict(dict)

def yesparent(ver):
    if Take.get(ver):
        if Let.get(ver) and Let[ver].get(0):
            return Let[ver][0]
        else:
            Let[ver][0]=sum(max(noparent(son),yesparent(son)) for son in Take[ver])
        return Let[ver][0]
    else:
        return 0

def noparent(ver):
    if Take.get(ver):
        if Let.get(ver) and Let[ver].get(1):
            return Let[ver][1]
        else:
            Let[ver][1]=1+sum(yesparent(son) for son in Take[ver])
            return Let[ver][1]
    else:
        return 1

print(max(noparent(A),yesparent(A)))