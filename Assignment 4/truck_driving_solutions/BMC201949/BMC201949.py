import sys
sys.setrecursionlimit(10**6)
in1=list(map(int,input().split()))
N=in1[0]
M=in1[1]
edges=[]
for i in range(0,M):
    x=list(map(int,input().split()))
    a=x[0]-1
    b=x[1]-1
    c=x[2]
    edges.append((c,a,b))
edges.sort(key= lambda x:x[0])
Q=int(input())
qu=[]
answer=[]

for i in range(N):
    set1=set()
    qu.append(set1)
for i in range(0,Q):
    answer.append(0)
    in2=list(map(int,input().split()))
    k=in2[0]-1
    l=in2[1]-1
    qu[k].add(i)
    qu[l].add(i)

parent=[]
for i in range(0,N):
    parent.append(i)
def find(u):
    pointer=u
    while(pointer!=parent[pointer]):
        pointer=parent[pointer]
    return pointer

        
    
count=0
for (c,a,b) in edges :
    if count==N-1:
        break
    else:    
        y=find(a)
        z=find(b)
        if y!=z:
            if (len(qu[y]))>(len(qu[z])):
                (y,z)=(z,y)
            parent[y]=z
            count=count+1
            for ele in qu[y]:
                if ele in qu[z]:
                    answer[ele]=c
                    qu[z].remove(ele) 
                else:
                    qu[z].add(ele)
for j in range(0,Q):
    print(answer[j])
        
        
        
        
        
        

