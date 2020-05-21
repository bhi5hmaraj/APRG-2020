N, b = map(int,input().split())
b1,b2 = map(int,input().split())

   
blacks = {}
new_blacks ={}

for i in range(b):
    el = list(map(int,input().split()))
    blacks[(el[0]-1,el[1]-1)] = 1
   
   
new_blacks[(b1-1,b2-1)]=1


add = []
add.append([b1-1,b2-1])

while(add):
    test = add.pop(0)
    if test[0]+1 < N and (test[0]+1,test[1]) not in blacks  and (test[0]+1,test[1]) not in new_blacks :
        add.append([test[0]+1,test[1]])
        new_blacks[(test[0]+1,test[1])] = 1
        
    if test[1]+1 < N and (test[0],test[1]+1) not in blacks and (test[0],test[1]+1) not in new_blacks  :
        add.append([test[0],test[1]+1])
        new_blacks[(test[0],test[1]+1)] = 1
        
    if test[0]-1 >= 0 and (test[0]-1,test[1]) not in blacks and (test[0]-1,test[1]) not in new_blacks:
        add.append([test[0]-1,test[1]])
        new_blacks[(test[0]-1,test[1])] = 1
        
    if test[1]-1 >= 0 and (test[0],test[1]-1) not in blacks and (test[0],test[1]-1) not in new_blacks :
        add.append([test[0],test[1]-1])
        new_blacks[(test[0],test[1]-1)] = 1
        
        
        
        


for i in range(N):
    for j in range(N):
        if (i,j) not in blacks and (i,j) not in new_blacks:
            print("N")
            break
    else:
        print("Y")
        break
    break
        