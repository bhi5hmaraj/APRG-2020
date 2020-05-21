n,d,l=map(int,input().split())
m=list(map(int,input().split()))
ni=list(map(int,input().split()))
#print(1)
m.sort()
ni.sort()
#print(m)
a=0
for i in range(n):
    c=m[i]+ni[n-i-1]
    if c>d:
        c=c-d
    else:
        c=0
    a+=c
print(a*l)