M,N = map(int,input().split())

L=[]
for x in range(M):
    y = input()
    L.append(y)
    
MWP = [['.' for x in range (N+2)] for y in range (M+2)]

for x in range(M):
    for y in range(N):
        MWP[x+1][y+1]=L[x][y]
        if MWP[x+1][y+1]=='.':
            MWP[x+1][y+1]='0'
        
for x in range(1,M+1):
    for y in range(1,N+1):
        c=0
        if MWP[x][y]!='*':
            if MWP[x-1][y-1]=='*':
                c+=1
            if MWP[x-1][y]=='*':
                c+=1
            if MWP[x-1][y+1]=='*':
                c+=1
            if MWP[x][y-1]=='*':
                c+=1
            if MWP[x][y+1]=='*':
                c+=1    
            if MWP[x+1][y-1]=='*':
                c+=1
            if MWP[x+1][y]=='*':
                c+=1
            if MWP[x+1][y+1]=='*':
                c+=1
            MWP[x][y]=(chr)((ord)(MWP[x][y])+c)
            
            
for x in range(1,M+1):
    a=""
    for y in range(1,N+1):
        a+=MWP[x][y]
    print(a)
