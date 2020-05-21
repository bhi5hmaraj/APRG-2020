li = list(map(int, input().split()))
n = li[0]
k = li[1]
A = [[] for i in range(100)]
T = list(map(int, input().split()))
li = [[] for i in range(n)]
for i in range(n):
    li[i] = list(map(int, input().split()))
    for j in li[i]:
        A[j].append(i)
        
def inc(i,j):
    if i == j:
        return 0
    else:
        return 60
mark = [ 0 for i in range(100)]
distance = [10000000000 for i in range(100)]
mark[0] = 1
distance[0] = 0
import heapq
"""l = []                         # list of entries arranged in a heap
entry_finder = {}               # mapping of tasks to entries
REMOVED = '<removed-task>'      # placeholder for a removed task
counter = itertools.count()     # unique sequence count

def add_task(task, priority=0):
    'Add a new task or update the priority of an existing task'
    if task in entry_finder:
        if entry_finder[task][0] <= priority:
            return
        else:
            remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heappush(pq, entry)

def remove_task(task):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED

def pop_task():
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while pq:
        priority, count, task = heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('pop from an empty priority queue')
c = 1"""
h = []
for i in A[0]:
    for v in li[i]:
        if T[i]*v < distance[v]:
            distance[v] = T[i]*v
            heapq.heappush(h, (T[i]*v,i,v))
while h!=[]:
    a = heapq.heappop(h)
    if mark[a[2]] == 1:
        continue
    for i in A[a[2]]:
        for v in li[i]:
            if a[0]  + T[i]*abs(v-a[2]) + inc(i,a[1]) < distance[v]:
                distance[v] = a[0]  + T[i]*abs(v-a[2]) + inc(i,a[1])
                heapq.heappush(h, (a[0]  + T[i]*abs(v-a[2]) + inc(i,a[1]),i, v))
    mark[a[2]] = 1
    
    
if mark[k] == 0:
    print("IMPOSSIBLE")
else:
    print(distance[k])            
    
    
          
              

    

