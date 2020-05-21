x = 0
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
l3 = list(map(int, input().split()))
l2 = sorted(l2)
l3 = sorted(l3, reverse = True)
for i in range(l1[0]):
    if(l2[i]+l3[i] > l1[1]):
        x += (l1[2]*(l2[i]+l3[i]-l1[1]))
print(x)