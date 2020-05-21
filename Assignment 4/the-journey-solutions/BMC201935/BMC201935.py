input1 = [int(x) for x in input().split()]
n = input1[0]
endjourney = input1[1]
source = [[] for i in range(n*100)]
timer = [int(x) for x in input().split()]
disttime = {}
busstop = [[int(x) for x in input().split()]for i in range(n)]
newstop = []
import heapq
def mintime(k):
    time = [float("Inf")]*(501)
    l = []
    for i in range(n):
        time[100*i] = 0
        journey = [0]*(501)
        if 100*i in newstop:
            heap = [(0, 100*i)]
            heapq.heapify(heap)
            while heap:
                (t, a) = heapq.heappop(heap)
                if journey[a] == 0:
                    journey[a] = 1
                for b in source[a]:
                    if journey[b] == 0 and time[a] + disttime[(a,b)] <= time[b]:
                        time[b] = time[a] + disttime[(a,b)]
                        heapq.heappush(heap, (time[b], b))
        for j in range(n):
             if time[100*j + endjourney] != float("Inf"):
                 l.append(time[100*j + endjourney])
             else:
                 l = l
    if l == []:
        print("IMPOSSIBLE")
    else:
        print(min(l))
for i in range(n):
    for s in busstop[i]:
       newstop.append(100*i + s)    
    for j in range(len(busstop[i]) - 1):
        a, b = 100*i + busstop[i][j], 100*i + busstop[i][j+1]
        source[a].append(b)
        disttime[(a, b)] = (b-a)*timer[i]
        source[b].append(a)
        disttime[(b, a)] = (b-a)*timer[i]
        

    for j in range(len(busstop[i])):
        if busstop[i][j] == 0: continue
        a  = 100*i + busstop[i][j]
        for k in range(i + 1, n):
            c = 100*k + busstop[i][j]
            if busstop[i][j] in busstop[k]:
                source[a].append(c)
                disttime[(a, c)] = 60
                source[c].append(a)
                disttime[(c, a)] = 60
    

mintime(endjourney)        
                         

           
