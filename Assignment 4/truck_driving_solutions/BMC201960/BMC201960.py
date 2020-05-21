nofcities_and_nofroads = input().split()
nofcities = int(nofcities_and_nofroads[0])
nofroads = int(nofcities_and_nofroads[1])

l = []
for i in range(nofroads):
    l.append(tuple(input().split()))
roads = [(int(x), int(y), int(z)) for (x, y, z) in l]

m = []
nofqueries = int(input())
for i in range(nofqueries):
    m.append(tuple(input().split()))
queries = [(int(x), int(y)) for (x, y) in m]

country = dict()
for i in range(nofcities):
    country[i + 1] = []

cities = list(country)

for (x, y, z) in roads:
    country.get(x).append((y, z))
    country.get(y).append((x, z))

def find_paths(graph, start, end, path):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for (x, y) in graph[start]:
        if x not in path:
            npaths = find_paths(graph, x, end, path)
            for npath in npaths:
                paths.append(npath)
    return paths

for (x, y) in queries:
    all_paths = find_paths(country, x, y, [])
    u = []
    for i in all_paths:
        p = []
        for j in range(len(i) - 1):
            h = [z for (t, z) in country.get(i[j]) if t == i[j + 1]]
            p.append(h[0])
        u.append(max(p))
    print(min(u))