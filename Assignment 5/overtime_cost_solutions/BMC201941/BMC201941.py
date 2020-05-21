l = list(map(int,input().split()))
m = sorted(list(map(int,input().split())))
n = sorted(list(map(int,input().split())))
n = n[::-1]
k = []
for i in range(0,l[0]):
    u = m[i]+n[i]-l[1]
    if u > 0:
        k.append(l[2]*u)
if k != []:
    print(sum(k))
else:
    print(0)