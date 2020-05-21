import sys
sys.setrecursionlimit(10**6)


import collections

def fill(a,m,n):
    while a:
        x= a.pop()
        m.add(x)
        if x[0]>0 and x[1]-1>0:
            if (x[0],x[1]-1) not in m:
               a.append((x[0],x[1]-1))
        if x[0]-1>0 and x[1]>0:
            if (x[0]-1,x[1]) not in m:
               a.append((x[0]-1,x[1]))
        if x[0]+1<=n and x[1]>0 :
            if (x[0]+1,x[1]) not in m:
               a.append((x[0]+1,x[1]))
        if x[0]>0 and x[1]+1<=n:
            if (x[0],x[1]+1) not in m:
               a.append((x[0],x[1]+1))
        
    return(m)

def run():
    a= list(map(int,input().split()))
    b= list(map(int,input().split()))
    c= set()
    e= collections.deque()
    x= a[1]
    while x>=1:
        y= list(map(int,input().split()))
        c.add((y[0],y[1]))
        x=x-1
    d=(b[0],b[1])
    e.append(d)
    l= len(fill(e,c,a[0]))
    if l== a[0]*a[0]:
        print('Y')
    else:
        print('N')
run()