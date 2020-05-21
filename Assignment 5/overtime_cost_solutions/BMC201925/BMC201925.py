n, d, r = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

a.sort(reverse = True)
b.sort()

ans = 0
for i in range(n):
    ans += max(0, a[i] + b[i] - d)*r
print(ans)