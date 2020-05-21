from queue import Queue
n,m=map(int,input().split())
x,y=map(int,input().split())
A=[]
sh_x=[]
sh_y=[]
mi=[]
s=[]
for i in range(n+1):
    A.append([])
    sh_x.append(-1)
    sh_y.append(-1)
    mi.append(None)
    s.append(0)
for i in range(m):
    a,c,b=map(str,input().split())
    a,b=int(a),int(b)
    A[a].append([b,c])
    A[b].append([a,c])
def kohli(src):
    queue=Queue()
    if src==x:
        sh_x[src]=0
    else:
        sh_y[src]=0
    queue.put(src)
    while (queue.empty()==0):
        e=queue.get()
        for i in range(len(A[e])):
            j=A[e][i][0]
            if src==x:
                if(sh_x[j]==-1):
                    sh_x[j] = 1 + sh_x[e]
                    queue.put(j)
            else:
                if(sh_y[j]==-1):
                    sh_y[j]=1+sh_y[e]
                    queue.put(j)
kohli(x)
kohli(y)
def anushka():
    for i in range(n+1):
        if i==0:
            continue
        if(sh_x[i]+sh_y[i]==sh_x[y]):
            temp=None
            for j in range(len(A[i])):
                k = A[i][j][0]
                l = A[i][j][1]
                if (sh_x[i]+1+sh_y[k]==sh_x[y]):
                    if (temp==None):
                        temp=l
                    elif (l<temp):
                        temp=l
            mi[i]=temp
anushka()
def virushka():
    path=""
    t=[x]
    Empty=[]  
    while(len(t)!= 0):
        temp=None
        c=0
        for i in range(len(t)):
            if(temp==None or temp>mi[t[i]]):
                temp=mi[t[i]]
        path=path + temp
        for i in range(len(t)):
            if(mi[t[i]]==temp):
                for j in range(len(A[t[i]])):
                    node=A[t[i]][j][0]
                    q=A[t[i]][j][1]
                    if(node==y):
                        c=1
                        break
                    if(sh_x[t[i]]+1+sh_y[node]==sh_x[y] and q==temp and s[node]==0):
                        s[node]=1
                        Empty.append(node)
        if(c):
            break
        t=Empty
        Empty=[]
    return path
if(x==y):
    print("")
else:
    print(virushka())