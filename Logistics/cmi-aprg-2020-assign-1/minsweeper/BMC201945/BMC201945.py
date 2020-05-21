x=list(map(int, input().split()))
n3=x[0]
n2=x[1]
y=[]
for i in range(n3):
    inp=input()
    y.append(list(inp))
m=[]
for i in range(n3):
    m.append([])
for i in range (len(y)):
    for j in range (len(y[i])):
        if y[i][j]!='*':
           m[i].append(0)
        else:
            m[i].append('*' )         
def f(m):            
    n1=[]            
    for i in range (n2+4):
         n1.append(0)
    for i in range (len(m)):
        m[i]=[0,0]+m[i]+[0,0]
    return ([n1]+[n1]+m+[n1]+[n1])    
def g(m):
    for i in range (1,n3+3):
        for j in range (1,n2+3):
            if m[i][j]=='*':
                if m[i-1][j-1]!='*':
                    m[i-1][j-1] += 1
                if m[i-1][j]!='*':
                    m[i-1][j] +=1
                if m[i-1][j+1] != '*':
                    m[i-1][j+1] += 1
                if m[i][j-1]!='*':
                    m[i][j-1]+=1
                if m[i][j+1]!='*':
                    m[i][j+1]+=1
                if m[i+1][j-1]!='*':
                    m[i+1][j-1]+=1
                if m[i+1][j]!='*':
                    m[i+1][j]+=1
                if m[i+1][j+1]!='*':
                    m[i+1][j+1]+=1
    return m                    
k = g(f(m))
def p(h):
    q=[]
    for i in range (2,(len(h)-2)):
        h[i]=(h[i][2:])[:-2]
        q.append(h[i])
    return q  
a=[]
for i in p(k):
    a.append(list(map(str,i)))
def jbc(l):
    a=''
    for i in l:
        a=a+i
    return a
d=list(map(jbc,a))
for i in d:
    print (i)
print()        
