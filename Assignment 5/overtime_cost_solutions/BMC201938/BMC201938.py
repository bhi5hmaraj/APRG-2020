n ,d, r = map(int, input().split())
morn = list(map(int, input().split()))
afte = list(map(int, input().split()))
morn.sort()
afte.sort()
morn = morn[::-1]
over = 0
for i in range(n):
    if (morn[i] + afte[i] - d) > 0:
        over+=(morn[i] + afte[i] - d)
print(over * r)