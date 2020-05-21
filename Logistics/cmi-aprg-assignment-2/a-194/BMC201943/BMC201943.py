class Node :
    def __init__(self, value = 0, color = 1):
        self.value = value
        self.color = color
        self.parent = None
        self.left = None
        self.right = None
        self.size = 1
class RedBlackTree:         
    def __init__(self):
        self.root = None
        self.sentinel = Node(value = 0,color = 0)
        self.sentinel.size = 0
        self.right = self.sentinel
        self.left = self.sentinel
        
    def _size(self,node):
        if node == None:
            return 0
        else:
            return node.size
                
    def left_rotate(self, x):
        y = x.right
        a = self._size(x.left)
        c = self._size(y.right)  
        b = self._size(y.left)      
        x.right = y.left
        if y.left != self.sentinel:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
        x.size = a+b+1
        y.size = a+b+1+c+1

        
        
    def right_rotate(self, x):
        y = x.left
        a = self._size(x.right)
        c = self._size(y.left)  
        b = self._size(y.right) 
        x.left = y.right
        if y.right != self.sentinel:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
        x.size = a+b+1
        y.size = a+b+1+c+1 
        
    def insert(self, z):
        node = Node(value = z)
        y = None
        x = self.root
        while x != self.sentinel and x != None:
            y = x
            if z < x.value :
                x = x.left
            elif z > x. value:
                x = x.right
            else: return
        node.parent = y
        if y == None:
            self.root = node
        elif z < node.parent.value:
            node.parent.left = node
        else:
            node.parent.right = node
        node.left = self.sentinel
        node.right = self.sentinel
        node.color = 1
        x = node.parent
        while x != None:
            x.size = x.size + 1
            x = x.parent
        if node==self.root or node.parent==self.root: return
        self.fix_rbproperty(node)

    def fix_rbproperty(self, z):        
        while z.parent.color == 1:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == 1:
                    z.parent.color = 0
                    y.color = 0
                    z.parent.parent.color = 1
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = 0
                    z.parent.parent.color = 1
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == 1:
                    z.parent.color = 0
                    y.color = 0
                    z.parent.parent.color = 1
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = 0
                    z.parent.parent.color = 1
                    self.left_rotate(z.parent.parent)
            if z.parent == None: break
        self.root.color = 0
        
    def count_less_than (self,z):
        i = 0
        x = self.root
        y = x
        while y != self.sentinel and y!= None:
            if y.value==z:
                i+=self._size(y.left)
                break
            if y.value > z:
                y = y.left
            else:
                i+=self._size(y.left)+1
                y = y.right
        return i

rbt = RedBlackTree()
n = int(input())
for i in range(n):
    l = (input().split())
    if l[0] == "+":
        rbt.insert(int(l[1]))
    else:
        print (rbt.count_less_than(int(l[2])+1) - rbt.count_less_than(int(l[1])))
