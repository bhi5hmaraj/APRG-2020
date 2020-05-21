
inNDR = list(map(int, input().split()))
n = inNDR[0]
d = inNDR[1]
r = inNDR[2]

morning = list(map(int, input().split()))
evening = list(map(int, input().split()))

morning = sorted(morning)
evening = sorted(evening)

work = 0
for i in range(0, n):
    work += max((morning[i] + evening[-i-1]) - d, 0)

ot = r * work

print(ot)
