class Node:
    def __init__(self, val = 0):
        self.value = val
        self.left = None
        self.right = None
        self.parent = None
        self.size = 1 #Size of subtree rooted at each node
        self.color = "red"
    
leaf = Node()
leaf.color = "black"
leaf.size = 0

def recolor(x, uncle):
    leaf.color = "black"
    x.parent.color = "black"
    x.parent.parent.color = "red"
    uncle.color = "black"
        
class RedBlackTree:
    def __init__(self):
        self.root = leaf
    
    def leftRotate(self, x):    
        y = x.right
        l = y.left
        size_y = y.size
        if (x == self.root):
            self.root = x.right
        y.left = x
        y.parent = x.parent
        if (x.parent != leaf):
            if (x.parent.left == x):
                x.parent.left = y
            else:
                x.parent.right = y
        x.parent = y
        x.right = l
        
        if (l != leaf):
            l.parent = x
            
        x.size = x.size + l.size - size_y
        y.size = y.size + x.size - l.size
    
    def rightRotate(self, x):
        y = x.left
        r = y.right
        size_y = y.size
        if (x == self.root):
            self.root = y
        y.right = x
        y.parent = x.parent
        if (x.parent != leaf):
            if (x.parent.right == x):
                x.parent.right = y
            else:
                x.parent.left = y
        x.parent = y
        x.left = r
        
        if (r != leaf):
            r.parent = x
            
        x.size = x.size + r.size - size_y
        y.size = y.size + x.size - r.size
        
    def count_less_than(self, x):
        leaf.size = 0
        r = self.root
        STSize = 0 #Size of subtree
        if (self.root == None):
            return 0
        while (r != leaf):
            if (x < r.value):
                r = r.left
            elif (x > r.value):
                STSize = STSize + 1 + r.left.size
                r = r.right
            else:
                return (STSize + r.left.size)
            
        else:
            return (STSize)
    
    def isPresent(self, x):
        r = self.root
        while (r != leaf):
            if (r.value == x):
                return True
            elif (r.value > x):
                r = r.left
            elif (r.value < x):
                r = r.right
        else:
            return False
        

    
    def fix_rbproperty(self, v):
        x = v
        while (x.parent.color == "red"):
            par = x.parent
            grand = par.parent
            if (par == grand.left):
                uncle = grand.right
            else:
                uncle = grand.left
            col_uncle = uncle.color
            
            if (grand.left == par):
                if (par.right == x):
                    self.leftRotate(par)
                    recolor(par, uncle)
                else:
                    recolor(x, uncle)
                if (col_uncle == "black"):
                    self.rightRotate(grand)
                    break
                else:
                    x = grand
            else:
                if (par.left == x):
                    self.rightRotate(par)
                    recolor(par, uncle)
                else:
                    recolor(x, uncle)
                if (col_uncle == "black"):
                    self.leftRotate(grand)
                    break
                else:
                    x = grand
        self.root.color = "black"
                    
                
    
    def insert(self, x):
        new = Node(x)
        new.left = leaf
        new.right = leaf
        new.parent = leaf
        if (self.root == leaf):
            self.root = new
            new.color = "black"
        elif (self.isPresent(x) == True):
            return
        else:
            r = self.root
            while True:
                r.size = r.size + 1
                if (r.value > x):
                    if (r.left != leaf):
                        r = r.left
                    elif (r.left == leaf):
                        r.left = new
                        new.parent = r
                        self.fix_rbproperty(new)
                        break
                elif (r.value < x):
                    if (r.right != leaf):
                        r = r.right
                    elif (r.right == leaf):
                        r.right = new
                        new.parent = r
                        self.fix_rbproperty(new)
                        break        

RBT = RedBlackTree()

num = int(input())
inpLi = [[] for _ in range(num)]
for i in range(num):
    inpLi[i] = str(input()).split()

for inp in inpLi:
    if (inp[0] == "+"):
        RBT.insert(int(inp[1]))
    elif (inp[0] == "?"):
        low = int(inp[1])
        upp = int(inp[2])
        print(RBT.count_less_than(upp + 1) - RBT.count_less_than(low))

