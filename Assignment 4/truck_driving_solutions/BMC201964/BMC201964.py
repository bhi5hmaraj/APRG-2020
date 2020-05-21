import sys
sys.setrecursionlimit(10**6)
def main():
    n,m =map(int, sys.stdin.readline().split(' '))
    edges = []
    for _ in range(m):
        u,v,w = map(int, sys.stdin.readline().split(' '))
        edges.append((w,u-1,v-1))


    q= int(input())
    qset = [set() for i in range(n)]


    for i in range(q):
        a,b = map(int, sys.stdin.readline().split(' '))
        a -= 1
        b -= 1
        qset[a].add(i)
        qset[b].add(i)


    edges = sorted(edges, key=lambda edge: edge[0])

    ps = [i for i in range(n)]

    def find(x):
        while ps[x] != x:
            x = ps[x]
        return x


    ans = [0]*(q)
    k=0
    for e in edges:
        a = find(e[1])
        b = find(e[2])
        if a != b:
            k += 1
            if len(qset[a]) < len(qset[b]):
                a, b = b, a
            for x in qset[b]:
                if x in qset[a]:
                    ans[x] = e[0]
                    qset[a].remove(x)
                else:
                    qset[a].add(x)
            ps[b] = a
            if(k == n-1):
                break

    for i in ans:
        print(i)

main()


