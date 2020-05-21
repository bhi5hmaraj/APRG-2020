l1=list(map(int,input().split()))
a1=l1[0]
a2=l1[1]
l2=list(map(int,input().split()))
b1=l2[0]
b2=l2[1]
black={}
for i in  range (a2):    
#    (m,n)=map(int,input().split())
#   black.append((m,n))
    x=input().split()
    black[int (x[0]),int (x[1])]=1
counter=1
white={(b1,b2):1}        
queue=[(b1,b2)]
while queue:
#    counter=1
 #   white={(b1,b2):1}
    t=queue.pop(0)
    if t[0]>1 and (t[0]-1,t[1]) not in black and (t[0]-1,t[1]) not in white:
         white[(t[0]-1,t[1])]=white[(t[0],t[1])]+1
#         white.append((t[0]-1,t[1]))
         queue.append((t[0]-1,t[1]))   
#         counter=counter+1
    if t[0]<a1 and (t[0]+1,t[1]) not in black and (t[0]+1,t[1]) not in white:
        white[(t[0]+1,t[1])]=white[(t[0],t[1])]+1
 #       white.append((t[0]+1,t[1]))
        queue.append((t[0]+1,t[1]))
#        counter=counter+1
    if t[1]>1 and (t[0],t[1]-1) not in black and (t[0],t[1]-1) not in white:
        white[(t[0],t[1]-1)]=white[(t[0],t[1])]+1
#        white.append((t[0],t[1]-1))
        queue.append((t[0],t[1]-1))
#        counter=counter+1
    if t[1]<a1 and (t[0],t[1]+1) not in black and (t[0],t[1]+1) not in white:
        white[(t[0],t[1]+1)]=white[(t[0],t[1])]+1
#        white.append((t[0],t[1]+1))
        queue.append((t[0],(t[1]+1)))
#        counter=counter+1
track=True
for i in range (1,a1+1):
    for j in range (1,a1+1):
        if (i,j) not in white and (i,j) not in black:
            track=False
            break
  
                     
                     
                     
                     
if track==True:
    print("Y")
else:
    print("N")


    
    
    
        
    