
N, b = map(int,input().split())

p,q = map(int,input().split())
m=p-1
n=q-1
   
R={}
R1={}

for i in range(b):
    d = list(map(int,input().split()))
    R[(d[0]-1,d[1]-1)]=1
   
   
R1[(m,n)]=1

   

queue = []
queue.append([m,n])


count=1
while(queue):
    a = queue.pop(0)
    if a[0]+1<N and (a[0]+1,a[1]) not in R  and (a[0]+1,a[1]) not in R1 :
        count = count + 1
        R1[(a[0]+1,a[1])]=1
        queue.append([a[0]+1,a[1]])
    if a[1]+1<N and (a[0],a[1]+1) not in R and (a[0],a[1]+1) not in R1  :
        count = count + 1
        R1[(a[0],a[1]+1)]=1
        queue.append([a[0],a[1]+1])
    if a[0]-1>=0 and (a[0]-1,a[1]) not in R and (a[0]-1,a[1]) not in R1 :
        count = count + 1
        R1[(a[0]-1,a[1])]=1
        queue.append([a[0]-1,a[1]])
    if a[1]-1>=0 and (a[0],a[1]-1) not in R and (a[0],a[1]-1) not in R1 :
        count = count + 1
        R1[(a[0],a[1]-1)]=1
        queue.append([a[0],a[1]-1])
n=1    
for i in range(N):
    for j in range(N):
        if (i,j) not in R and (i,j) not in R1:
            n=2
            break
if n==1:
    print('Y')
else:
    print('N')