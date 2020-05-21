import sys
sys.setrecursionlimit(10**6)

ls=list(map(int,input().split()))
n=ls[0]
d=ls[1]
r=ls[2]

ls1=list(map(int,input().split()))
ls2=list(map(int,input().split()))

def edgeCost(n1,n2):
    if n1+n2>d:
        return(n1+n2-d)
    else:
        return(0)
    
'''def minOvertime(N,l1,l2):
    if N == 1:
        a1=l1[0]
        b1=l2[0]
        return(edgeCost(a1,b1))
    else:
        ldd=[]
        for k in range(N):
            ldd.append(edgeCost(l1[0],l2[k])+minOvertime(N-1,l1[1:],l2[:k]+l2[k+1:]))
        return(min(ldd))'''

'''costTable = [[edgeCost(ii,jj) for ii in ls1] for jj in ls2]
def minOvertime(N,table):
    if N==1:
        return(min(table[0]))
    else:
        ld=[]
        for k in range(N):
            tab=table[1:]
            for j in tab:
                j=j[:k]+j[k+1:]
            ld.append(table[0][k] + minOvertime(N-1,tab))
        return(min(ld))'''

lr=[]
while ls1:
    lr.append(edgeCost(max(ls1),min(ls2)))
    ls1.remove(max(ls1))
    ls2.remove(min(ls2))

over=sum(lr)
print(over*r)
    
        


        
        
#print(minOvertime(n,costTable)*r)
#print((minOvertime(n,ls1,ls2))*r)