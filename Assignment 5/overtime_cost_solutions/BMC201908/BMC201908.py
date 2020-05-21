s = str(input()).split()
n = int(s[0])
d = int(s[1])
r = int(s[2])
s = str(input()).split()
M = [int(x) for x in s]
M.sort()
s = str(input()).split()
E = [int(x) for x in s]
E.sort(reverse=True)
B = [0]*n
for i in range(n):
    x = M[i]
    y = E[i]
    if x + y <= d:
        B[i] = 0
    else:
        B[i] = (x + y - d)*r
cost = sum(B)
print(cost)