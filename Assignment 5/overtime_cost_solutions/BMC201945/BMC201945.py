n,d,r=map(int,input().split())
mrng=list(map(int,input().split()))
aft=list(map(int,input().split()))
def mergesort(l):
  if len(l)>1:
    p=[]
    m=len(l)//2
    L=mergesort(l[m:])
    M=mergesort(l[:m])
    a=0
    b=0
    while a<len(L) and b<len(M):
      if L[a]<M[b]:
        p.append(L[a])
        a += 1
      else:
        p.append(M[b])
        b += 1
    while a<len(L):
      p.append(L[a])
      a += 1
    while b<len(M):
      p.append(M[b])
      b += 1
  else:
    p=l
  return p    
l=mergesort(mrng)
m=mergesort(aft)
N=len(l)
x=0
for i in range (N):   
  if l[i]+m[N-1-i]>d:
    x=x+l[i]+m[N-1-i]-d
print(x*r)      