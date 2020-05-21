from queue import Queue 

#my implementation of min-heaps
class minheap:
    def __init__(self , n):
        self.Heap = [(-1,-1)]
        self.positions = [-1]
        for i in range(n):
            self.positions.append(-1)
    def parent(self , pos):
        return (pos // 2)
    def leftChild(self , pos):
        return (2 * pos)
    def rightChild(self , pos):
        return (2 * pos) + 1
    def isLeaf(self , pos):
        if pos >= ((len(self.Heap) - 1)//2) and pos <= len(self.Heap) - 1: 
            return True
        return False
    def swap(self , pos1 , pos2):
        self.Heap[pos1], self.Heap[pos2] = self.Heap[pos2], self.Heap[pos1]
        self.positions[self.Heap[pos1][0]] = pos1
        self.positions[self.Heap[pos2][0]] = pos2
    def minHeapify(self , pos):
        while(self.isLeaf(pos) == 0):
            if (self.Heap[pos][1] > self.Heap[self.leftChild(pos)][1] or 
                self.Heap[pos][1] > self.Heap[self.rightChild(pos)][1]):
                if (self.Heap[self.leftChild(pos)][1] < self.Heap[self.rightChild(pos)][1]):
                    self.swap(pos , self.leftChild(pos))
                    pos = self.leftChild(pos)
                else:
                    self.swap(pos , self.rightChild(pos))
                    pos = self.rightChild(pos)
            else:
                return
    def insert(self , element):
        self.Heap.append(element)
        self.positions[element[0]] = len(self.Heap) - 1
        current = len(self.Heap) - 1
        while (current != 1 and self.Heap[current][1] < self.Heap[self.parent(current)][1]):
            self.swap(current , self.parent(current))
            current = self.parent(current)
    def remove(self):
        if (len(self.Heap) - 1 > 1):
            self.swap(1 , len(self.Heap) - 1)
        popout = self.Heap.pop()
        if (len(self.Heap) - 1 > 0):
            self.minHeapify(1)
        return popout
    #make sure that the new value is less than the original one (min heap)
    def update(self , vertex , value):
        self.Heap[self.positions[vertex]] = (vertex , value)
        current = self.positions[vertex]
        while (current != 1 and self.Heap[current][1] < self.Heap[self.parent(current)][1]):
            self.swap(current , self.parent(current))
            current = self.parent(current)
#defining infinity
infty = 100000000000
            
#taking the graph info
inp = list(input().split())
N = int(inp[0])
M = int(inp[1])

#making the adjacency list and shortest distance arrays
adj = [[]]
shor1 = [-1]
shorN = [-1]
color1 = [-1]
colorN = [-1]
for i in range(N):
    adj.append([])
    shor1.append(-1)
    shorN.append(-1)
    color1.append(0)
    colorN.append(0)
for i in range(M):
    inp = list(input().split())
    adj[int(inp[0])].append((int(inp[1]) , int(inp[2])))
    adj[int(inp[1])].append((int(inp[0]) , int(inp[2])))

#implementing dijkstra
def dijkstra(source , storeArray , colorArray):
    mh = minheap(N)
    mh.insert((source , 0))
    colorArray[source] = 1
    
    while(len(mh.Heap) - 1 > 0):
        top = mh.remove()
        el = top[0]
        storeArray[el] = top[1]
        colorArray[el] = 2
        
        for i in range(len(adj[el])):
            neig = adj[el][i][0]
            weight = adj[el][i][1]
            tem = weight + top[1]
            if(colorArray[neig] == 0):
                colorArray[neig] = 1
                mh.insert((neig , tem))
            elif(colorArray[neig] == 1):
                if(tem < mh.Heap[mh.positions[neig]][1]):
                    mh.update(neig , tem)
dijkstra(1 , shor1 , color1)
dijkstra(N , shorN , colorN)

#final ans temp
temp = infty

for i in range(1 , N + 1):
    #if the vertex doesn't lie on a shortest path
    if (shor1[i] + shorN[i] > shor1[N]):
        temp = min(temp , shor1[i] + shorN[i])
    #if it does
    else:
        for j in range(len(adj[i])):
            #if the edge doesn't lie on a shortest path
            if (shor1[i] + adj[i][j][1] + shorN[adj[i][j][0]] > shor1[N]):
                temp = min(temp , shor1[i] + adj[i][j][1] + shorN[adj[i][j][0]])
print(temp)

