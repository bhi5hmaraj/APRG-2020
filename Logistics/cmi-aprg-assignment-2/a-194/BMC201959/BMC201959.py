class Node:
    def __init__(self, value, rb):
        self.size = 1
        self.color = rb
        self.left = None
        self.right = None
        self.parent = None
        self.value = value


class RedBlackTree:
    def __init__(self):
        self.root = None

    def element(self, a, b):
        if a is None:
            return False
        elif a.value == b:
            return True
        elif b < a.value:
            if a.left.size == 0:
                return False
            else:
                return self.element(a.left, b)
        else:
            if a.right.size == 0:
                return False
            else:
                return self.element(a.right, b)

    def insert(self, a):
        b = Node(a, 1)
        child1 = Node(None, 0)
        child2 = Node(None, 0)
        b.left = child1
        b.right = child2
        child1.size = 0
        child2.size = 0
        c = self.root
        if self.element(self.root, a):
            return self
        else:
            if self.root is None:
                self.root = b
                self.root.color = 0
                return
            else:
                while c.left is not None and c.right is not None:
                    if c.value > a:
                        if c.left is not None and c.left.size > 0:
                            c.size += 1
                            c = c.left
                        else:
                            break
                    else:
                        if c.right is not None and c.right.size > 0:
                            c.size += 1
                            c = c.right
                        else:
                            break
                if c.value > a:
                    c.left = b
                else:
                    c.right = b
                b.parent = c
                c.size += 1
            return self.rebalance(a)

    def left_rotate(self, a):
        if a == self.root:
            b = a.right
            c = b.left
            a.size -= (b.right.size + 1)
            self.root = b
            b.parent = None
            b.left = a
            a.parent = b
            a.right = c
            c.parent = a
            b.size = b.left.size + 1 + b.right.size
        else:
            b = a.right
            c = b.left
            d = a.parent
            if d.right == a:
                a.size -= (b.right.size + 1)
                d.right = b
                b.parent = d
                b.left = a
                a.parent = b
                a.right = c
                c.parent = a
            else:
                a.size -= (b.right.size + 1)
                d.left = b
                b.parent = d
                b.left = a
                a.parent = b
                a.right = c
                c.parent = a
            b.size = b.left.size + 1 + b.right.size

    def right_rotate(self, a):
        if a == self.root:
            b = a.left
            c = b.right
            a.size -= (b.left.size + 1)
            self.root = b
            b.parent = None
            b.right = a
            a.parent = b
            a.left = c
            c.parent = a
            b.size = b.left.size + 1 + b.right.size
        else:
            b = a.left
            c = b.right
            d = a.parent
            if d.right == a:
                a.size -= (b.left.size + 1)
                d.right = b
                b.parent = d
                b.right = a
                a.parent = b
                a.left = c
                c.parent = a
            else:
                a.size -= (b.left.size + 1)
                d.left = b
                b.parent = d
                b.right = a
                a.parent = b
                a.left = c
                c.parent = a
            b.size = b.left.size + 1 + b.right.size

    def rebalance(self, a):
        b = self.search(self.root, a)
        if self.root.value == a:
            self.root.color = 0
            return
        elif b.parent.color == 0:
            return
        elif b.parent.color == 1:
            grandparent = b.parent.parent
            par = b.parent
            if grandparent.left == par:
                uncle = grandparent.right
            else:
                uncle = grandparent.left
            if uncle.color == 1:
                par.color = 0
                uncle.color = 0
                grandparent.color = 1
                return self.rebalance(grandparent.value)
            else:
                if par.left == b:
                    if uncle == grandparent.right:
                        par.color = 0
                        grandparent.color = 1
                        self.right_rotate(grandparent)
                        return
                    else:
                        self.right_rotate(par)
                        return self.rebalance(par.value)
                else:
                    if uncle == grandparent.right:
                        self.left_rotate(par)
                        return self.rebalance(par.value)
                    else:
                        grandparent.color = 1
                        par.color = 0
                        self.left_rotate(grandparent)
                        return

    def search(self, a, b):
        if a.value == b:
            b = a
            return b
        else:
            if b < a.value:
                a = a.left
                return self.search(a, b)
            else:
                a = a.right
                return self.search(a, b)

    def count_less_than(self, a):
        if self.root is None:
            return 0
        elif self.root.value == a:
            return self.root.left.size
        else:
            b = self.root
            c = 0
            while b.value != a and b.value is not None:
                if b.value > a:
                    b = b.left
                else:
                    c = c + b.left.size + 1
                    b = b.right
            if b.value is not None:
                return c + b.left.size
            else:
                return c


inp = int(input())
p = []
q = []
for i in range(inp):
    p.append(input().split())
r = RedBlackTree()
for i in range(inp):
    if p[i][0] == '+':
        r.insert(int(p[i][1]))
    elif p[i][0] == '?':
        result = (r.count_less_than(int(p[i][2])) - r.count_less_than(int(p[i][1])))
        if r.element(r.root, int(p[i][2])):
            q.append(result + 1)
        else:
            q.append(result)
for i in range(len(q)):
    print(q[i])
print()

