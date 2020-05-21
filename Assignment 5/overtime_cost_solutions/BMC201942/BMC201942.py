n, d, r = map(int, input().split())
morn_list = list(map(int, input().split()))
eve_list = list(map(int, input().split()))

morn_list.sort()
eve_list.sort()
eve_list.reverse()

extra_hrs = 0
for i in range(n):
    if morn_list[i] + eve_list[i] > d:
        extra_hrs += (morn_list[i] + eve_list[i] - d)

print(extra_hrs*r)