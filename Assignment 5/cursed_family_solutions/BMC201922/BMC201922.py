inf, c, r, a1, a2, ar = int(10e7+1), 0, -1, [], [], []
n = int(input())
while (c < n):
    a1.append([])
    a2.append(-inf)
    c+=1
for i in range(n-1):
    dad,son = map(int,input().split())
    a2[son-1] = dad
    a1[dad-1].append(son)

for i in range(n):
    if(a2[i] == -inf):
        r = i+1

a = [0 for i in range(n)]
for j in range(n):
    if a1[j] == [] :
        ar.append(j+1)
for i in range(inf):
    if ar == [] :
        break
    qq = ar.pop(0)
    if(a1[qq-1] == []):
        a[qq-1] = 1
    else:
        p, q = 0, 1
        for j in a1[qq-1]:
            p += a[j-1]
            if(a1[j-1] != []):
                for i in a1[j-1]:
                    q += a[i-1]
        a[qq-1] = max(q, p)
    if(a2[qq-1] != -inf):
        ar.append(a2[qq-1])
print(a[r-1])