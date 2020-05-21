li=list(map (int, input().split()))
y=[]
for k in range(li[0]):
    y.append(input())

def func0(a,m):
    if (a==m):
        return (a-1)
    else:
        return a
def func(row,col,l):
    x=[]
    for i in range(row):
        y=[]
        for j in range(col):
            
            if (l[i][j]=='*'):
                y.append('*')
            elif (l[i][j]=='.'):
                c=0
                for m in (list(set([abs(i-1),i,func0((i+1),row)]))):
                    for n in (list(set([abs(j-1),j,func0((j+1),col)]))):
                        if (l[m][n]=='*'):
                            c+=1
                y.append(c)
        x.append(y)
    return x
p=(func(li[0],li[1],y))
for e in range(li[0]):
    for elem in p[e]:
        print(elem,end='')
    print('')
