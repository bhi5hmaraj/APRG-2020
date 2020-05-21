
class Node:
    def __init__(self, x=None):
        self.value = x
        self.left = None
        self.right = None
        self.parent = None
        self.size = 0
        self.color = 0 # 0: black, 1: red


class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, x):
        if self.root == None:
            a = Node(x)
            a.size = 1
            self.root = a

        else:
            t = self.root
            while True:
                if x == t.value: break
                if x < t.value:
                    if t.left:
                        t = t.left
                    else:
                        t.left = Node(x)
                        t.left.color = 1
                        t.left.parent = t
                        t.left.size = 1
                        self.inc_size(t.left)
                        self.rebalance(t.left)
                        break
                else:
                    if t.right:
                        t = t.right
                    else:
                        t.right = Node(x)
                        t.right.color = 1
                        t.right.parent = t
                        t.right.size = 1
                        self.inc_size(t.right)
                        self.rebalance(t.right)
                        break



    def rotate_left(self, node):
        y = node.right
        node.right = y.left

        bs = 0
        if y.left:
            y.left.parent = node
            bs = y.left.size

        node.size -= y.size
        node.size += bs

        y.size -= bs
        y.size += node.size

        y.parent = node.parent
        if node.parent == None:             self.root = y
        elif node == node.parent.right:     node.parent.right = y
        else:                               node.parent.left = y

        y.left = node
        node.parent = y


    def rotate_right(self, node):
        x = node.left
        node.left = x.right

        bs = 0 # size of x.right
        if x.right:
            x.right.parent = node
            bs = x.right.size

        node.size -= x.size
        node.size += bs

        x.size -= bs
        x.size += node.size

        x.parent = node.parent
        if node.parent == None:             self.root = x
        elif node == node.parent.right:     node.parent.right = x
        else:                               node.parent.left = x

        x.right = node
        node.parent = x
        


    def inc_size(self, node):
        ## modifying size of parents after inserting node
        while node.parent:
            node.parent.size += 1
            node = node.parent

            

    def rebalance(self, node):
        while node.parent.color == 1:  # if node.parent.color = black, then nothing to do
            if node.parent.parent and node.parent == node.parent.parent.right:
                u = node.parent.parent.left # u = parent's sibling
                if u and u.color == 1:
                    u.color = 0
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.rotate_right(node)
                    if node.parent: node.parent.color = 0
                    if node.parent.parent: node.parent.parent.color = 1
                    if node.parent.parent: self.rotate_left(node.parent.parent)
            elif node.parent.parent:
                u = node.parent.parent.right # u = parent's sibling

                if u and u.color == 1:
                    u.color = 0
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent 
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.rotate_left(node)
                    if node.parent: node.parent.color = 0
                    if node.parent.parent:
                        node.parent.parent.color = 1
                        self.rotate_right(node.parent.parent)
            if node == self.root:
                break
        self.root.color = 0
                            

    def count_less_than(self, x, exclude=False):
        t = self.root
        if t == None: return 0
        while True:
            if x < t.value and t.left:
                t = t.left
            elif x > t.value and t.right:
                t = t.right
            else: break
            
        while t and t.value > x:
            t = t.parent
            
        if t == None: return 0
        count = 1
        if t.value == x and exclude:
            count -= 1
            
        if t.left: count += t.left.size
        while t.parent:
            if t.parent.right == t:
                count += 1
                if t.parent.left: count += t.parent.left.size
            t = t.parent
            if t == None: break
        
        return count
        


tree = RedBlackTree()

for i in range(int(input())):
    s = input()
    if s[0] == '+':
        x = int(s.split()[1])
        tree.insert(x)
    else:
        s = s.split()
        l, r = int(s[1]), int(s[2])
        ans = tree.count_less_than(r) - tree.count_less_than(l, exclude=True)
        print(ans)
