m = input()
n = int(m)

l = []
for i in range(n - 1):
    l.append(tuple(input().split()))

if n == 1 or n == 2:
    print(1)

r = [(int(x), int(y)) for (x, y) in l]
p = [i + 1 for i in range(n)]
c = [y for (x, y) in r]

h = list(set(p) - set(c))[0]

family = dict()
parent = dict()

parent[h] = 0

for (x, y) in r:
    parent[y] = x

for i in p:
    family[i] = []

for (x, y) in r:
    family[x].append(y)

g1 = []
g2 = []

lone = [i for i in p if family[i] == []]
lpt = [parent[i] for i in lone]

def colour(f, x):
    if isinstance(x, int):
        par = parent[x]
        if par == 0:
            f[x].append('b')
        elif f[par][-1] == 'b':
            f[x].append('r')
        elif f[par][-1] == 'r':
            f[x].append('b')
        for i in f[x]:
            colour(f, i)
    return f

colour(family, h)

for i in p:
    if family[i][-1] == 'b':
        g1.append(i)
    elif family[i][-1] == 'r':
        g2.append(i)

if len(set(g1) - set(lpt)) > len(set(g2) - set(lpt)):
    g0 = list(set(g1) - set(lpt) - set(lone))
else:
    g0 = list(set(g2) - set(lpt) - set(lone))

g = len(g0) + len(lone)

print(g)