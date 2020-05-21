a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
b.sort()
c.sort(reverse = True)
x = 0
for i in range(a[0]):
    if b[i] + c[i] > a[1]:
        x = x + b[i] + c[i] - a[1]
print(x*a[2])