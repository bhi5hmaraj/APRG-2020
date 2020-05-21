class Node:
   
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.color = 'red'
        self.size = 1

class RedBlackTree:
   
    def __init__(self):
        self.root = None

    def insert(self, x):
        if self.search(self.root, x) == 0:
            z = Node(x)
            self.root = self.insertnode(self.root, z)      
            if not (self.root is z):
                z.parent = self.updateparent(self.root, z)
                self.rebalance(z)

            self.root.color = 'black'    
   
    def insertnode(self, root, node):
        if not root:
            root = node
        elif node.value < root.value:
            root.left = self.insertnode(root.left, node)
            root.size += 1
        else:
            root.right = self.insertnode(root.right, node)    
            root.size += 1

        return root
           
    def rebalance(self, node):
        if node is not self.root:
       
            if node.parent.color == 'red':
           
        #node's uncle is red
           
                if node.parent.parent.left and node.parent.parent.right and node.parent.parent.left.color == 'red' and node.parent.parent.right.color == 'red':
                    node.parent.parent.left.color = 'black'
                    node.parent.parent.right.color = 'black'
                    node.parent.parent.color = 'red'
                    self.rebalance(node.parent.parent)

        #node's uncle is black:
        #1. Left left case

                elif node.parent.left is node and node.parent.parent.left is node.parent:
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.right_rotate(node.parent.parent)

        #2. Left right case

                elif node.parent.parent.left is node.parent and node.parent.right is node:
                    self.left_rotate(node.parent)
                    self.rebalance(node.left)
                   
        #3. Right right case
                elif node.parent.right is node and node.parent.parent.right is node.parent:
                    node.parent.parent.color = 'red'
                    node.parent.color = 'black'
                    self.left_rotate(node.parent.parent)

        #4. Right left case
                elif node.parent.parent.right is node.parent and node.parent.left is node:
                    self.right_rotate(node.parent)
                    self.rebalance(node.right)                            
                   
    def updateparent(self, root, node):

        if root.left is node or root.right is node:
            node.parent = root
        elif node.value < root.value:
            node.parent = self.updateparent(root.left, node)
        else:
            node.parent = self.updateparent(root.right, node)
       
        return node.parent

    def left_rotate(self, x):

        y = x.right

        x.right = y.left
        
        if y.left != None:
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
        
        x.size = 1
        if x.left:
            x.size += x.left.size
        if x.right:
            x.size += x.right.size
            
        y.size = 1
        
        if y.left:
            y.size += y.left.size
        if y.right:
            y.size += y.right.size

    def right_rotate(self, x):
        
        y = x.left
        
        x.left = y.right
        
        if y.right != None:
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
        
        x.size = 1
        if x.left:
            x.size += x.left.size
        if x.right:
            x.size += x.right.size
            
        y.size = 1
        
        if y.left:
            y.size += y.left.size
        if y.right:
            y.size += y.right.size

    def printtree(self, root):
        
        if not root:
            return
        print(root.value, root.color, root.size)
        if root.left:
            self.printtree(root.left)
        if root.right:
            self.printtree(root.right)

    def no_of_elem(self, root):
        n = 0
        if root:
            n = 1 + self.no_of_elem(root.left) + self.no_of_elem(root.right)

        return n

    def updatesize(self, z):
        if z:
            z.size = self.no_of_elem(z)
            self.updatesize(z.left)
            self.updatesize(z.right)
       
 
    def count(self, root, x):
        n = 0
        if root:
            if root.value >= x:
                n = self.count(root.left, x)

            elif root.left:
                n = 1 + root.left.size + self.count(root.right, x)

            else:
                n = 1 + self.count(root.right, x)

        return n
   
    def search(self, root, x):
        k = 0
        if root:
            if root.value == x:
                k = 1
            elif root.value < x:
                k = self.search(root.right, x)
            else:
                k = self.search(root.left, x)

        return k
               
    def count_less_than(self, x):

        return self.count(self.root, x)
           
tree = RedBlackTree()

Q = input()
Q = int(Q)

for z in range(Q):
    i = input().split()
    if i[0] == '+' :
        n = i[1]
        n = int(n)
        tree.insert(n)
        #print('-----')
        #tree.printtree(tree.root)
    elif i[0] == '?':
        
        a = i[1]
        b = i[2]
        b = int(b)
        a = int(a)
        if b >= a:
            print(tree.count_less_than(b+1) - tree.count_less_than(a))

