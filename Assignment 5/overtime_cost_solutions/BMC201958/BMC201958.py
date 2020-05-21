n, d, r = list(map(int,input().split()))
l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
l3 = sorted(l1)
l4 = sorted(l2)[::-1]

l = [sum(x) for x in zip(l3, l4)]
overtime = []
for i in range(n):
    if l[i] < d:
        overtime.append(0)
    else:
        overtime.append((l[i]-d)*r)
print(sum(overtime))