a= list(map(int,input().split()))
b= list(map(int,input().split()))
c= list(map(int,input().split()))
b.sort()
c.sort()
n=a[0]
d=a[1]
r=a[2]
hours=0
for i in range(0,n):
    if b[i]+c[n-1-i]>d:
        hours=hours+b[i]+c[a[0]-1-i]-a[1]
overtimecost=hours*r
print(overtimecost)