Red = 1
Black = 0


class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.color = Red
        self.size = 1
    def getcol(self):
        return self.color

sentinel = Node()
sentinel.color = Black
sentinel.size = 0

def recolor(node, u):                     # u ---- uncle
        node.parent.color = Black
        node.parent.parent.color = Red
        u.color = Black
        sentinel.color = Black

class RedBlackTree:
    def __init__(self):
        self.root = sentinel

    def insert(self, val):
        if val<0:
            return
        new_node = Node(val)
        new_node.left = sentinel
        new_node.right = sentinel
        new_node.parent = sentinel
        if self.root == sentinel:
            self.root = new_node
            new_node.color = Black
        elif self.find(val):
            return
        else:
            a = self.root
            while True:
                a.size += 1

                if a.value > val:
                    if a.left != sentinel:
                        a = a.left
                
                    else:
                        a.left = new_node
                        new_node.parent = a
                        
                        self.rebalance(new_node)
                        break

                elif a.value < val:
                    if a.right != sentinel:
                        a = a.right
                        
                    else:
                        a.right = new_node
                        new_node.parent = a
                        
                        self.rebalance(new_node)
                        break

    def rebalance(self, node):
        a = node
        while a.parent.color == Red:
            p = a.parent
            
            g = p.parent
            if p == g.left:
                uncle = g.right
            else:
                uncle = g.left
            k = uncle.color

            #self.recolor(a, uncle)
            
            if g.left == p:
                if p.right == a:
                    self.left_rotate(p)
                    recolor(p, uncle)
                else:
                    recolor(a, uncle)
                if k == Black:
                    self.right_rotate(g)
                    break
                else:
                    a = g
                    
            else:
                if p.left == a:
                    self.right_rotate(p)
                    recolor(p, uncle)
                else:
                    recolor(a, uncle)
                if k == Black:
                    self.left_rotate(g)
                    break
                else:
                    a = g
        self.root.color = Black
        
    '''def rebalance(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left # uncle
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
                u = k.parent.parent.right # uncle

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
        self.root.color = 0'''


    
    def left_rotate(self, node):
        y = node.right
        t = y.left
        sy = y.size
        if node == self.root:
            self.root = y
        y.left = node
        y.parent = node.parent
        if node.parent != sentinel:
            if node.parent.left == node:
                node.parent.left = y
            else:
                node.parent.right = y
        node.parent = y
        node.right = t
        if t != sentinel:
            t.parent = node

        node.size += (t.size - sy)
        y.size += (node.size - t.size)

    def right_rotate(self, node):
        y = node.left
        t = y.right
        sy = y.size
        if node == self.root:
            self.root = y
        y.right = node
        y.parent = node.parent
        if node.parent != sentinel:
            if node.parent.right == node:
                node.parent.right = y
            else:
                node.parent.left = y
        node.parent = y
        node.left = t
        if t != sentinel:
            t.parent = node

        node.size += (t.size - sy)
        y.size += (node.size - t.size)

    def count_less_than(self, val):
        sentinel.size = 0
        a = self.root
        b = 0
        if self.root == None:
            return 0
        while a != sentinel:
            if val < a.value:
                a = a.left
            elif val > a.value:
                b += (1 + a.left.size)
                a = a.right
            else:
                b += a.left.size
                return b
        else:
            return b

    def find(self, val):
        a = self.root
        while a != sentinel:
            if a.value == val:
                return True
            elif a.value > val:
                a = a.left
            else:
                a = a.right
        else:
            return False



rbt = RedBlackTree()

n = int(input())

queries = []

for i in range(n):
    queries.append(list(input().split()))


for query in queries:
    if query[0] == "+":
        rbt.insert(int(query[1]))
    elif query[0] == "?" and rbt.root:
        l, u = map(int, query[1:5])
        
        k = rbt.count_less_than(u+1)-rbt.count_less_than(l)
        print(k)
        
        #else:
            #print(0)
