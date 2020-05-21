BLACK = 0
RED = 1

class Node(object):
    
    def __init__(self, value):    
        self.parent = None
        self.left = None
        self.right = None
        self.value = value
        self.color = RED
    
    def size(self):
        return subtree_size(self)
        
        
    def insert(self, data):
        if data == self.value:
            return False
        elif data < self.value:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True

        
def subtree_size(root):
    visited = 0
    if not root: return visited
    stack = [root]
    while stack:
        node = stack.pop()
        visited += 1
        if node.left: stack.append(node.left)
        if node.right: stack.append(node.right)
    return visited


def countlessthan(node, x):
    if node == None:
        return 0
    count = 0
    if node.value >= x:
        count = countlessthan (node.left, x)
    else:
        count = 1
        if node.left != None:
            count += node.left.size()
        count += countlessthan (node.right, x)
    return count   


class RedBlackTree(object):
    
    def __init__(self):
        self.root = None
        
    def insertFixup(self, x):
        
        while x != self.root and x.parent.color == RED:

            if x.parent == x.parent.parent.left:

                y = x.parent.parent.right

                if y.color == RED:
                    x.parent.color = BLACK
                    y.color = BLACK
                    x.parent.parent.color = RED
                    x = x.parent.parent

                else:
                    if x == x.parent.right:
                        x = x.parent
                        self.left_rotate(x)

                    x.parent.color = BLACK
                    x.parent.parent.color = RED
                    self.right_rotate(x.parent.parent)
            else:

                y = x.parent.parent.left

                if y.color == RED:
                    x.parent.color = BLACK
                    y.color = BLACK
                    x.parent.parent.color = RED
                    x = x.parent.parent

                else:
                    if x == x.parent.left:
                        x = x.parent
                        self.right_rotate(x)

                    x.parent.color = BLACK
                    x.parent.parent.color = RED
                    self.left_rotate(x.parent.parent)

        self.root.color = BLACK

    def insertnode (self, node): 
        
        if self.root:
            return self.root.insert(node)
        else:
            self.root = Node(node)
            return True
            
        self.insertFixup(node)
        return node

                    
                    
    def left_rotate(self, z):
        y = z.right 
        T2 = y.left 
        y.left = z 
        z.right = T2 
        return y 
    
    def right_rotate(self, z):
        y = z.left 
        T3 = y.right 
        y.right = z 
        z.left = T3   
        return y 
    
    def count_less_than(self, x):
        return countlessthan(self.root, x)

    def count_between(self, y, x):
        return (self.count_less_than(x+1) - self.count_less_than(y))

tree = RedBlackTree()
    
n =  int(input())
for i in range(n):
    s = input().split()
    if len(s) == 2:
        y = int(s[1])
        tree.insertnode(y)
      
    else:
        y = int(s[1])
        x = int(s[2])
        print(tree.count_between(y, x))
