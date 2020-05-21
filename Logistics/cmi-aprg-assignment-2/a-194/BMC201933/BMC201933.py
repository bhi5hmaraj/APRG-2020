class Node:
    def __init__(self,initval=None):
        self.value=initval
        self.left=None
        self.right=None
        self.size=0
        self.color=False
        self.parent=None
        
    
                    
    def leftsize(self):
        
        if self.left==None:
            return 0
        if self.left:
            return self.left.size
    def rightsize(self):
        if self.right:
            return self.right.size
        else:
            return 0
    
class RedBlackTree:
    def __init__(self,initval=None):
        self.root=initval
    
    
    def ninsert(self, x):
        if self.root == None:
            self.root = Node(x)
            self.root.size = 1
            return self.root
        if self.root:
            if self.root.value == x:
                return self.root
            else:
                if x < self.root.value:
                    if self.root.left:
                        self.root.size = self.root.size + 1
                        return RedBlackTree(self.root.left).ninsert(x)
                    else:
                        self.root.left = Node(x)
                        self.root.left.size = 1
                        self.root.left.parent = self.root
                        self.root.size = self.root.size + 1
                        return self.root.left
                else:
                    if self.root.right:
                        self.root.size = self.root.size + 1
                        return RedBlackTree(self.root.right).ninsert(x)
                    else:
                        self.root.right = Node(x)
                        self.root.right.size = 1
                        self.root.right.parent = self.root
                        self.root.size = self.root.size + 1
                        return self.root.right
    def find(self, x):
        if self.root == None:
            return
        if self.root:
            if self.root.value == x:
                return self.root
            else:
                if x < self.root.value:
                    return RedBlackTree(self.root.left).find(x)
                else:
                    return RedBlackTree(self.root.right).find(x)
            
    def leftrotate(self, n):
        m = n.right
        if self.root == n:
            self.root = m
            if m:
                m.parent = None
            
        else:
            if n == n.parent.left:
                n.parent.left = m
                
            else:
                n.parent.right = m
            if m:
                m.parent = n.parent
        n.right = m.left
        if n.right:
            n.right.parent = n
        if n.left:
            n.left.parent = n
        m.left = n
        n.parent = m
        n.size = n.leftsize() + n.rightsize() + 1
        m.size = m.leftsize() + m.rightsize() + 1
    
    def rightrotate(self, n):
        m = n.left
        if self.root == n:
            self.root = m
            if m:
                m.parent = None
            
        else:
            if n == n.parent.left:
                n.parent.left = m
                
            else:
                n.parent.right = m
            if m:
                m.parent = n.parent
        n.left = m.right
        if n.left:
            n.left.parent = n
        if n.right:
            n.right.parent = n
        m.right = n
        n.parent = m
        n.size = n.leftsize() + n.rightsize() + 1
        m.size = m.leftsize() + m.rightsize() + 1
        
    def rebalance(self , node):
        if node == self.root:
            if self.root.color == True:
                return
            else:
                self.root.color = True
                return
        else:
            if node.parent.color:
                return
            else:
                if node.parent.parent.left == node.parent:
                    if node.parent.parent.right == None or node.parent.parent.right.color == True:
                        if node.parent.right == node :
                            self.leftrotate(node.parent)
                            node.color = True
                            node.parent.color = False
                            self.rightrotate(node.parent)
                            self.root.color = True
                            return
                        else:
                            node.parent.color = True 
                            node.parent.parent.color = False
                            self.rightrotate(node.parent.parent)
                            self.root.color = True
                            return 
                    else:
                        node.parent.color = True
                        node.parent.parent.right.color = True
                        node.parent.parent.color = False
                        return self.rebalance(node.parent.parent)
                    
                    
                else:
                    if node.parent.parent.left == None or node.parent.parent.left.color == True:
                        if node.parent.left == node:
                            self.rightrotate(node.parent)
                            node.color = True
                            node.parent.color = False
                            self.leftrotate(node.parent)
                            self.root.color = True
                            return
                        else:
                            node.parent.color = True 
                            node.parent.parent.color = False
                            self.leftrotate(node.parent.parent)
                            self.root.color = True
                            return 
                    else:
                        node.parent.color = True
                        node.parent.parent.left.color = True
                        node.parent.parent.color = False
                        self.root.color = True
                        return self.rebalance(node.parent.parent)
                    
    def count_less_than_e(self, x):
        if self.root:
            if self.root.value > x :
                    return RedBlackTree(self.root.left).count_less_than_e(x)
            else:
                return (1 + self.root.leftsize() + RedBlackTree(self.root.right).count_less_than_e(x))
        else:
            return 0
    
    def count_less_than(self, x):
        if self.root:
            if self.root.value >= x :
                    return RedBlackTree(self.root.left).count_less_than(x) 
            else:
                return (1 + self.root.leftsize() + RedBlackTree(self.root.right).count_less_than(x))
        else:
            return 0
    def insert(self, x):
        if self.find(x):
            return
        else:
            return self.rebalance(self.ninsert(x))
    
self = RedBlackTree()
n = int(input())
for i in range(n):
    li = list(input().split())
    if li[0] == '+':
        self.insert(int(li[1]))
    else:
        print(str(self.count_less_than_e(int(li[2]))- self.count_less_than(int(li[1]))))
        
        
        
                        
                        
                        
                
                
            
            
          
        
        
            
    

