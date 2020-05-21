n,d,r=map(int, input().split())
l=[]

for i in range (n):
    l.append([])

for i in range(2):
    x = [int(x) for x in input().split()]
    l[i]=x
s=0
c=n-1
while(c>=0):

    m1=max(l[1])
    m2=min(l[0])
    if(m1+m2>d):
        s=s+((m1+m2)-d)*r
    l[1].remove(m1)
    l[0].remove(m2)
    c=c-1
if(s>0):
    print(s)
else:
    print(0)