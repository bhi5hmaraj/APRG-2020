

class Node:
    def __init__(self,initval = None):
        self.value = initval
        self.parent = None
        self.left = None
        self.right = None
        self.color = None
        self.size = 1
    def childcolor(self,str):
        if(str == "R"):
            if(self.right != None):
                return (self.right.color)
            else:
                return ("Black")
        else:
            if(self.left != None):
                return (self.left.color)
            else:
                return ("Black")
        
    def childsize(self,str):
        if(str == "R"):
            if(self.right != None):
                return (self.right.size)
            else:
                return (0)
        else:
            if(self.left != None):
                return (self.left.size)
            else:
                return (0)
    
    def childvalue(self,str):
        if(str == "R"):
            if(self.right != None):
                return (self.right.value)
            else:
                return ("*")
        else:
            if(self.left != None):
                return (self.left.value)
            else:
                return ("*")
        
class RedBlackTree:
    def __init__(self):
        self.root = Node()
        self.root.color = "Black"
    
            
    def rightrotate(self,Y):
        y = Y.size
        X = Y.left
        B = X.right
        b = X.childsize("R")
        A = X.left
        a = X.childsize("L")
        C = Y.right
        c = Y.childsize("R")
        D = Y.parent
        X.parent = Y.parent
        X.right = Y
        Y.parent = X
        Y.left = B
        if(B != None):
            B.parent = Y
        if (D != None):
            if(D.left == Y):
                D.left = X
            else:
                D.right = X
    
        else:
            self.root = X
        Y.size = 1 + Y.childsize("L") + Y.childsize("R")
        X.size = 1 + X.childsize("L") + Y.size
       
       
        
    def leftrotate(self,X):
        x = X.size
        Y = X.right
        B = Y.left
        b = Y.childsize("L")
        A = X.left
        a = X.childsize("R")
        C = Y.right
        c = Y.childsize("R")
        D = X.parent
        Y.parent = X.parent
        Y.left = X
        X.parent = Y
        X.right = B
        if(B != None):
            B.parent = X
        if(D != None):
            if(D.left == X):
                D.left = Y
            else:
                D.right = Y
            
        else:
            self.root = Y
        X.size = 1 + X.childsize("L") + X.childsize("R")
        Y.size = 1 + Y.childsize("R") + X.size
       
        
    def rebalance(self,N):
        if(N.parent == None):
            N.color = "Black"
        else:
            if(N.parent.parent != None):
                if(N.parent.color == "Red"):
                    if(N.parent.parent.left == N.parent):
                        if(N.parent.parent.childcolor("R") == "Red"):
                            N.parent.color = "Black"
                            N.parent.parent.right.color = "Black"
                            N.parent.parent.color = "Red"
                            self.rebalance(N.parent.parent)
                        else:
                            if(N.parent.right == N):
                                self.leftrotate(N.parent) 
                                self.rebalance(N.left)
                            else:
                                N.parent.color = "Black"
                                N.parent.parent.color = "Red"
                                self.rightrotate(N.parent.parent)
                    else:
                        if(N.parent.parent.childcolor("L") == "Red"):
                            N.parent.color = "Black"
                            N.parent.parent.left.color = "Black"
                            N.parent.parent.color = "Red"
                            self.rebalance(N.parent.parent)
                        else:
                            if(N.parent.left == N):
                                self.rightrotate(N.parent)
                                self.rebalance(N.right)
                            else:
                                N.parent.color = "Black"
                                N.parent.parent.color = "Red"
                                self.leftrotate(N.parent.parent)
                            
             

    def search(self, N, x):
        if (N == None or N.value == None): 
            return False
        elif (N.value == x): 
            return True
        elif (N.value < x): 
            return self.search(N.right,x)
        else:
            return self.search(N.left,x)
 
    def insertafternode(self,N,x):
        if(N.value == None):
            N.value = x
            N.size = 1
        if(N.value != x):
            X = Node(x)
            X.color = "Red"
            N.size = N.size + 1
            if(N.value < x):
                if(N.right == None):
                    N.right = X
                    X.parent = N
                    
                    self.rebalance(X)
                else:
                    self.insertafternode(N.right,x)
            else:
                if(N.left == None):
                    N.left = X
                    X.parent = N
                   
                    self.rebalance(X)
                else:
                    self.insertafternode(N.left,x)
        
                    
                
    def insert(self,x):
        if(self.search(self.root,x) == False): self.insertafternode(self.root,x)
        
    def count_less_than_after(self,N,x):
        if(N == None or N.value == None):
            return 0 
        else:
            if(N.value == x):
                return(N.childsize("L"))
            elif(N.value < x):
                return(1 + N.childsize("L") + self.count_less_than_after(N.right,x))
            else:
                return(self.count_less_than_after(N.left,x))
            
    def count_less_than(self,x):
        return (self.count_less_than_after(self.root,x))
           
    
    def f (self,l,u):
        return(self.count_less_than(u + 1) - self.count_less_than(l))
    

COUNT = [10]
def print2DUtil(root, space):
    if (root == None) :
        return
    space += COUNT[0]
    print2DUtil(root.right, space)
    print()  
    for i in range(COUNT[0], space):
        print(end = " ")  
    print(root.value,root.color,root.size)  
    print2DUtil(root.left, space)  
def print2D(root):
    print2DUtil(root, 0)

    

T = RedBlackTree()
Q = int(input())
for i in range(Q):
    S = input().split()
    L = [S[0]] + list(map(int,S[1:]))
    if(L[0] == "+"):
        T.insert(L[1])
    else:
        print(T.f(min(L[1:]),max(L[1:])))
"""T.insert(1)
T.insert(2)
T.insert(3)
T.insert(4)

print2D(T.root)
T.count_less_than(3)"""

        
