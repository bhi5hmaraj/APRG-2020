n,d,r  = map(int, input().split())

l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
l1.sort()
l2.sort()

ans = 0
for i in range(n):
    if(l1[i] + l2[n-i-1] - d > 0):
        ans += (l1[i] + l2[n-i-1] - d)*r
print(ans)