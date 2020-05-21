
N1, b1 = input().split()
N=int(N1)
b=int(b1)
u1,v1 = input().split()
u=int(u1)
v=int(v1)

Black={}
Red={}
Red[(u-1,v-1)]=1
#entering black cells
for i in range(b):
    bbox = list(map(int,input().split()))
    Black[(bbox[0]-1,bbox[1]-1)]=1
   
queue = []
queue.append([u-1,v-1])

while(queue):
    ptr = queue.pop(0)    #pointer for colouring
    if ptr[1]-1>=0 and (ptr[0],ptr[1]-1) not in Black and (ptr[0],ptr[1]-1) not in Red :
        Red[(ptr[0],ptr[1]-1)]=1
        queue.append([ptr[0],ptr[1]-1])
    if ptr[0]-1>=0 and (ptr[0]-1,ptr[1]) not in Black and (ptr[0]-1,ptr[1]) not in Red:
        Red[(ptr[0]-1,ptr[1])]=1
        queue.append([ptr[0]-1,ptr[1]])
    if ptr[0]+1<N and (ptr[0]+1,ptr[1]) not in Black  and (ptr[0]+1,ptr[1]) not in Red :
        Red[(ptr[0]+1,ptr[1])]=1
        queue.append([ptr[0]+1,ptr[1]])
    if ptr[1]+1<N and (ptr[0],ptr[1]+1) not in Black and (ptr[0],ptr[1]+1) not in Red  :
        Red[(ptr[0],ptr[1]+1)]=1
        queue.append([ptr[0],ptr[1]+1])
c=0    
for i in range(N):
    for j in range(N):
        if (i,j) not in Black and (i,j) not in Red:
            c=1
            break
if c==1:
    print('N')
else:
    print('Y')