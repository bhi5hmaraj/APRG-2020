[n, d, r] = input().split()
n = int(n)
d = int(d)
r = int(r)
morn = input().split()
afternoon = input().split()
for i in range(n):
    morn[i] = int(morn[i])
    afternoon[i] = int(afternoon[i])
morn.sort()
afternoon.sort(reverse = True)
overtime = 0
for i in range(n):
    time = morn[i] + afternoon[i] - d
    if time > 0:
        overtime = overtime + time * r
        
print(overtime)
    