import sys
sys.setrecursionlimit(10**6)
class Node:
    def __init__(self,initval = None):
        self.value = initval
        self.right = None
        self.left = None
        self.parent = None
        self.size = 1
        self.color = "black"
    def myinsert (self,x):
        if self == None:
            n = Node(x)
            n.color = "red"
            self = n
            return (self)
        if self.value > x:
            if self.left == None:
                n = Node(x)
                n.color = "red"
                n.parent = self
                self.left = n
                self.size = 1 + self.size
                return (self.left)
            else:
                self.size = 1 + self.size
                return (self.left.myinsert(x))
        else:
            if self.right == None:
                n = Node(x)
                n.color = "red"
                n.parent = self
                self.right = n
                self.size = 1 + self.size
                return (self.right)
            else:
                self.size = 1 + self.size
                return (self.right.myinsert(x))
class RedBlackTree:
    def __init__(self):
        self.root = Node(0)
    def search (self,x):
        if self.root == None or self.root == Node(0):
            return (None)
        elif self.root.value == x:
            return (self.root)
        elif self.root.value > x:
            if self.root.left == None:
                return (None)
            else:
                leftsubtree = RedBlackTree()
                leftsubtree.root = self.root.left
                return (leftsubtree.search(x))
        else:
            if self.root.right == None:
                return (None)
            else:
                rightsubtree = RedBlackTree()
                rightsubtree.root = self.root.right
                return (rightsubtree.search(x))
    def insert (self,x):
        if (self.search(x)) != None:
            return (None)
        else:
            return (Node.myinsert (self.root,x))
    def left_rotate (self,n):
        y = n.right
        r = n.right.right
        a = n.left
        if r != None:
            n.size = n.size - r.size - 1
        else:
            n.size = n.size - 1
        if a != None:
            y.size = y.size + a.size + 1
        else:
            y.size = y.size + 1
        if y != None:
            n.right = y.left
            if y.left != None:
                y.left.parent = n
            y.parent = n.parent
            if n.parent == None:
                self.root = y
            elif n.parent.left == n:
                n.parent.left = y
            else:
                n.parent.right = y
            y.left = n
            n.parent = y
            return
        else:
            return
    def right_rotate (self,n):
        y = n.left
        a = n.left.left
        c = n.right
        if a != None:
            n.size = n.size - a.size - 1
        else:
            n.size = n.size - 1
        if c != None:
            y.size = y.size + c.size + 1
        else:
            y.size = y.size + 1
        if y != None:
            n.left = y.right
            if y.right != None:
                y.right.parent = n
            y.parent = n.parent
            if n.parent == None:
                self.root = y
            elif n.parent.right == n:
                n.parent.right = y
            else:
                n.parent.left = y
            y.right = n
            n.parent = y
            return
        else:
            return
    def rebalance (self,n):
        if n == None:
            return (self)
        elif n == self.root:
            self.root.color = "black"
            return (self)
        elif n.parent.color == "black":
            return (self)
        else:
            if n.parent.parent.left == n.parent:
                if  n.parent.parent.right != None and n.parent.parent.right.color == "red":
                    g = n.parent.parent
                    n.parent.color = "black"
                    g.right.color = "black"
                    g.color = "red"
                    return (self.rebalance(g))
                else:
                    if n.parent.right == n:
                        c = n.parent
                        self.left_rotate(c)
                        return (self.rebalance(c))
                    else:
                        g = n.parent.parent
                        n.parent.color = "black"
                        n.parent.parent.color = "red"
                        self.right_rotate(g)
                        return (self)
            else:
                if n.parent.parent.left != None and n.parent.parent.left.color == "red":
                    n.parent.color = "black"
                    g = n.parent.parent
                    g.left.color = "black"
                    g.color = "red"
                    return (self.rebalance(g))
                else:
                    if n.parent.left == n:
                        c = n.parent
                        self.right_rotate(c)
                        return (self.rebalance(c))
                    else:
                        n.parent.color = "black"
                        g = n.parent.parent
                        g.color = "red"
                        self.left_rotate(g)
                        return (self)
    def count_less_than (self,x):
        if self.root == None:
            return (0)
        elif self.root.value == x:
            if self.root.left == None:
                return (0)
            else:
                return (self.root.left.size)
        elif self.root.value > x:
            leftsubtree = RedBlackTree()
            leftsubtree.root = self.root.left
            return (leftsubtree.count_less_than(x))
        else:
            if self.root.left == None:
                rightsubtree = RedBlackTree()
                rightsubtree.root = self.root.right
                return (1 + (rightsubtree.count_less_than(x)))
            else:
                rightsubtree = RedBlackTree()
                rightsubtree.root = self.root.right
                a = self.root.left.size
                b = rightsubtree.count_less_than(x)
                return (1 + a + b)
    def height (self):
        return (Node.height (self.root))
a = int(input())
RBT = RedBlackTree()
for i in range(a):
    b = list(input().split())
    if b[0] == "+":
        n = RBT.insert(int(b[1]))
        RBT.rebalance(n)
    else:
        print ((RBT.count_less_than(int(b[2])+1)) - RBT.count_less_than(int(b[1])))    

            
        
