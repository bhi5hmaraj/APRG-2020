l=list(map(int,input().split()))
n=l[0]
children={}
lmst={}
p=[]
for i in range (1,n+1):
    children[i]=[]
    lmst[i]=[]
for i in range (1,n):
    z=input().split()
    u=int(z[0])
    v=int(z[1])
    children[u].append(v)
if i in children:
    x=i
def lenofmst(x):
        if len (children[x])==0:
            f= 1
        if lmst[x]!=[]:
            return lmst[x][0]
        else:
            a=0
            b=0
            for i in children[x]:
                a=a+lenofmst(i)
                if len(children[i])!=0:
                    for j in children[i]:
                        b=b+lenofmst(j)
            f=max(b+1,a)       
        lmst[x].append(f)
        return f
for i in children:
    p.append(lenofmst(i))
print (max (p))        
                
            
                

    