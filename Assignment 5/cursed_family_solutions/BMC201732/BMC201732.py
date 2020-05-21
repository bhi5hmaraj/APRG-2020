n = int(input())

def max(x, y):  
    if(x > y): 
        return x 
    else: 
        return y 

class node : 
    def __init__(self): 
        self.data = 0
        self.parent = None
        self.children = []
    
    def insert(self, u):
        self.children.append(u)
        u.parent = self

memo = [-1]*n                
def LISS(root):  
    
    if root == None: 
        return 0
    
    if memo[root.data - 1] > 0:
        return memo[root.data - 1]
    
    size_excl = 0
    for i in root.children:
        size_excl += LISS(i)  
   
    size_incl = 1
    for i in root.children:
        for j in i.children:
            size_incl += LISS(j)
            
    memo[root.data - 1] = max(size_incl, size_excl)
    return memo[root.data - 1]

def newNode( data ) : 
  
    temp = node() 
    temp.data = data  
    temp.left = temp.right = temp.parent = None
    return temp  


l = []
for i in range(n):
    l.append(newNode(i+1))

for i in range(n-1):
    u, v = map(int, input().split())
    l[u-1].insert(l[v-1])

for i in range(n):
    if l[i].parent == None:
        root = l[i]
        break

p = LISS(root)
print(p)



   