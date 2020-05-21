
in_list = [int(x) for x in input().split()]
n = in_list[0]
m = in_list[1]
start_end = [int(x) for x in input().split()]
start = start_end[0]
end = start_end[1]
neighbours = [[] for i in range(n+1)]
alphabets = dict()
for i in range(m):
    x, alpha, y = input().split()
    x = int(x)
    y = int(y)
    neighbours[x].append(y)
    neighbours[y].append(x)
    alphabets[(x,y)] = alpha
    alphabets[(y,x)] = alpha

def lexixographic_Journey_Prerequisite(initial, goal):
    coloured = [0] * (n + 1)
    visited = [0] * (n + 1)
    visited[initial] = 1
    previous = [initial]
    parents = {}
    got = False

    while previous:
        newone = []
        for i in previous:
            for j in neighbours[i]:
                if j == goal: got = True
                if visited[j] == 0:
                    if coloured[j] == 0:
                        coloured[j] = 1
                        newone.append(j)
                        parents[j] = [i]
                    else:
                        parents[j].append(i)
        if got:
            newone = [goal]
            break
        previous = newone[:]
        for g in previous:
            visited[g] = 1
    if got:
        answer = ""
        previous = [goal]
        while True:
            if previous[0] == initial: break
            newone = set()
            alpha = 'z'
            for fi in previous:
                for pr in parents[fi]:
                    beta = alphabets[(fi,pr)]
                    if beta < alpha:
                        newone = set([pr])
                        alpha = beta
                    elif beta == alpha: newone.add(pr) 

            previous = list(newone)
            answer += alpha
        return answer
    else:
        return 0


print(lexixographic_Journey_Prerequisite(end, start))