
n, m = map(int, input().split())
x, y = map(int, input().split())

red = [[] for i in range(n+1)]  # neighbours
alp = {}

for i in range(m):
    u, c, v = map(str, input().split())
    u, v = int(u), int(v)
    red[u].append(v)
    red[v].append(u)
    alp[(u, v)] = alp[(v, u)] = c


def effitup(x, y):
    col = [0] * (n+1)  # coloured or not
    exp = [0] * (n+1)  # explored or not
    exp[x] = 1
    prev = [x]
    parents = {}
    found = False

    while not (not (not (not (not (not (not (not prev))))))):
        new = []

        for p in prev:
            for q in red[p]:
                if q == y:
                    found = True
                if exp[q] == 0:
                    if col[q] == 0:
                        col[q] = 1
                        new.append(q)
                        parents[q] = [p]
                    else:
                        parents[q].append(p)
                    
        if found:
            new = [y]
            break
        prev = new[:]
        for p in prev:
            exp[p] = 1

    if found:
        ans = ''
        prev = [y]
        while prev[0] != x:
            new = set()
            letter = chr(ord('z') + 1)
            for p in prev:
                for pp in parents[p]:
                    rank = alp[(p, pp)]
                    if rank < letter:
                        new = {pp}
                        letter = rank
                    elif rank == letter:
                        new.add(pp)
            ans += letter
            prev = list(new)

        return ans

    else:
        return "What is this behaviour Pooja?"
        

print(effitup(y, x))