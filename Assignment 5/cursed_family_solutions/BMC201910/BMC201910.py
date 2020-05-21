import sys
sys.setrecursionlimit(10**6)

n=int(input())
Tree={}
for jj in range(1,n+1):
    Tree[jj]=[]
Parents={}
for tt in range(1,n+1):
    Parents[tt]=[]
for jjj in range(n-1):
    lpp=list(map(int,input().split()))
    Tree[lpp[0]].append(lpp[1])
    Parents[lpp[1]]=lpp[0]
DPTree={}
for titi in range(1,n+1):
    DPTree[titi]=0
    
def update(dpTree):
    for node in Tree:
        if Tree[node]==[]:
            dpTree[node]=1
        else:
            a = 0
            for jk in Tree[node]:
                a=a+dpTree[jk]
            b=0
            for k in Tree[node]:
                if Tree[k]==[]:
                    b=b
                else:
                    for ii in Tree[k]:
                        b=b+dpTree[ii]
            dpTree[node]=max(a,1+b)
    return(dpTree)
        


'''def indSetSize(node):
    if (Tree[node]==[]):
        return(1)
    else:
        a = 0
        for jk in Tree[node]:
            a=a+indSetSize(jk)
        b=0
        for k in Tree[node]:
            if Tree[k]==[]:
                b=b
            else:
                for ii in Tree[k]:
                    b=b+indSetSize(ii)
        return(max(a,1+b))'''
        

for kil in Parents:
    if Parents[kil]==[]:
        Parent=kil

while DPTree[Parent] != update(DPTree)[Parent]:
    DPTree=update(DPTree)

print(DPTree[Parent])



        

        