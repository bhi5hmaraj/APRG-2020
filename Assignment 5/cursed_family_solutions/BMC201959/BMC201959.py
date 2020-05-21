members = int(input())
generations = [[] for x in range(members + 1)]
fathers = []
sons2 = []
for i in range(members - 1):
    father, son = map(int, input().split())
    fathers.append(father)
    sons2.append(son)
    generations[father].append(son)

def great_father():
    for x in fathers:
        if x not in sons2:
            return x

def max_ind_set(x, e, f):
    for j in generations[x]:
        max_ind_set(j, e, f)
    e[x] = sum([max(e[k], f[k]) for k in generations[x]])
    f[x] = 1 + sum(e[k] for k in generations[x])
    return (e[x], f[x])

print(max(max_ind_set(great_father(), [0]*(members + 1), [0]*(members + 1))))
