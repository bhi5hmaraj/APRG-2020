n = int(input())
famtree = [[] for i in range(n+1)]
sons = []
fathers = []
for i in range(n-1):
    a, b = map(int, input().split())
    fathers.append(a)
    sons.append(b)
    famtree[a].append(b)

root = []
for i in fathers:
    if i not in sons:
        root.append(i)
root_father = root[0]

A = [0]*(n+1)
B = [0]*(n+1)

def biggest_gathering(a):
    for i in famtree[a]:
        biggest_gathering(i)
    A[a] = sum(max(A[j], B[j]) for j in famtree[a])
    B[a] = sum(A[j] for j in famtree[a]) +1
    return max(A[a], B[a])

print(biggest_gathering(root_father))
