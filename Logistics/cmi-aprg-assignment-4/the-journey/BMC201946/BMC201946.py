'''

Program to solve the problem Journey in APRG Assignment

'''


import heapq

#function to implement dijkstra
def dijkstra(src):
    distance = [-1] * (100*n)
    distance[src] = 0

    pq = [(0,src)]

    while len(pq) > 0:
        dist,u = heapq.heappop(pq)
        if dist > distance[u]:
            continue
        for temp in graph[u]:
            v = temp[0]
            w = temp[1]
            temp_dist = dist + w 
            if temp_dist < distance[v] or distance[v] == -1:
                distance[v] = temp_dist
                heapq.heappush(pq, (temp_dist,v))

    return distance

#define infinity
inf = 1000000000

#first line of input
s = str(input()).split()
n = int(s[0])
dest = int(s[1])

#second line of input
time_taken = []
s = str(input()).split()
for i in s:
    time_taken.append(int(i))

#bus_stops[i] represents bus stops serviced by driver i
bus_stops = [[] for i in range(n)]
for i in range(n):
    s = str(input()).split()
    for j in s:
        bus_stops[i].append(int(j))

#adjacency list representation of graph
graph = [[] for i in range(100*n)]

#add edges representing switch of driver with weight 60
for i in range(100):
    for j in range(n):
        for k in range(n):
            graph[i + (100*k)].append([i + (100*j), 60])

#add edges between bus stops serviced by each driver 
for i in range(n):
    stops_i = bus_stops[i]
    for a in stops_i:
        for b in stops_i:
            temp = a-b
            if temp<0:
                temp = (-1)*temp
            time = temp*time_taken[i]
            graph[100*i + a].append([100*i + b,time])

#distance[i] is the list of distances of all nodes from all 0's aka 0,100,200,...,(n-1)*100
distance = [[] for i in range(n)]
for i in range(n):
    distance[i] = dijkstra(100*i)
#for all possible start nodes (100*i) and destination nodes(100*j + dest) find the min. dist.
min_dist = -1
for i in range(n):
    for j in range(n):
        u = 100*i 
        v = 100*j + dest
        temp = distance[i][v]
        if temp != inf:
            if min_dist == -1 or min_dist > temp:
                min_dist = temp
#print answer
if min_dist == -1:
    print("IMPOSSIBLE")
else:
    print(min_dist)
