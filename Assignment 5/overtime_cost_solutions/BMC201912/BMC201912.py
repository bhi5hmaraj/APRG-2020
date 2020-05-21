n, d, r = [int(x) for x in input().split()]
l1 = [int(x) for x in input().split()]
l2 = [int(x) for x in input().split()]
l1.sort()
l2.sort()
s = 0
for i in range(n):
    s += r*max(l1[i] + l2[n-1-i]-d, 0)
print(s)