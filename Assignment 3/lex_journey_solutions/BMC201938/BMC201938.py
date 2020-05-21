n_m = list(map(int, input().split()))
n = n_m[0]
m = n_m[1]
x_y = list(map(int, input().split()))
x = x_y[0]
y = x_y[1]
l1 = []
i1 = list(map(str, input().split()))
l1.append(i1)
for i in range(m-1):
    inp = list(map(str, input().split()))
    ans = 0
    #if len(l1) > 0:
    for k in l1:
        if (int(k[-1]) == int(inp[0])):
            k.append(inp[1])
            k.append(inp[2])
            ans+=1
    if ans != len(l1):
        l1.append(inp)
l2 = []
for i in l1:
    if int(i[0]) == x and int(i[-1]) == y:
        l2.append(i)
l2.sort(key = len)
l = len(l2[0])
#abc = 0
#for i in l2:
#    if len(i) == l:
#        abc+=1
#print((abc * (l-2) + 2))
ac = l2[0]
abc = ''
for i in range(l//2):
    abc = abc + ac[2*i + 1]
print(abc)
#print(l1)
#print(l2)