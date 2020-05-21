def BFS(source, shortest_distance):
    queue = []
    queue.append(source)
    shortest_distance[source] = 0
    while queue:
        temp = queue.pop(0)
        for i in range(len(adj_list[temp])):
            j = adj_list[temp][i][0]
            if shortest_distance[j] == -1:
                shortest_distance[j] = 1 + shortest_distance[temp]
                queue.append(j)


def find_path():
    if x == y:
        return ""
    s = ""
    nodeset = [x]
    nodeset1 = []
    while len(nodeset) != 0:
        min_cha = None
        flag = 0
        for i in nodeset:
            if min_cha == None or min_cha > min_char[i]:
                min_cha = min_char[i]
        s = s + min_cha 
        for i in range(len(nodeset)):
            if min_char[nodeset[i]] == min_cha:
                for j in range(len(adj_list[nodeset[i]])): 
                    nd = nodeset[i]
                    val = adj_list[nd][j][0]
                    cha = adj_list[nd][j][1]
                    if val == y:
                        flag = 1
                        break
                    if shortest_distance_x[nd]+1+shortest_distance_y[val] == shortest_distance_x[y] and cha == min_cha and visited[val] == 0:
                        visited[val] = 1
                        nodeset1.append(val)
        if flag == 1:
            break
        nodeset = nodeset1
        nodeset1 = []

    return s

s = str(input()).split()
n = int(s[0])
m = int(s[1])

s = str(input()).split()
x = int(s[0])
y = int(s[1])

shortest_distance_x = [(-1) for i in range(n+1)]
shortest_distance_y = [(-1) for i in range(n+1)]
min_char = [None for i in range(n+1)]
visited = [0  for i in range(n+1)]
adj_list  = [[] for i in range(n+1)]

for i in range(m):
    s = str(input()).split()
    u = int(s[0])
    v = int(s[2])
    c = s[1]
    adj_list[u].append([v,c])
    adj_list[v].append([u,c])



BFS(x, shortest_distance_x)
BFS(y, shortest_distance_y)

for i in range(1,n+1):
    if shortest_distance_x[i] + shortest_distance_y[i] == shortest_distance_x[y]:
        temp = None 
        for j in range(len(adj_list[i])):
            val = adj_list[i][j][0]
            cha = adj_list[i][j][1]
            if shortest_distance_x[i] + 1 + shortest_distance_y[val] == shortest_distance_x[y]:
                if temp == None:
                    temp = cha 
                elif cha < temp:
                    temp = cha 
                else:
                    continue
        min_char[i] = temp 

print(find_path())

