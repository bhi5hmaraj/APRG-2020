def ot(l1,l2):
    x=0
    l3=[0]*n
    l1.sort()
    l2.sort(reverse=True)
    for i in range(n):
        l3[i]=max(l2[i]+l1[i]-d,0)
    for i in range(n):
        x=x+l3[i]*r
    print(x)
n,d,r=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
ot(l1,l2)
