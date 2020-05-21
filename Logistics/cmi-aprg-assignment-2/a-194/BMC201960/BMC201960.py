a = int(input())

k = ""
for i in range(a):
    k += input() + "\n"

l = k.split("\n") 

class Node:
    """All the properties of nodes that we will need"""
    def __init__(self, value, left, right, parent, size, colour):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.size = size
        self.colour = colour

class RedBlackTree:
    def __init__(self, root):
        self.root = root

    def insert(self, n):
        if self.root == None:
            self.root = Node(n, RedBlackTree(None), RedBlackTree(None), None, 1, "Black")
            return self
        if n > self.root.value and self.root.right == RedBlackTree(None):
            self.root.right.root = Node(n, RedBlackTree(None), RedBlackTree(None), self.root, 1, "Red")
            self.root.size += 1
            return self.rebalance(self.root.right.root)
        elif n > self.root.value and self.root.right != RedBlackTree(None):
            self.root.size += 1
            self.root.right.insert(n)
            return self
        elif n < self.root.value and self.root.left == RedBlackTree(None):
            self.root.left.root = Node(n, RedBlackTree(None), RedBlackTree(None), self.root, 1, "Red")
            self.root.size += 1
            return self.rebalance(self.root.left.root)            
        elif n < self.root.value and self.root.left != RedBlackTree(None):
            self.root.size += 1
            self.root.left.insert(n)
            return self
        elif n == self.root.value:
            return self

    def rebalance(self, x):
        if x == self.root:
            x.colour = "Black"
            return self
        elif x.parent.colour == "Black":
            return self
        elif x.parent == x.parent.parent.left.root:
            if x.parent.parent.right.root.colour == "Red":
                x.parent.colour == "Black"
                x.parent.parent.colour == "Red"
                x.parent.parent.right.root.colour == "Black"
                return self.rebalance(x.parent.parent)
            else:
                if x == x.parent.right.root:
                    self.left_rotate(x.parent)
                    return self.rebalance(x) #check this again after writing code for right-rotate
                else:
                    x.parent.colour = "Black"
                    x.parent.parent.colour = "Red"
                    self.right_rotate(x.parent.parent)
                    return self
        elif x.parent == x.parent.parent.right.root:
            if x.parent.parent.left.root.colour == "Red":
                x.parent.colour == "Black"
                x.parent.parent.colour == "Red"
                x.parent.parent.left.root.colour == "Black"
                return self.rebalance(x.parent.parent)
            else:
                if x == x.parent.right.root:
                    self.left_rotate(x.parent)
                    return self.rebalance(x) #check this again after writing code for right-rotate
                else:
                    x.parent.colour = "Black"
                    x.parent.parent.colour = "Red"
                    self.right_rotate(x.parent.parent)
                    return self

    def right_rotate(self, n):
        x = n
        a = n.left.root
        b = n.left.root.right.root
        p = n.parent
        if n == p.left.root: #check None cases
            p.left == a
            a.parent == p
            x.left.root == b
            b.parent == x
            a.right.root == x
            x.parent == a
            return self    # in insert, check if the element has both parent and child
        else:
            p.right == a
            a.parent == p
            x.left.root == b
            b.parent == x
            a.right.root == x
            x.parent == a
            return self

    def left_rotate(self, n):
        x = n
        a = n.right.root
        b = n.right.root.left.root
        p = n.parent
        if n == p.left.root: #check None cases
            p.left == a
            a.parent == p
            x.right.root == b
            b.parent == x
            a.left.root == x
            x.parent == a
            return self    # in insert, check if the element has both parent and child
        else:
            p.right == a
            a.parent == p
            x.right.root == b
            b.parent == x
            a.left.root == x
            x.parent == a
            return self

    def count_less_than(self, x):
        if self.root == None:
            return 0
        elif x > self.root.value:
            if self.root.left.root == None:
                return(1 + self.root.right.count_less_than(x))
            else:
                return (1 + self.root.left.root.size + self.root.right.count_less_than(x))
        else:
            return (self.root.left.count_less_than(x))

    def contains(self, y):
        if self.root == None:
            return False
        elif self.root.value == y:
            return True
        elif self.root.value < y:
            return self.root.right.contains(y)
        else:
            return self.root.left.contains(y)        

rbt = RedBlackTree(None)

for i in range(a):
    if l[i][0] == '+':
        c = int(l[i][2:])
        rbt.insert(c)
    elif l[i][0] == '?':
        c = l[i][2:]
        d = c.split()
        a = int(d[0])
        b = int(d[1])
        if rbt.contains(b) == True:
            print(rbt.count_less_than(b) - rbt.count_less_than(a) + 1)
        else:
            print(rbt.count_less_than(b) - rbt.count_less_than(a))
    else:
        print("Error: Wrong cases given")
