import sys
sys.setrecursionlimit(10**6)

class Node:

    def __init__(self,v):
        self.value = v
        self.left  = None
        self.right = None
        self.parent = None
        self.size = 1
        self.color = "RED"

class RedBlackTree:

    def __init__(self):
        self.root = None

    def left_rotate(self,v):
        y = v.right
        v.right  = y.left

        if y.left != None:
            y.left.parent = v
            ls = y.left.size
        else:
            ls = 0
        y.parent = v.parent
        if v.parent == None:
            self.root =y
        elif v == v.parent.left:
            v.parent.left = y
        else:
            v.parent.right = y
        y.left = v
        v.parent = y
        tff = v.size
        tf = y.size
        y.size = tff
        v.size = tff - tf  + ls


    def right_rotate(self,v):
        y = v.left
        v.left = y.right
        if y.right != None:
            y.right.parent = v
            ls = y.right.size
        else:
            ls = 0
        y.parent = v.parent
        if v.parent == None:
            self.root = y
        elif v == v.parent.right:
            v.parent.right = y
        else:
            v.parent.left = y
        y.right = v
        v.parent = y
        tff = v.size
        tf = y.size
        y.size = tff
        v.size = tff - tf  + ls



    def rebalance(self,v):
        while (v.parent.color == "RED"):
            if v.parent == v.parent.parent.left:
                y = v.parent.parent.right
                if y != None and y.color == "RED":
                    v.parent.color = "BLACK"
                    y.color = "BLACK"
                    v.parent.parent.color = "RED"
                    v = v.parent.parent
                else:
                    if v == v.parent.right:
                        v = v.parent
                        self.left_rotate(v)
                    v.parent.color = "BLACK"
                    v.parent.parent.color = "RED"
                    self.right_rotate(v.parent.parent)
            else:
                y = v.parent.parent.left
                if y != None and y.color == "RED":
                    v.parent.color = "BLACK"
                    y.color = "BLACK"
                    v.parent.parent.color = "RED"
                    v = v.parent.parent
                else:
                    if v == v.parent.left:
                        v = v.parent
                        self.right_rotate(v)
                    v.parent.color = "BLACK"
                    v.parent.parent.color = "RED"
                    self.left_rotate(v.parent.parent)
            if(v.parent == None):
                break
        self.root.color = "BLACK"

    def insert(self,v):
        if self.root == None:
            self.root = v
            self.root.color = "BLACK"
        else:
            x = self.root
            y = None
            while x != None:
                x.size += 1
                y = x
                if v.value < x.value:
                    x = x.left
                else:
                    x = x.right

            v.parent = y
            if v.value < y.value :
                y.left = v
            else:
                y.right = v
            v.right = None
            v.left = None
            v.color = "RED"
            self.rebalance(v)



    def count_less_than(self,val):
        x = self.root
        ans = 0
        if(x == None):
            return 0
        while True:
            #print(x.value)
            if(x.right == None):
                rs = 0
            else:
                rs = x.right.size

            if(x.value < val):
                ans += x.size -rs
                x = x.right            
            elif x.value > val:
                x = x.left
            else:
                ans += x.size - rs
                return ans
            #print(ans)
            if x == None:
                return ans

q = int(input())
tree = RedBlackTree()
for _ in range(q):
    inp = input()
    if(inp[0] == '+'):
        val = int(inp[2:])
        f = tree.count_less_than(val) - tree.count_less_than(val-1)
        #print(f)
        if(f == 0):
            tree.insert(Node(val))
    else:
        l,r = inp[2:].split()
        l = int(l)
        r = int(r)
        print(tree.count_less_than(r) - tree.count_less_than(l-1))


