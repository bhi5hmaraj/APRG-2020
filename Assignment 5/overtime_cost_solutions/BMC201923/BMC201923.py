n,d,r=list(map(int,input().split()))
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
b.sort()
b.reverse()
ans=0
for i in range(n):
    ans+=max(a[i]+b[i]-d,0)

ans*=r
print(ans)
