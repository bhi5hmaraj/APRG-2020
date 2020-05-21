from collections import defaultdict 

list_of_inputs = input().split()

N= (int)(list_of_inputs[0])
b= (int )(list_of_inputs[1])

X={}
Y={}


startpos= input().split()

x=(int)(startpos[0])-1
y=(int)(startpos[1])-1


    

for k in range (b):
    pos=input().split()
    X[((int)(pos[0])-1,(int)(pos[1])-1)]=1
    
Y[(x,y)]=2

queue = []
queue.append([x,y])


while(queue):
    m = queue.pop(0)
    if ((m[0]+1)<N and (m[0]+1,m[1]) not in X  and (m[0]+1,m[1]) not in Y) :
        Y[(m[0]+1,m[1])]=2
        queue.append([m[0]+1,m[1]])
        
    if m[1]+1<N and (m[0],m[1]+1) not in X and (m[0],m[1]+1) not in Y  :
        Y[(m[0],m[1]+1)]=2
        queue.append([m[0],m[1]+1])
        
    if m[0]-1>=0 and (m[0]-1,m[1]) not in X and (m[0]-1,m[1]) not in Y:
        Y[(m[0]-1,m[1])]=2
        queue.append([m[0]-1,m[1]])
        
    if m[1]-1>=0 and (m[0],m[1]-1) not in X and (m[0],m[1]-1) not in Y :
        Y[(m[0],m[1]-1)]=2
        queue.append([m[0],m[1]-1])
        
        
f=0    
for i in range(N):
    for j in range(N):
        if (i,j) not in X and (i,j) not in Y:
            f=1
            break        
        
if (f==0):
    print("Y")
else:
    print("N")