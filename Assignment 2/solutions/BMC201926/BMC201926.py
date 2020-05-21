Red = False
Black = True

a = int(input())
lines = []
for i in range(0, a):
    lines.append(list(input().split()))

class Node:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.size = 1
        self.color = Black

sentinel = Node()
sentinel.color = Black
sentinel.size = 0

class RBTree:
    def __init__(self):
        self.root = sentinel                  #####

    def check(self, v):
        b = 0
        x = self.root
        while x is not sentinel:
            if x is None:
                return 0
            if v < x.value:
                x = x.left
            elif v > x.value:
                x = x.right
            elif v == x.value:
                b = b + 1
                return b
        if x is sentinel:
            return 0

    def insert1(self , v):
        if self.check(v) > 0:
            return
        else:
            newnode = Node(v)
            newnode.left = newnode.right = sentinel
            newnode.parent = sentinel
            newnode.size = 1
            x = self.root
            y = sentinel
            if x is sentinel:  # ####
                self.root = newnode
                newnode.color = Black
                return
            while x is not sentinel and x is not None:
                y = x
                x.size += 1
                if v < x.value:
                    x = x.left
                else:
                    x = x.right

            if v < y.value:
                y.left = newnode
                newnode.parent = y
            else:
                y.right = newnode
                newnode.parent = y
            newnode.color = Red
            if newnode.parent == self.root:
                return
            else:
                self.rebalance(newnode)




    def left_rotate(self, node):
        p = node.parent
        y = node.right
        if self.root == node:
            self.root = y
        node.right = y.left
        if y.left is not sentinel:
            y.left.parent = node
        y.left = node
        node.parent = y
        y.parent = p
        if p is not sentinel:
            if p.left == node:
                p.left = y
            else:
                p.right = y
        q = node.size
        y.size = q
        node.size = y.size - y.right.size - 1

    def right_rotate(self, node):
        p = node.parent
        y = node.left
        if self.root == node:
            self.root = y
        node.left = y.right
        if y.right is not sentinel:
            y.right.parent = node

        y.right = node
        node.parent = y
        y.parent = p
        if p is not sentinel:
            if p.left == node:
                p.left = y
            else:
                p.right = y
        q = node.size
        y.size = q
        node.size = y.size - y.left.size - 1

    def count_less_than(self, v):
        size = 0
        x = self.root
        if x is sentinel:
            return 0
        while x != sentinel:
            if v > x.value:
                size = size + 1 + x.left.size
                x = x.right
            elif v < x.value:
                x = x.left
            elif v == x.value:
                size = size + x.left.size
                return size
        if x is sentinel:
            return size


    def rebalance(self, node):
        if node is self.root or node.parent is self.root:
            return
        g = node.parent.parent

        if g.left is node.parent:
            u = g.right
        else:
            u = g.left

        if node.parent.color == Red:
            if u.color == Red:
                node.parent.color = Black
                u.color = Black
                g.color = Red
                self.rebalance(g)
            elif u.color == Black and node.parent.right is node and node.parent == g.left:

                self.left_rotate(node.parent)
                self.rebalance(node.left)
            elif u.color == Black and node.parent.left is node and node.parent == g.right:

                self.right_rotate(node.parent)
                self.rebalance(node.right)
            elif u.color == Black and node.parent.left is node and node.parent == g.left:

                node.parent.color = Black
                g.color = Red
                self.right_rotate(g)
            elif u.color == Black and node.parent.right is node and node.parent == g.right:
                node.parent.color = Black
                g.color = Red
                self.left_rotate(g)

t = RBTree()

for i in range (0, a):
    if lines[i][0] == '+':
        t.insert1(int(lines[i][1]))

    else:
        print((t.count_less_than(int(lines[i][2]) + 1)) - (t.count_less_than(int(lines[i][1]))))
        

