ndr = input().split()
n = int(ndr[0])
d = int(ndr[1])
r = int(ndr[2])

h = []
for i in range(2):
    h.append(input().split())

h1 = [int(i) for i in h[0]]
h2 = [int(i) for i in h[1]]

sh1 = sum(h1)
sh2 = sum(h2)
if (sh1 + sh2) > (n * d):
    print(((sh1 + sh2) - (n * d)) * r)
else:
    print(0)