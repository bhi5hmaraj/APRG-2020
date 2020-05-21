# Implementing Red-Black Tree in Python

import sys

class Node():
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.size = 0
        self.color = 1

class RedBlackTree():
    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL

    def sizeOf(self, node):
        return node.size if node else 0
    
    def  __fix_insert(self, k):
        while k.parent.color == 1: # if parent is red
            if k.parent == k.parent.parent.right: # if parent is right child of GP
                u = k.parent.parent.left # uncle -> left of GP
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
            else: #if parent is left child of GP
                u = k.parent.parent.right # uncle -> right of GP

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

    def left_rotate(self, x):

        # x.size, x.right.size = self.sizeOf(x.left) + self.sizeOf(x.right.left) + 1, x.size

        y = x.right
        x.size, y.size = self.sizeOf(x.left) + self.sizeOf(y.left) + 1, x.size
        x.right = y.left
        if y.left != self.TNULL:
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

    def right_rotate(self, x):

        # x.size, x.left.size = self.sizeOf(x.right) + self.sizeOf(x.left.right) + 1, x.size
        
        y = x.left
        x.size, y.size = self.sizeOf(x.right) + self.sizeOf(y.right) + 1, x.size
        x.left = y.right
        if y.right != self.TNULL:
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

    def insert(self, key):
        node = Node(key)
        node.parent = None
        node.data = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 1
        node.size = 1

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y == None:
            self.root = node
        elif node.data < y.data:
            y.left = node
            while y!=None:
                y.size = y.size + 1
                y = y.parent
        else:
            y.right = node
            while y!=None:
                y.size = y.size + 1
                y = y.parent

        if node.parent == None:
            node.color = 0
            return

        if node.parent.parent == None:
            return

        self.__fix_insert(node)

    def __print_helper(self, node, indent, last):
        if node != self.TNULL:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print(str(node.data) + "(" + s_color + "," + str(node.size) + ")")
            self.__print_helper(node.left, indent, False)
            self.__print_helper(node.right, indent, True)

    def print_tree(self):
        self.__print_helper(self.root, "", True)

    def __search_tree_helper(self, node, key):
        if node == self.TNULL or key == node.data:
            return node

        if key < node.data:
            return self.__search_tree_helper(node.left, key)
        return self.__search_tree_helper(node.right, key)

    def searchTree(self, k):
        return self.__search_tree_helper(self.root, k)
        
    def getCount(self, root, low, high): 
        if root == None:        #Base case
            return 0
 
        if root.data == high and root.data == low:    #Optional, for efficiency
            return 1
     
        if root.data <= high and root.data >= low:  
            return (1 + self.getCount(root.left, low, high) + self.getCount(root.right, low, high))
                         

        elif root.data < low:  
            return self.getCount(root.right, low, high) 
  
        else: 
            return self.getCount(root.left, low, high)

    def rank(self, node, key):
        r = 0
        # print('For key {0}'.format(key))
        while(node):
            if key<node.data:
                node = node.left
            elif key>node.data:
                # print('> Printing size of left node {0}'.format(self.sizeOf(node.left)))
                r=r+1+self.sizeOf(node.left)
                # print('Printing value of r {0}'.format(r))
                node=node.right
            else:
                # print('== Printing size of left node {0}'.format(self.sizeOf(node.left)))
                return r+self.sizeOf(node.left)+1
                # print('Printing value of r {0}'.format(r))
        return r-1

    def countByRank(self, l, h):
        hNode = self.searchTree(h)
        lNode = self.searchTree(l)
        lRank = self.rank(self.root, l)
        hRank = self.rank(self.root, h)
        # print('Rank for l {0} : {1}'.format(str(l), str(lRank)))
        # print('Rank for h {0} : {1}'.format(str(h), str(hRank)))
        if lNode != self.TNULL:
            return hRank - lRank + 1
        return hRank - lRank

if __name__ == "__main__":

    NumberOfOperations = int(input())
    INPUT = []
    res = []
    RBObject = RedBlackTree()
    for i in range(0, NumberOfOperations):
        INPUT.append(input())
    if NumberOfOperations > 100000:
        NumberOfOperations = 100000


    for i in range(0,NumberOfOperations):
        inp = INPUT[i].split(" ")
        if inp[0] == "+":
            if RBObject.searchTree(int(inp[1])) != RBObject.TNULL:
                continue
            RBObject.insert(int(inp[1]))
            # RBObject.print_tree()
        else:
            # result = RBObject.getCount(RBObject.root, int(inp[1]), int(inp[2]))
            result = RBObject.countByRank(int(inp[1]), int(inp[2]))
            res.append(str(result))

    print("\n".join(res))
