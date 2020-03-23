# This is an implementation of a Red Black tree from CLRS

global RED, BLACK

RED = 0
BLACK = 1

class Node:

    # 0 - red , 1 - black 
    def __init__(self, val, left=None, right=None, parent=None, size=1, color=RED):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        self.size = size
        self.color = color


class RedBlackTree():

    global NIL, DEBUG

    DEBUG = False
    NIL = Node(val=-1, color=BLACK, size=0)


    def check(curr):
        if curr != NIL:
            assert curr.size == 1 + curr.left.size + curr.right.size
            l = RedBlackTree.check(curr.left)
            r = RedBlackTree.check(curr.right)
            assert l == r
            return l + (1 if curr.color == BLACK else 0)
        else:
            return 0


    def check_tree(self):
        print("Checking ... ")
        assert self.root.color == BLACK, "Root isn't black"
        assert RedBlackTree.check(self.root)
        print("Looks fine !")

    def print_tree(self):
        print('\n'.join(RedBlackTree.pretty_print("", True, [], self.root)))
        # RedBlackTree.inorder_print(self.root)

    def pretty_print(prefix, isTail, sb, root):
        if root == NIL:
            return ["Tree is empty"]

        if root.right != NIL:
            RedBlackTree.pretty_print(prefix + ("|   " if isTail else "    "), False, sb, root.right)

        # sb.append(prefix + "|-- " + str(root.val) + " (p = {}, c = {}, sz = {})".format(root.parent.val, root.color, root.size))
        sb.append(prefix + "|-- " + str(root.val))
        if root.left != NIL:
            RedBlackTree.pretty_print(prefix + ("|   " if not isTail else "    "), True, sb, root.left)

        return sb

    def update_size(node):
        node.size = 1 + node.left.size + node.right.size

    def count_less_than(curr, x):
        if curr == NIL:
            return 0
        elif x <= curr.val:
            return RedBlackTree.count_less_than(curr.left, x)
        else:
            return 1 + curr.left.size + RedBlackTree.count_less_than(curr.right, x)

    def get_count_in_range(self, l, r):
        return RedBlackTree.count_less_than(self.root, r + 1) - RedBlackTree.count_less_than(self.root, l)

    def fixup(self, curr):
        while curr.parent.color == RED:

            if DEBUG : print(curr.val, "inside fix")
            
            if curr.parent == curr.parent.parent.left:
                y = curr.parent.parent.right    # uncle of curr
                if y.color == RED:
                    curr.parent.color = BLACK
                    y.color = BLACK
                    curr.parent.parent.color = RED
                    curr = curr.parent.parent
                else:
                    if curr == curr.parent.right:   # uncle is not red and curr is right child
                        curr = curr.parent
                        self.left_rotate(curr)

                    curr.parent.color = BLACK
                    curr.parent.parent.color = RED
                    self.right_rotate(curr.parent.parent)
            else:
                y = curr.parent.parent.left
                if y.color == RED:
                    curr.parent.color = BLACK
                    y.color = BLACK
                    curr.parent.parent.color = RED
                    curr = curr.parent.parent
                else:
                    if curr == curr.parent.left:
                        curr = curr.parent
                        self.right_rotate(curr)

                    curr.parent.color = BLACK
                    curr.parent.parent.color = RED
                    self.left_rotate(curr.parent.parent)

        self.root.color = BLACK

    def b_height(curr):
        h = 0
        curr = curr.left
        while curr != NIL:
            h += 1 if curr.color == BLACK else 0
            curr = curr.left # leftist ! 

        return h

    def get_height(self):
        return RedBlackTree.b_height(self.root)

    def insert(self, x):
        # self.root = RedBlackTree.insert_(self, self.root, x)

        # self.root.parent = NIL
        y = NIL
        curr = self.root
        while curr != NIL:
            y = curr
            if curr.val == x:
                return
            curr = curr.left if x < curr.val else curr.right

        new_node = Node(val=x, left=NIL, right=NIL)
        new_node.parent = y
        if y == NIL:
            self.root = new_node
        elif new_node.val < y.val:
            y.left = new_node
        else:
            y.right = new_node

        curr = new_node.parent
        while curr != NIL:
            RedBlackTree.update_size(curr)
            curr = curr.parent

        self.fixup(new_node)    
        if DEBUG:            
            print(new_node.val)
            self.print_tree()
            print("Height ", self.get_height())
            self.check_tree()

    # Need to update b_height, cnt and all other fields !



    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != NIL:
            y.left.parent = x
        y.parent = x.parent

        if x.parent == NIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y
        RedBlackTree.update_size(x)
        RedBlackTree.update_size(y)

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != NIL:
            x.right.parent = y
        x.parent = y.parent

        if y.parent == NIL:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x

        x.right = y
        y.parent = x
        RedBlackTree.update_size(y)
        RedBlackTree.update_size(x)



    def __init__(self, root=None):
        self.root = NIL




# rbtree = RedBlackTree()
# for i in range(20):
#     rbtree.insert(i)

# rbtree.print_tree()
# l = 10
# r = 15

# print("count in range %d to %d" % (l, r), rbtree.get_count_in_range(l, r))

def solve():

    rbtree = RedBlackTree()
    q = int(input())
    for _ in range(q):
        line = input().split()
        if line[0] == '+':
            rbtree.insert(int(line[1]))
        else:
            l, r = map(int, line[1:])
            print(rbtree.get_count_in_range(l, r))

