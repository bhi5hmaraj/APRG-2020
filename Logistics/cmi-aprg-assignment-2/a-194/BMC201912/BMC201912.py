import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__ (self, val = None, lt = None, rt = None, par = None, sz = 1, col = False ):
        self.value = val #integer
        self.left = lt #node
        self.right = rt #node
        self.parent = par #node
        self.size = sz #integer
        self.color = col #Bool, True if Red or False if black; interpret it as isred
    def sibling(self):
        if (self.parent == None):
            return None
        else:
            if (self.parent.value < self.value):
                return self.parent.left
            else:
                return self.parent.right
    def printnode(self, z, n = 0):
        ws = " "*(2*n)
        if (z == None):
            return ws + " None [sentinel], black \n"
        s = ws + " val: " + str(z.value) + " size : " + str(z.size) + " isRed : "+ str(z.color) + '\n'
        s = s + self.printnode(z.left, n+1) + self.printnode(z.right, n+1)
        return s
    def __str__(self):
        return self.printnode(self)

class RedBlackTree:
    def __init__(self, rt = Node()):
        self.root = rt
    def sizesub(self, v):
        if (v == None):
            return 0
        else:
            return v.size
    def setpar(self, v, w):
        if (v == None):
            return
        else:
            v.parent = w
    def left_rotate(self, x): #add the size
        a = x.left
        y = x.right
        b = y.left
        g = y.right
        x.size = 1 + self.sizesub(a) + self.sizesub(b)
        y.size = 1 + self.sizesub(x) + self.sizesub(g)
        if (x.value == self.root.value):
            self.root = y
        else:
            z = x.parent
            if (z.value < x.value):
                 z.right = y
            else:
                z.left = y
        y.right = g
        y.left = x
        x.right = b
        x.left = a
        y.parent = x.parent
        x.parent = y
        self.setpar(b,x)        
    def right_rotate(self, y):

        x = y.left
        g = y.right
        a = x.left
        b = x.right
        y.size = 1 + self.sizesub(g) + self.sizesub(b)
        x.size = 1 + self.sizesub(y) + self.sizesub(a)
        if (y.value == self.root.value):
            self.root = x
        else:
            z = y.parent
            if (z.value < y.value):
                 z.right = x
            else:
                z.left = x    
        x.right = y
        x.left = a
        y.right = g
        y.left = b
        x.parent = y.parent
        y.parent = x
        self.setpar(b,y)    
    def insert(self, val, v):
        if (v.value == None):
            v.value = val
        if (val == v.value):
            return
        else:
            v.size +=1
            z = Node(val, col = True)
            if (val < v.value):
                if (v.left == None):
                    v.left = z
                    z.parent = v
                    self.rebalance(z)
                else:
                    self.insert(val, v.left)
            else:
                if (v.right == None):
                    v.right = z
                    z.parent = v
                    self.rebalance(z)
                else:
                    self.insert(val, v.right)
    def rebalance(self, vert):
        if (vert.value == self.root.value):
            self.root.color = False
            return
        if (vert.parent == self.root):
            vert.parent.color = False
            return
        if (vert.parent.color == False):
            return
        else:
            b = vert
            a = vert.parent
            c = vert.parent.parent
            d = vert.parent.sibling()
            if ((d == None) or (d.color == False)):
                if (a.value < c.value): #d is in the right side
                    if (b.value > a.value): #z is in the right side:
                        self.left_rotate(a)
                        self.rebalance(a)
                    else: #z is in the left side
                        a.color = False
                        c.color =  True
                        self.right_rotate(c)
                        self.rebalance(c)
                else: #d is in the left side
                    if (b.value < a.value): #z is in the left side
                        self.right_rotate(a)
                        self.rebalance(a)
                    else: #z is in the right side
                        a.color = False
                        c.color = True
                        self.left_rotate(c)
                        self.rebalance(c)
            elif (d.color):
                a.color = False
                d.color = False
                c.color = True
                self.rebalance(c) 
    def findtree(self,  val, v):
        if ((v == None) or (v.value == None)):
            return False
        elif (val == v.value):
            return True
        elif (val < v.value):
            return self.findtree(val, v.left)
        else:
            return self.findtree(val, v.right)
    def numbelow(self, val, v):
        if ((v == None) or (v.value == None)):
            return 0
        elif (val == v.value):
            return self.sizesub(v.left) + 1
        elif (val < v.value):
            return self.numbelow(val, v.left)
        else:
            return 1 + self.sizesub(v.left) + self.numbelow(val, v.right)
    def count_less_than(self, x):
        return self.numbelow(x, self.root)
    def numint(self, a, b):
        if (a > b):
            return 0
        return self.numbelow(b, self.root) - self.numbelow(a-1, self.root)


q = int(input())
tr = RedBlackTree()
for i in range(q):
    s = str(input()).split()
    if (s[0] == '+'):
       a = int(s[1])
       if (tr.findtree(a, tr.root)):
               continue
       else:
               tr.insert(int(s[1]), tr.root)
    else:
        a = int(s[1])
        b = int(s[2])
        print(tr.numint(a,b))

