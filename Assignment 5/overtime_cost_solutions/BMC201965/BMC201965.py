n,d,r = list(map(int, input().split()))
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
a1.sort()
a2.sort()
a2.reverse()
s = sum([a1[i]+a2[i]-d for i in range(n) if a1[i]+a2[i]>d])
print(r*s)
