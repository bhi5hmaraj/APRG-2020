
class Node:

    BLACK = 0
    RED = 1

    LEFT = 1
    RIGHT = 2

    def __init__(self, value, color = RED, parent = None,
                 left = None, right = None, size = 1, lr = None):

        self.value = value
        self.color = color
        self.parent = parent
        self.left = left
        self.right = right
        self.size = size
        self.lr = lr

    def is_left_child(self):
        return (self.lr == Node.LEFT)

    def is_right_child(self):
        return (self.lr == Node.RIGHT)

    def desc(self):
        return f'{self.value}, {self.color}, {self.size}, {self.parent.value if self.parent else None}'


class RedBlackTree:

    def __init__(self, root = None):
        self.root = root


    def fix_size(self, node):
        left_size = self.fix_size(node.left) if node.left else 0
        right_size = self.fix_size(node.right) if node.right else 0
        node.size = 1 + left_size + right_size
        return node.size


    def rec_insert(self, node, value):
        if value == node.value:
            return

        if value < node.value:
            if not node.left:
                node.left = Node(value, parent = node, lr = Node.LEFT)
                return node.left
            return self.rec_insert(node.left, value)

        else:
            if not node.right:
                node.right = Node(value, parent = node, lr = Node.RIGHT)
                return node.right
            return self.rec_insert(node.right, value)


    def insert(self, value):
        if not self.root:
            self.root = Node(value, color = Node.BLACK)
            return
        new_node = self.rec_insert(self.root, value)

        if not new_node:
            return
            
        self.rebalance(new_node)

        while self.root.parent:
            self.root = self.root.parent

        self.fix_size(self.root)
        self.root.color = Node.BLACK


    def rotate_left(self, node):
        if not node.right:
            return

        node_left_child = node.is_left_child()
        x, y, z, beta = node, node.right, node.parent, node.right.left
        node.parent, node.right, y.parent, y.left = y, beta, x.parent, node

        if beta:
            beta.parent = node
            beta.lr = Node.RIGHT

        if node_left_child:
            if z:
                z.left = y
            y.lr = Node.LEFT
        else:
            if z:
                z.right = y
            x.lr = Node.LEFT


    def rotate_right(self, node):
        if not node.left:
            return

        node_right_child = node.is_right_child()
        y, x, z, beta = node, node.left, node.parent, node.left.right
        node.parent, node.left, x.parent, x.right = x, beta, y.parent, node

        if beta:
            beta.parent = node
            beta.lr = Node.LEFT

        if node_right_child:
            if z:
                z.right = x
            x.lr = Node.RIGHT
        else:
            if z:
                z.left = x
            y.lr = Node.RIGHT


    def rebalance_red_uncle(self, node, node_uncle):

        node.parent.color = Node.BLACK

        if node_uncle:
            node_uncle.color = Node.BLACK
        
        node.parent.parent.color = Node.RED
        return
    

    def rebalance_black_uncle(self, node):
        
        if node.is_right_child() and node.parent.is_left_child():
            self.rotate_left(node.parent)
            node = node.left

        elif node.is_left_child() and node.parent.is_right_child():
            self.rotate_right(node.parent)
            node = node.right

        node.parent.color = Node.BLACK
        node.parent.parent.color = Node.RED

        if node.is_left_child():
            self.rotate_right(node.parent.parent)
        
        if node.is_right_child():
            self.rotate_left(node.parent.parent)

        return


    def rebalance(self, node):

        if not node.parent or not node.parent.parent:
            return

        if node.parent.color == Node.BLACK:
            return

        node_uncle = None
        if node.parent.is_left_child():
            node_uncle = node.parent.parent.right

        elif node.parent.is_right_child():
            node_uncle = node.parent.parent.left

        if node_uncle and node_uncle.color == Node.RED:
            self.rebalance_red_uncle(node, node_uncle)
            self.rebalance(node.parent.parent)
        else:
            self.rebalance_black_uncle(node)


    def count_nodes_in_range(self, node, count, min, max):
        if not node:
            return 0

        count = self.count_nodes_in_range(node.left, count, min, max)

        if min <= node.value <= max:
            count += 1

        count += self.count_nodes_in_range(node.right, count, min, max)
        return count


    def print_rb_tree(self, node, level = 0):
        if not node:
            return

        self.print_rb_tree(node.right, level + 1)
        print((level+1)*'----', end=' ')
        print(f"{node.value}({'b' if node.color == Node.BLACK else 'r'})({node.size})")
        self.print_rb_tree(node.left, level + 1)

        return


    def print_tree(self):
        self.print_rb_tree(self.root)


def main():
    rbtree = RedBlackTree()

    no_inputs = int(input())
    while no_inputs > 0:
        values = input().split()
        
        if len(values) == 2 and values[0] == '+':
            rbtree.insert(int(values[1]))

        elif len(values) == 3 and values[0] == '?':
            rmin, rmax = int(values[1]), int(values[2])
            if rmin > rmax:
                rmax, rmin = rmin, rmax

            count = rbtree.count_nodes_in_range(rbtree.root, 0, rmin, rmax)
            print(count)

        no_inputs -= 1

    #rbtree.print_tree()

if __name__ == '__main__':
    main()

