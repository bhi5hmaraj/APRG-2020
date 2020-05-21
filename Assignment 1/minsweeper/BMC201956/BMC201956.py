import sys
def f(a,m):
    if (a==m):
        return (a-1)
    else:
        return a
    


def hint(r,c,l):
    l1=[]
    for i in range(r):
        l2=[]
        for j in range(c):
            
            if (l[i][j]=='*'):
                l2.append('*')
            elif (l[i][j]=='.'):
                count=0
                for p in (list(set([abs(i-1),i,f((i+1),r)]))):
                    for q in (list(set([abs(j-1),j,f((j+1),c)]))):
                        if (l[p][q]=='*'):
                            count+=1
                l2.append(count)
        l1.append(l2)
    return l1
rc=list(map (int, input().split()))
y=[]
for k in range(rc[0]):
    y.append(input())
s=(hint(rc[0],rc[1],y))
for u in range(rc[0]):
    for elem in s[u]:
        print(elem,end='')
    print('')
