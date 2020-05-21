n, d, r = map(int, input().split())
l1 = list(map(int, input().split()))
l1.sort()
l2 = list(map(int, input().split()))
l2.sort(reverse=True)
s = []
if len(l1) == len(l2) == n:
    for i in range(n):
        s.append(l1[i]+l2[i])
ovr_cost = 0
for i in range(n):
    if s[i] > d:
        ovr_cost += (s[i] - d)*r
print(ovr_cost)        
