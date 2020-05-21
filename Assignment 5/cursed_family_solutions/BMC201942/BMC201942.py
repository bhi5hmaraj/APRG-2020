from collections import defaultdict

parent = defaultdict(None)
children = defaultdict(set)

memo = {}
root = -1
def largest_family(n):
    if not children[n]:
        memo[n] = 1
    elif n not in memo:
        lst = [children[i] for i in children[n]]
        included = set.union(*lst)
        p1 = sum(map(largest_family, included))
        p2 = sum(map(largest_family, children[n]))
        memo[n] = max(p1 + 1, p2)
    return memo[n]


n = int(input())
for i in range(n-1):
    u, v = map(int, input().split())
    children[u-1].add(v-1)
    parent[v-1] = u-1
for i in range(n):
    if i not in parent:
        root = i
        break
print(largest_family(root))