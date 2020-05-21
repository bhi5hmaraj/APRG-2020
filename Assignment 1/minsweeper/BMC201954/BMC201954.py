n = list(map(int,input().split()))
mat = []
for i in range(n[0]):
    a=[]
    for j in input():
        a.append(j)
    mat.append(a)
l=[]
for i in range(n[1]):
    l.append('.')
N=[l]+ mat[0:(len(mat)-1)]
S=(mat[1:(len(mat))])+[l]
E=[]
for i in range(len(mat)):
    E.append((mat[i]+['.'])[1:(n[1]+1)])
W=[]
for i in range(len(mat)):
    W.append((['.']+mat[i])[0:(n[1])])
NE=[l]+(E[0:(len(E)-1)])
SE=(E[1:len(E)])+[l]
NW=[l]+(W[0:(len(W)-1)])
SW=(W[1:len(W)])+[l]
def z(a,b,c,d,e,f,g,h,k):
    m=[]
    for i in range(len(a)):
        for j in range(len(a[i])):
            m.append(((a[i])[j],(b[i])[j],(c[i])[j],(d[i])[j],(e[i])[j],(f[i])[j],(g[i])[j],(h[i])[j],(k[i])[j]))
    return m
def f(x):
        r=0
        if x[0]=='*':
            return '*'
        else:
            for i in x[0:]:
                    if i=='*':
                        r+=1
            return r
b=(z(mat,N,S,E,W,NE,NW,SE,SW))
#print(b)
#print(f('.','*','*','*','*','.','.','.','.'))
a=list(map(str,list(map(f,list(map(list,z(mat,N,S,E,W,NE,NW,SE,SW)))))))
b=[]
for i in range(n[0]):
    b.append(a[0:(n[1])])
    a=a[(n[1]):]
def t(l):
    a=''
    for i in l:
        a+=i
    return a
c=list(map(t,b))
#print(c)
for i in c:
    print(i)

