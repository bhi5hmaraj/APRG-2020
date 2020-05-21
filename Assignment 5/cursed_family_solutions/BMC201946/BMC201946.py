def solve():
    #find levels array
    visited = [False] * n
    dist = [-1] * n 
    queue = []
    visited[0] = True
    queue.append(0)
    dist[0] = 0
    max_dist = 0
    while queue:
        u = queue.pop(0)
        for v in graph[u]:
            if visited[v] == False:
                visited[v] = True
                queue.append(v)
                dist[v] = dist[u] + 1
                max_dist = max(max_dist,dist[v])
    levels = [[] for i in range(max_dist+1)]
    for i in range(n): 
        levels[dist[i]].append(i)

    answer = [0 for i in range(n)]

    ite = max_dist

    while ite >= 0:
        nodes_at_cur_level = levels[ite]
        ite = ite-1
        for i in nodes_at_cur_level:
            temp1 = 0
            for j in graph[i]:
                if dist[j] > dist[i]:
                    temp1 = temp1 + answer[j]
            temp2 = 0
            for j in graph[i]:
                if dist[j]>dist[i]:
                    for k in graph[j]:
                        if dist[k]>dist[j]:
                            temp2 = temp2 + answer[k]
            answer[i] = max(temp1,temp2+1)

    return answer[0]

s = str(input()).split()
n = int(s[0])
graph = [[] for i in range(n)]
for i in range(n-1):
    s = str(input()).split()
    u = int(s[0]) - 1
    v = int(s[1]) - 1
    graph[u].append(v)
    graph[v].append(u)
print(solve())