#def split1(word):
 #   return [char for char in word]
x=input().split()
n=int(x[0])
m=int(x[1])

matrix=[]
for i in range(n):
    #k = list(split1(input())
    #matrix.append(k)
    matrix.append(list(input()))
for i in range(n):
    for j in range(m): 
        if(matrix[i][j]=='.'):
            matrix[i][j]=0
        elif(matrix[i][j]=='*'):
            for k in [-1,0,1]:
                for l in [-1,0,1]:
                    if(((i+k) in range(n)) and ((j+l) in range(m))):
                        if(matrix[i+k][j+l]!='*'):
                            if(matrix[i+k][j+l]=="."):
                                matrix[i+k][j+l]=1
                            else:
                                matrix[i+k][j+l]=matrix[i+k][j+l]+1
        #elif(matrix[i][j]=='.'):
         #   matrix[i][j]=0
for i in range(n):
    qw=""
    for val in matrix[i]:
        if(val=='*'):
            qw+=val
        else:
            qw+=str(val)
    print(qw)
