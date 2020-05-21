n, d, r = map(int, input().split())
coco = list(sorted(map(int, input().split())))
lava = list(sorted(map(int, input().split()), reverse=True))

ans = 0
for a, b in zip(coco, lava):
    s = a+b
    if s > d: ans += s-d

print(ans * r)