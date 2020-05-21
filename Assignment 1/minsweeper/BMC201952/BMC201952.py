import sys
def Matrix(A,B):
    if (A==B):
        return (A-1)
    else:
        return A
    


def Findbomb(m,n,o):
    List1=[]
    for i in range(m):
        List2=[]
        for j in range(n):
            
            if (o[i][j]=='*'):
                List2.append('*')
            elif (o[i][j]=='.'):
                Pos=0
                for p in (list(set([abs(i-1),i,Matrix((i+1),m)]))):
                    for q in (list(set([abs(j-1),j,Matrix((j+1),n)]))):
                        if (o[p][q]=='*'):
                            Pos = Pos + 1
                List2.append(Pos)
        List1.append(List2)
    return List1
mn=list(map (int, input().split()))
y=[]
for k in range(mn[0]):
    y.append(input())
s=(Findbomb(mn[0],mn[1],y))
for u in range(mn[0]):
    for elem in s[u]:
        print(elem,end='')
    print('')
