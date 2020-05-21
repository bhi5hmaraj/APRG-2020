n, d, r = list(map(int, input().split()))
mornin = sorted(list(map(int, input().split())))
afternoon = list(reversed(sorted(((list(map(int, input().split())))))))
cost=0
for i in range(n):
    if mornin[i]+afternoon[i]>d:
        cost = cost+mornin[i]+afternoon[i]-d
print(cost*r)