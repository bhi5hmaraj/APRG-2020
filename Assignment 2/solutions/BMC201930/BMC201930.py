class Node:
    def __init__(self, initval = None):
        self.value  = initval
        self.right  = None
        self.left   = None
        self.parent = None
        self.size   = 1
        self.colour = 1

class RedBlackTree:
    def __init__(self): self.root = None
    
    def isLeft(self, node):
        if node.parent.left == node: return True
        return False
    
    def isRight(self, node):
        if node.parent.right == node: return True
        return False
    
    def node_col(self,node):
        if not node: return 0
        return node.colour

    def node_size(self, node):
        if not node: return 0
        return node.size
    
    def node_val(self, node):
        if not node: return 1e-6
        return node.value

    def left_rotate(self, x):
        y = x.right
        p = x.parent
        x.parent = y
        y.parent = p
        if not p: self.root = y
        elif p.left==x: p.left=y
        else: p.right = y
        b = y.left
        y.left = x
        x.right = b
        if b: b.parent = x
        A = self.node_size(x.left)
        B = self.node_size(b)
        C = self.node_size(y.right)
        x.size = A + B + 1
        y.size = self.node_size(x) + C + 1
    
    def right_rotate(self,y):
        x = y.left
        p = y.parent
        x.parent = p
        if not p: self.root = x
        elif p.left==y: p.left = x
        else: p.right = x
        y.parent = x
        b = x.right
        x.right = y
        y.left = b
        if b: b.parent = y
        A = self.node_size(x.left)
        B = self.node_size(b)
        C = self.node_size(y.right)
        y.size = B + C + 1
        x.size = A + self.node_size(y) + 1

    def setcol(self,node,col):
        if not node: return
        node.colour = col
    
    def insert(self,v):
        z = Node(v)
        p = None
        x = self.root
        while x != None:
            p = x
            if v == self.node_val(x): return
            elif v < self.node_val(x): x = x.left
            else: x = x.right
        z.parent = p
        self.fix_size(z)
        if p == None: self.root = z
        elif self.node_val(p) < v: p.right = z
        elif self.node_val(p) > v: p.left = z
        else: return
        if self.root == z: 
            z.colour = 0
            return
        if self.root == z.parent: 
            return
        self.fix_rbproperty(z)
        
    def fix_rbproperty(self,node):
        p = node.parent
        while self.node_col(node.parent):
            if self.isLeft(p):
                uncle = node.parent.parent.right
                if self.node_col(uncle):
                    self.setcol(node.parent,0)
                    self.setcol(uncle,0)
                    self.setcol(node.parent.parent,1)
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    self.setcol(node.parent,0)
                    self.setcol(node.parent.parent,1)
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if self.node_col(uncle):
                    self.setcol(node.parent,0)
                    self.setcol(uncle,0)
                    self.setcol(node.parent.parent,1)
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    self.setcol(node.parent,0)
                    self.setcol(node.parent.parent,1)
                    self.left_rotate(node.parent.parent)
            if node == self.root: break
        self.root.colour = 0
    
    def fix_size(self, node):
        x = node
        while x.parent:
            x = x.parent
            x.size = self.node_size(x) + 1            
            
    def count_less_than(self, n):
        x = self.root
        ans = 0
        while x:
            if self.node_val(x) < n:
                ans += self.node_size(x.left)+1
                x = x.right
            else:
                x = x.left
        return ans
    
if __name__ == "__main__":
    rbt = RedBlackTree()
    q = int(input())
    while q > 0:
        inp = input().split()
        if inp[0] == '+': rbt.insert(int(inp[1]))
        else: 
            (l,r) = (int(inp[1]), int(inp[2]))
            print(rbt.count_less_than(r+1) - rbt.count_less_than(l))
        q -= 1
