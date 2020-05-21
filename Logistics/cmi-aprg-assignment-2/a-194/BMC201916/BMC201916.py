class Node:
    def __init__(self, value):
        self.value = value 
        self.parent = None 
        self.left = None 
        self.right = None
        self.color = None
        self.size = 1
        
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
        self.TNULL = Node(0)
        self.TNULL.color = "Black"
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL
    
            
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
                            
             

    def __search_tree_helper(self, node, key):
        if node == None:
            return 0
        elif key == node.value:
            return 1
        elif key < node.value:
            return self.__search_tree_helper(node.left, key)
        else:
            return self.__search_tree_helper(node.right, key)

    def __rb_transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent
        
        
    def __pre_order_helper(self, node):
        if node != TNULL:
            sys.stdout.write(node.value + " ")
            self.__pre_order_helper(node.left)
            self.__pre_order_helper(node.right)

    def __in_order_helper(self, node):
        if node != TNULL:
            self.__in_order_helper(node.left)
            sys.stdout.write(node.value + " ")
            self.__in_order_helper(node.right)

    def __post_order_helper(self, node):
        if node != TNULL:
            self.__post_order_helper(node.left)
            self.__post_order_helper(node.right)
            sys.stdout.write(node.value + " ")

    
    def search(self, k):
        return self.__search_tree_helper(self.root, k)
 
    def i(self,N,x):
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
                    self.i(N.right,x)
            else:
                if(N.left == None):
                    N.left = X
                    X.parent = N
                   
                    self.rebalance(X)
                else:
                    self.i(N.left,x)         
                
    def insert(self,x):
        if(self.__search_tree_helper(self.root,x) == False): self.i(self.root,x)
        
    def count(self,N,x):
        if(N == None or N.value == None):
            return 0 
        else:
            if(N.value == x):
                return(N.childsize("L"))
            elif(N.value < x):
                return(1 + N.childsize("L") + self.count(N.right,x))
            else:
                return(self.count(N.left,x))
            
    def count_less_than(self,x):
        return (self.count(self.root,x))
           
    
    def final (self,l,u):
        return(self.count_less_than(u + 1) - self.count_less_than(l))    

bst = RedBlackTree()
n = int(input())
for i in range(n):
    S = input().split()
    L = [S[0]] + list(map(int,S[1:]))
    if(L[0] == "+"):
        bst.insert(L[1])
    else:
        print(bst.final(min(L[1:]),max(L[1:])))       
