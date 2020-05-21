li = list(map(int, input().split()))
n = li[0]
d = li[1]
r = li[2]
l0 = list(map(int, input().split()))
l1 = list(map(int, input().split()))
l0.sort()
l1.sort(reverse=True)
c = 0
for i in range(n):
    c = c + max(0,(l1[i] + l0[i]-d)*r)
print(c)                