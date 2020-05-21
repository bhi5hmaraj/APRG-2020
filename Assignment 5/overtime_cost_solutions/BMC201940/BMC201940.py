a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

n = int(a[0])
d = int(a[1])
r = int(a[2])

b.sort()
c.sort(reverse=True)
def fun(n) :
    l1 = []
    for i in range(0,n):
        if (b[i] + c[i] - d) > 0 :
         l1 = l1 + [r*(b[i] + c[i] - d)]
    return(l1)

print(sum(fun(n)))