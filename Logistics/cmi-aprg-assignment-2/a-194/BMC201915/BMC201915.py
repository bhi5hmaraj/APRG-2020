# 1 = Red
# 0 = Black
import sys
sys.setrecursionlimit(10**6)
class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1
class RedBlackTree:
    def __init__(self):
        self.sentinel = Node(0)
        self.sentinel.color = 0
        self.sentinel.left = None
        self.sentinel.right = None
        self.root = self.sentinel
    def find(self, val):
        a = self.root
        while a is not None and a != self.sentinel:
            if a.value == val:
                return 1
            if a.value > val:
                a = a.left
            else:
                a = a.right
        return 0
    def right_rotate(self, x):
        y = x.left
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
        
    def left_rotate(self, x):
        y = x.right
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

    def __fix_insert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent 
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0
    def insert(self, key):
        if self.find(key):
            return
        node = Node(key)
        node.parent = None
        node.value = key
        node.left = self.sentinel
        node.right = self.sentinel
        node.color = 1

        y = None
        x = self.root

        while x != self.sentinel:
            y = x
            if node.value < x.value:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y == None:
            self.root = node
        elif node.value < y.value:
            y.left = node
        else:
            y.right = node

        if node.parent == None:
            node.color = 0
            return

        if node.parent.parent == None:
            return

        self.__fix_insert(node)
    def count_less_than(self, pt, val):
        if pt == self.sentinel or pt == None:
            return 0
        else :
            if pt.value <= val:
                return (1 + self.count_less_than(pt.right, val) + self.count_less_than(pt.left, val))
            else:
                return self.count_less_than(pt.left, val)
t = int(input())
rb = RedBlackTree()
while t:
    query = input().split()
    if query[0] == "+":
        rb.insert(int(query[1]))
    elif query[0] == "?" :        #query[0]=="?"
        pr = rb.count_less_than(rb.root, int(query[2])) - rb.count_less_than(rb.root, int(query[1])) + rb.find(int(query[1]))
        print(pr)
    t = t - 1
    
            
    
