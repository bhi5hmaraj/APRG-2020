class Node:
    def __init__(self, val):
        self.value = val
        self.parent = None
        self.left = None
        self.right = None
        self.size = 1
        self.color = False


class RedBlackTree:
    def __init__(self, node=None):
        self.root = node

    def left_rotate(self, node):
        papa = node.parent
        baby = node.right
        beta = baby.left
        baby.parent = papa
        node.parent = baby
        node.right = beta
        baby.left = node
        if beta is None:
            pass
        else:
            beta.parent = node
        if node.left is None:
            a = 0
        else:
            a = node.left.size
        if baby.right is None:
            c = 0
        else:
            c = baby.right.size
        if papa is None:
            self.root = baby
        else:
            if node == papa.left:
                papa.left = baby
            else:
                papa.right = baby
        node.size -= 1 + c
        baby.size += 1 + a

    def right_rotate(self, node):
        papa = node.parent
        baby = node.left
        beta = baby.right
        baby.parent = papa
        node.parent = baby
        node.left = beta
        baby.right = node
        if beta is None:
            pass
        else:
            beta.parent = node
        if node.right is None:
            a = 0
        else:
            a = node.right.size
        if baby.left is None:
            c = 0
        else:
            c = baby.left.size
        if papa is None:
            self.root = baby
        else:
            if node == papa.left:
                papa.left = baby
            else:
                papa.right = baby
        node.size -= 1 + c
        baby.size += 1 + a

    def count_less_than(self, x):
        r = self.root
        if r is None:
            return 0
        else:
            v = r.value
            if r.left is None:
                a = 0
            else:
                a = r.left.size
            if x == v:
                return a
            elif x > v:
                return 1 + a + RedBlackTree(r.right).count_less_than(x)
            else:
                return RedBlackTree(r.left).count_less_than(x)

    def find(self, x):
        r = self.root
        if r is None:
            return False
        else:
            v = r.value
            if x == v:
                return True
            elif x > v:
                return RedBlackTree(r.right).find(x)
            else:
                return RedBlackTree(r.left).find(x)

    def insert_violate(self, x):
        z = Node(x)
        r = self.root
        if r is None:
            self.root = z
            return None
        else:
            r.size += 1
            z.color = True
            if x > r.value:
                if r.right is None:
                    r.right = z
                    z.parent = r
                    if r.color:
                        return z
                    else:
                        return None
                else:
                    return RedBlackTree(r.right).insert_violate(x)
            else:
                if r.left is None:
                    r.left = z
                    z.parent = r
                    if r.color:
                        return z
                    else:
                        return None
                else:
                    return RedBlackTree(r.left).insert_violate(x)

    def fix_rb_property(self, z):
        p = z.parent
        g = p.parent
        if g.left == p:
            y = g.right
        else:
            y = g.left

        if y is None or y.color is False:
            if g.left == p:
                if p.right == z:
                    self.left_rotate(p)
                    self.right_rotate(g)
                    z.color = False
                else:
                    self.right_rotate(g)
                    p.color = False
            else:
                if p.left == z:
                    self.right_rotate(p)
                    self.left_rotate(g)
                    z.color = False
                else:
                    self.left_rotate(g)
                    p.color = False
            g.color = True
        else:
            p.color = False
            y.color = False
            g.color = True
            if g == self.root:
                g.color = False
            else:
                if g.parent.color:
                    self.fix_rb_property(g)
                else:
                    pass

    def insert(self, x):
        if self.find(x):
            pass
        else:
            z = self.insert_violate(x)
            if z is None:
                pass
            else:
                self.fix_rb_property(z)

    def count_in_range(self, low, high):
        if low > high:
            return 0
        else:
            ans = self.count_less_than(high)- self.count_less_than(low)
            if self.find(high):
                ans += 1
            return ans


RBT = RedBlackTree()
Q = int(input())
for t in range(Q):
    inp = input().strip().split()
    if inp[0] == "?":

        print(RBT.count_in_range(int(inp[1]),int(inp[2])))
    else:
        RBT.insert(int(inp[1]))
