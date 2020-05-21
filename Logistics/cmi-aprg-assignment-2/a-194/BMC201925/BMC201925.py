class Node:

    def __init__(self, value = None, left = None, right = None, parent = None, size = 0, color = True):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.size = size
        self.color = color

class RedBlackTree:

    def __init__(self):
        self.root = None

    def right_rotate(self, node):
        if not node.left:
            return

        new_size = node.size - node.left.size
        if node.left.right:
            new_size += node.left.right.size
        new_node = Node(node.value, node.left.right, node.right, node, new_size, node.color)
        node.value = node.left.value
        node.color = node.left.color
        node.left = node.left.left
        node.right = new_node
        if node.left:
            node.left.parent = node
        if node.right.left:
            node.right.left.parent = node.right
        if node.right.right:
            node.right.right.parent = node.right


    def left_rotate(self, node):
        if not node.right:
            return

        new_size = node.size - node.right.size
        if node.right.left:
            new_size += node.right.left.size
        new_node = Node(node.value, node.left, node.right.left, node, new_size, node.color)
        node.value = node.right.value
        node.color = node.right.color
        node.right = node.right.right
        node.left = new_node
        if node.right:
            node.right.parent = node
        if node.left.right:
            node.left.right.parent = node.left
        if node.left.left:
            node.left.left.parent = node.left

    def rebalance(self, node):
        if not node:
            return

        #L L
        if node.left and node.left.left and not node.left.color and not node.left.left.color:
            # print("HEY LL")
            if not node.right or node.right.color:
                self.right_rotate(node)
                node.color = True
                node.right.color = False
            else:
                node.left.color = True
                node.right.color = True
                if node.parent:
                    node.color = False
            return

        #L R
        if node.left and node.left.right and not node.left.color and not node.left.right.color:
            # print("HEY LR")
            if not node.right or node.right.color:
                self.left_rotate(node.left)
                self.right_rotate(node)
                node.color = True
                node.right.color = False
            else:
                node.left.color = True
                node.right.color = True
                if node.parent:
                    node.color = False
            return

        #R R
        if node.right and node.right.right and not node.right.color and not node.right.right.color:
            # print("HEY RR")
            # self.printTree(node)
            if not node.left or node.left.color:
                self.left_rotate(node)
                node.color = True
                node.left.color = False
            else:
                node.left.color = True
                node.right.color = True
                if node.parent:
                    node.color = False
            return

        #R L
        if node.right and node.right.left and not node.right.color and not node.right.left.color:
            # print("HEY RL")
            if not node.left or node.left.color:
                self.right_rotate(node.right)
                self.left_rotate(node)
                node.color = True
                node.left.color = False
            else:
                node.left.color = True
                node.right.color = True
                if node.parent:
                    node.color = False
            return

    def insertValue(self, curNode, value):
        if value < curNode.value:
            if not curNode.left:
                curNode.left = Node(value = value, parent = curNode, size = 1, color = False)
            else:
                self.insertValue(curNode.left, value)
        else:
            if not curNode.right:
                curNode.right = Node(value = value, parent = curNode, size = 1, color = False)
            else:
                self.insertValue(curNode.right, value)
        curNode.size += 1
        self.rebalance(curNode)
        # if curNode.parent:
        #     self.printTree(curNode.parent)
        # self.rebalance(curNode.parent)

    def insert(self, value):
        if self.root:
            if not self.find(self.root, value):
                self.insertValue(self.root, value)
        else:
            self.root = Node(value, None, None, None, 1, True)

    def find(self, node, value):
        if not node:
            return False
        if node.value == value:
            return True
        if value < node.value:
            return self.find(node.left, value)
        return self.find(node.right, value)

    def count(self, node, value):
        if not node:
            return 0
        if value <= node.value:
            return self.count(node.left, value)
        if node.left:
            return 1 + node.left.size + self.count(node.right, value)
        return 1 + self.count(node.right, value)

    def count_less_than(self, value):
        return self.count(self.root, value)

    def query(self, l, r):
        return self.count_less_than(r + 1) - self.count_less_than(l)

    def printTree(self, node):
        print(node.value, end="")
        print(" | Color = ", node.color, end="")
        print(" | Size = ", node.size, end="")
        if node.parent:
            print(" | Parent = ", node.parent.value, end="")
        if node.left:
            print(" | left = ", node.left.value, end="")
        if node.right:
            print(" | right = ", node.right.value, end="")
        print()
        if node.left:
            self.printTree(node.left)
        if node.right:
            self.printTree(node.right)

number_of_queries = int(input())
rbTree = RedBlackTree()

while number_of_queries > 0:
    inp = input().split(' ')
    if inp[0] == '+':
        x = int(inp[1])
        rbTree.insert(x)
    else:
        l = int(inp[1])
        r = int(inp[2])
        print(rbTree.query(l, r))
    # rbTree.printTree(rbTree.root)
    number_of_queries -= 1
# rbTree.printTree(rbTree.root)
