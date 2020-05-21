
import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self,initval=None):
        self.value = initval
        self.parent = None
        self.left = None
        self.right = None
        self.color = "black"
        self.size = 1


    def height(self):
        l = 0 if self.left == None else self.left.height()
        r = 0 if self.right == None else self.right.height()
        return 1 + max(l, r) 


    def countless (self,x):
        if self == None:
            return (0)
        elif self.value == x:
            if self.left == None:
                return (0)
            else:
                return (self.left.size)
        elif self.value > x:
            if self.left == None:
                return (0)
            else:
                return (self.left.countless(x))
        else:
            if self.left == None:
                if self.right == None:
                    return (1)
                else:
                    return (1 + self.right.countless(x))
            else:
                if self.right == None:
                    return (1 + self.left.size)
                else:
                    return (1 + self.left.size + self.right.countless(x))
class RedBlackTree:
    def __init__(self):
        self.root = Node(0)

    def search (self,x):
        if self.root.value == x:
            return (self.root)
        elif self.root.value > x:
            leftsubtree = RedBlackTree()
            leftsubtree.root = self.root.left
            self.root.left = leftsubtree.root
            return (leftsubtree.search(x))
        else:
            rightsubtree = RedBlackTree()
            rightsubtree.root = self.root.right
            self.root.right = rightsubtree.root
            return (rightsubtree.search(x))
    def find (self,x):
        if self.root.value == 0:
            return False
        elif self.root.value == x:
            return True
        elif self.root.value > x:
            if self.root.left == None:
                return False
            else:
                leftsubtree = RedBlackTree()
                leftsubtree.root = self.root.left
                return (leftsubtree.find(x))
        else:
            if self.root.right == None:
                return False
            else:
                rightsubtree = RedBlackTree()
                rightsubtree.root = self.root.right
                return (rightsubtree.find(x))
    def insert (self,x):
        if (self.find(x)) == True:
            return
        else:
            if self.root.value == 0:
                self.root.value = x
                self.root.color = "red"
                return
            elif self.root.value > x:
                if self.root.left == None:
                    n = Node(x)
                    n.color = "red"
                    n.parent = self.root
                    self.root.left = n
                    self.root.size = 1 + self.root.size
                    return
                else:
                    self.root.size = 1 + self.root.size
                    leftsubtree = RedBlackTree()
                    leftsubtree.root = self.root.left
                    self.root.left = leftsubtree.root
                    leftsubtree.insert(x)
            else:
                if self.root.right == None:
                    n = Node(x)
                    n.color = "red"
                    n.parent = self.root
                    self.root.right = n
                    self.root.size = 1 + self.root.size
                    return
                else:
                    self.root.size = 1 + self.root.size
                    rightsubtree = RedBlackTree()
                    rightsubtree.root = self.root.right
                    self.root.right = rightsubtree.root
                    rightsubtree.insert(x)
    def left_rotate (self,x):
        n = self.search(x)
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
    def right_rotate (self,x):
        n = self.search(x)
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
    def rebalance (self,x):
        if (self.search(x)) == self.root:
            self.root.color = "black"
            return (self)
        elif (self.search(x)).parent.color == "black":
            return (self)
        else:
            n = self.search(x)
            if n.parent.parent.left == n.parent:
                if  n.parent.parent.right != None and n.parent.parent.right.color == "red":
                    n.parent.color = "black"
                    n.parent.parent.right.color = "black"
                    n.parent.parent.color = "red"
                    return (self.rebalance(n.parent.parent.value))
                else:
                    if n.parent.right == n:
                        self.left_rotate(n.parent.value)
                        return (self.rebalance(x))
                    else:
                        n.parent.color = "black"
                        n.parent.parent.color = "red"
                        self.right_rotate(n.parent.parent.value)
                        return (self)
            else:
                if n.parent.parent.left != None and n.parent.parent.left.color == "red":
                    n.parent.color = "black"
                    n.parent.parent.left.color = "black"
                    n.parent.parent.color = "red"
                    return (self.rebalance(n.parent.parent.value))
                else:
                    if n.parent.left == n:
                        self.right_rotate(n.parent.value)
                        return (self.rebalance(x))
                    else:
                        n.parent.color = "black"
                        n.parent.parent.color = "red"
                        self.left_rotate(n.parent.parent.value)
                        return (self)
    def count_less_than (self,x):
        return (Node.countless (self.root,x))


def solve():
    a = int(input())
    RBT = RedBlackTree()
    for i in range(a):
        b = list(input().split())
        if b[0] == "+":
            RBT.insert(int(b[1]))
            RBT.rebalance(int(b[1]))
        else:
            pass
            # print((RBT.count_less_than((int(b[2])+1))) - (RBT.count_less_than(int(b[1]))))
    print(a, " height = ", RBT.root.height())



import timeit


start_time = timeit.default_timer()
solve()
print(timeit.default_timer() - start_time)