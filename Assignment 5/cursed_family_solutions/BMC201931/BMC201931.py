import sys
sys.setrecursionlimit(10**6)
from collections import defaultdict
n=int(input())
x=n*(n+1)//2
fam=defaultdict(list)

def f1(fam,u,v):
    fam[u].append(v)

for i in range(n-1):
    a,b=map(int,input().split())
    x=x-b
    f1(fam,a,b)
lol=defaultdict(dict)

def f2(z):
    if fam.get(z):
        if lol.get(z) and lol[z].get(1):
            return lol[z][1]
        else:
            lol[z][1]=1+sum(f3(c) for c in fam[z])
        return lol[z][1]
    else:
        return 1

def f3(z):
    if fam.get(z):
        if lol.get(z) and lol[z].get(0):
            return lol[z][0]
        else:
            lol[z][0]=sum(max(f3(c),f2(c)) for c in fam[z])
            return lol[z][0]
    else:
        return 0

print(max(f2(x),f3(x)))