

class Node:
    def __init__(self, value = None, colour = None):
        self.value = value
        self.colour = colour
        self.left = None
        self.right = None
        self.size = 1
        self.parent = None
    

class RedBlackTree:

    def __init__(self):
        self.root = None
    
    def left_rotate(self, node):
        x = node.size
        noder = node.right
        y = noder.size
        node.right = noder.left
        if noder.left is not None:
            noder.left.parent = node
        
        noder.parent = node.parent
        if node.parent is None:
            self.root = noder
        elif node.parent.left == node:
            node.parent.left = noder
        else:
             node.parent.right = noder
        noder.left = node
        node.parent = noder
        if node.right is not None:
            node.size = x - y + node.right.size
            noder.size = y - node.right.size + node.size
        else:
            node.size = x - y
            noder.size = y + node.size

    
    def right_rotate(self, node):
        x = node.size
        nodel = node.left
        y = nodel.size
        node.left = nodel.right
        if nodel.right is not None:
            nodel.right.parent = nodel
        nodel.parent = node.parent
        if node.parent is None:
            self.root = nodel
        elif node.parent.left == node:
            node.parent.left = nodel
        else:
            node.parent.right = nodel
        nodel.right = node
        node.parent = nodel
        if node.left is not None:
            node.size = x - y + node.left.size
            nodel.size = y - node.left.size + node.size
        else:
            node.size = x - y
            nodel.size = y + node.size


    def rebalance(self, node):
            while node.parent != self.root and node != self.root and node.parent.colour == 'r':
                
            #case1
                if node.parent.parent.left == node.parent:
                    y = node.parent.parent.right
                    if y is not None and y.colour == 'r':
                        node.parent.colour = 'b'
                        y.colour = 'b'
                        node.parent.parent.colour = 'r'
                        node = node.parent.parent
                        
                    #case2
                    elif y is None or y.colour == 'b':
                        if node.parent.right == node:
                            self.left_rotate(node.parent)
                            node = node.left
                        node.parent.colour = 'b'
                        node.parent.parent.colour = 'r'
                        self.right_rotate(node.parent.parent)
                        
                else:
                    y = node.parent.parent.left
                    if y is not None and y.colour == 'r':
                        node.parent.colour = 'b'
                        y.colour = 'b'
                        node.parent.parent.colour = 'r'
                        node = node.parent.parent
                        
                    #case2
                    elif y is None or y.colour == 'b': 
                        if node.parent.left == node:
                            self.right_rotate(node.parent)
                            node = node.right
                        node.parent.colour = 'b'
                        node.parent.parent.colour = 'r'
                        self.left_rotate(node.parent.parent)





    def insert(self, x):
        newnode = Node(x, 'r')
        a = None
        b = self.root
        while b is not None:
            a = b
            a.size += 1
            if x < b.value:
                b = b.left
            else:
                b = b.right
        newnode.parent = a
        if a is None:
            self.root = newnode
            self.root.colour = 'b'
            self.root.size = 1
        elif x < a.value:
            a.left = newnode
        else:
            a.right = newnode
        
        self.rebalance(newnode)
    
    def count(self, node, x):
        if node == None:
            return 0
        nodel = node.left
        noder = node.right
        
        if node.value <= x:
            if nodel is None:
                return 1 + self.count(noder, x)
            else:
                return 1 + nodel.size + self.count(noder, x)
        else:
            return self.count(node.left, x)

    def count_less_than(self, x):
        return self.count(self.root, x)
                          
    


                  
        
            

c = int(input())
rbt = RedBlackTree()
o = []
while c != 0:
    inp = input().split()
    if inp[0] == '+':
        rbt.insert(int(inp[1]))
    else:
        o.append(str(rbt.count_less_than(int(inp[2])) - rbt.count_less_than(int(inp[1]))))

    c -= 1

os = "\n".join(o)
print(os)


