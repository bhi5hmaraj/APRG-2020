import queue
from collections import deque
def find(graph, start,length):         
    d=set()         
    d.add(start)         
    length[start]=0         
    q = deque([start])         
    while len(q):             
        at = q.popleft()             
        a=length[at]             
        for next in graph[at]:                 
            if next not in d:                     
                length[next]=a+1                     
                q.append(next)                     
                d.add(next)         
    return length 
def run():     
    l= ""
    length1={}     
    length={}     
    graph= {}     
    c= set()
    a=list(map(int,input().split()))     
    b=list(map(int,input().split()))
    tras={}
    i=1
    dr=[]
    while i<=a[0]:  
        c1=set()
        dr.append(c1)
        graph[i]=set()        
        length[i]=[]         
        length1[i]=[]         
        i=i+1     
    i=1     
    while i<=a[1]:         
        e=list(input().split())
        f= int(e[0])         
        g= int(e[2])         
        graph[f].add(g)         
        graph[g].add(f)         
        tras[(f,g)]=e[1]
        tras[(g,f)]=e[1]
        i=i+1
    i=1     
    n= find(graph,b[0],length)     
    m= find(graph,b[1],length1)     
    d= n[b[1]]     
    while i<=a[0]:         
        x=n[i]         
        y=m[i] 
        if x +y == d:            
             c.add(i)
             dr[n[i]].add(i)
        i=i+1
    i=0    
    z=[b[0]]
    while i<d: 
        j=0
        z1=set()
        h='z'
        a1=len(z)
        while j<a1:
            o=z[j]
            for next in graph[o]:
                  if next in dr[i+1]:
                      k=tras[(o,next)]
                      if k< h:                     
                         h= k
            j=j+1
        j=0
        while j<a1:
            o=z[j]
            for next in dr[i+1]:
                  if next in graph[o]:
                      k=tras[(o,next)]
                      if k== h:                     
                         z1.add(next)
            j=j+1
        z1=list(z1)
        z=z1
        i=i+1
        l+=h
    print(l)  
run()