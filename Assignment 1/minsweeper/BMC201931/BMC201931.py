R,C= map(int,input().split())
matrix=[]
L=[]
for i in range(R) :
    matrix.append(list(map(str,input())))

def change(matrix,a,b) :
    Z=0
    for l in range(3) :
        for k in range(3) :
            if((i-1+l,j-1+k) in L) :
                Z=Z+1
              
    return (Z)
       
for i in range(R) :
    for j in range(C) :
        if(matrix[i][j] == '*') :
            L.append((i,j))

for i in range(R) :
    for j in range(C) :
        if(matrix[i][j] == '.') :
            matrix[i][j]=change(matrix,i,j)
            
for i in range(R) :
    print(''.join(map(str,matrix[i])))

