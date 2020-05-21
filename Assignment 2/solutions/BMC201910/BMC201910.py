import sys
sys.setrecursionlimit(10**6)

nlist = []
for j in range(100000 + 1):
    nlist.append(0)

class Node:
    def __init__(self,value,color='red',size= 1):
        self.value = value
        self.color=color
        self.left=None
        self.right=None
        self.parent=None
        self.size=size
    
    def newSize(self):
        if (self.left != None) and (self.right != None):
            self.size= self.left.size + self.right.size +1
        elif (self.left != None):
            self.size= self.left.size + 1
        elif (self.right != None):
            self.size= self.right.size + 1
        else:
            self.size=1
            
    def newParent(self):
        if self.right != None:
            self.right.parent = self
        if self.left != None:
            self.left.parent = self
                
class RedBlackTree:
    def __init__(self):
        self.root = None
    
    def right_rotate(self,node):
        if node.left != None:
            x = node
            node = node.left
            if self.root ==x:
                self.root = node
                node.parent = None
            else:
                if x == x.parent.left:
                    x.parent.left = node
                else:
                    x.parent.right = node
                node.parent = x.parent
            x.left = node.right
            node.right = x
            node.newParent()
            node.right.newParent()
            node.right.newSize()
            node.newSize()
            if (self.root != node):
                node.parent.newSize()
        
    def left_rotate(self,node):
        if node.right != None:
            x = node
            node = node.right
            if self.root == x:
                self.root = node
                node.parent = None
            else:
                if x == x.parent.left:
                    x.parent.left = node
                else:
                    x.parent.right = node
                node.parent = x.parent
            x.right = node.left
            node.left = x
            node.newParent()
            node.left.newParent()
            node.left.newSize()
            node.newSize()
            if(self.root != node):
                node.parent.newSize()
        
    def insert(self,x,node):
        nlist[x] = 1
        if (self.root == None) :
            neu = Node(x,'black')
            self.root = neu
            return
        else:
            while(node != None):
                if x < node.value:
                    if node.left == None:
                        neu = Node(x)
                        node.left = neu
                        neu.parent = node
                        node.size = node.size + 1
                        if(node.color == 'red'):
                            self.rebalance(neu)
                        break
                    else:
                        node.size = node.size + 1
                        node = node.left
                        continue
                elif x > node.value:
                    if node.right == None:
                        neu = Node(x)
                        node.right = neu
                        neu.parent = node
                        node.size = node.size + 1
                        if(node.color == 'red'):
                            self.rebalance(neu)
                        break
                    else:
                        node.size = node.size + 1
                        node = node.right
                        continue
                          
    def rebalance(self , node):
        if (node == self.root):
            node.color = 'black'
            return
        if(node.parent == node.parent.parent.left):
            if(node.parent.parent.right != None and node.parent.parent.right.color == 'red'):
                node.parent.color = 'black';
                node.parent.parent.right.color = 'black'
                node.parent.parent.color = 'red'
                if(node.parent.parent == self.root or node.parent.parent.parent.color == 'red'):
                    self.rebalance(node.parent.parent)
                return
            else:
                if(node == node.parent.right):
                    self.left_rotate(node.parent)
                    node.color = 'black'
                    node.parent.color = 'red'
                    self.right_rotate(node.parent)
                else:
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.right_rotate(node.parent.parent)
                return
        else:
            if(node.parent.parent.left != None and node.parent.parent.left.color == 'red'):
                node.parent.color = 'black';
                node.parent.parent.left.color = 'black'
                node.parent.parent.color = 'red'
                if(node.parent.parent == self.root or node.parent.parent.parent.color == 'red'):
                    self.rebalance(node.parent.parent)
            else:
                if(node == node.parent.left):
                    self.right_rotate(node.parent)
                    node.color = 'black'
                    node.parent.color = 'red'
                    self.left_rotate(node.parent)
                else:
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.left_rotate(node.parent.parent)
                return

            

    def count_less_than(self , node , x):
        if node == None:
            return 0
        else:
            if node.value > x:
                return self.count_less_than(node.left , x)
            else:
                s = self.count_less_than(node.right , x)
                if(node.left == None):
                    return s + 1
                else:
                    return s + 1 + node.left.size
            
    def countGreat(self , node , x):
        if node == None:
            return 0
        else:
            if node.value < x:
                return self.countGreat(node.right , x)
            else:
                s = self.countGreat(node.left , x)
                if(node.right == None):
                    return (1 + s)
                else:
                    return (s + node.right.size + 1)
        
    
    
    def output(self , node , a , b):
        if node == None:
            return 0
        else:
            if node.value > b:
                return self.output(node.left , a , b)
            elif(node.value < a):
                return self.output(node.right , a , b)
            else:
                c1 = self.countGreat(node.left , a)
                c2 = self.count_less_than(node.right , b)
                return 1 + c1 + c2
    
    
    
t = RedBlackTree()
k = int(raw_input())

for i in range(k):
    ls = list(raw_input().split())
    if(ls[0] == "+"):
        if(nlist[int(ls[1])] == 0):
            t.insert(int(ls[1]),t.root)
    else:
        a = int(ls[1])
        b = int(ls[2])
        if(a > b):
            print(0)
        elif(a == b):
            if(nlist[b] == 1):
                print(1)
            else:
                print(0)
        else:
            print(t.output(t.root , a , b))
