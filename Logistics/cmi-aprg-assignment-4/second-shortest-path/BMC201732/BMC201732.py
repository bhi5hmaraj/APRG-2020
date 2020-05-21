import heapq #need it for heap data structure in dijkstra
import sys
#first input
N, M = map(int, input().split())
arr = [[] for i in range(N)]
#add weights
for j in range(M):
  s = list(map(int, input().split()))
  arr[s[0]-1].append((s[1],s[2])) #add weight
  arr[s[1]-1].append((s[0],s[2])) #add weight
  #set the largest list size
maxi = [(sys.maxsize, sys.maxsize) for i in range(N)]
maxi[0] = (0, sys.maxsize)
#inititalizing queue
queue = [(0,1)]
while queue != [] and queue[0][0]!= sys.maxsize:
  heap = heapq.heappop(queue)    #heapification here
  ind = arr[heap[1]-1]
  for count in ind:
    (a, b) = maxi[count[0]-1]
    if b > heap[0]+count[1] >= a:
      if a == heap[0]+count[1]:
        if maxi[heap[1]-1][1] + count[1] < b:
          maxi[count[0]-1] = (a, maxi[heap[1]-1][1]+count[1])
          heapq.heappush(queue, (a, count[0]))  #push out       
      else:        
        maxi[count[0] - 1] = (a, heap[0] + count[1])
        heapq.heappush(queue, (a, count[0]))  #push out
    elif a > heap[0]+count[1]:
      maxi[count[0]-1] = (heap[0]+count[1], a)
      heapq.heappush(queue, (heap[0]+count[1], count[0])) #push out
p =  maxi[N-1][1] #second shortest path        
print(p)
