n, d, r = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse=True)
c = 0
for i in range(n):
    c += max(a[i] + b[i] - d, 0)
c *= r
print(c)
