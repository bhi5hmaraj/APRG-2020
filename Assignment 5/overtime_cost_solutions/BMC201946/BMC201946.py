s = str(input()).split()
n = int(s[0])
d = int(s[1])
r = int(s[2])

s = str(input()).split()
morn = []
for i in range(n):
    morn.append(int(s[i]))

s = str(input()).split()
even = []
for i in range(n):
    even.append(int(s[i]))

morn.sort()
even.sort(reverse=True)

ans = 0
for i in range(n):
    work = morn[i]+even[i]
    if work > d:
        overtime = (work-d)*r 
        ans = ans + overtime

print(ans)