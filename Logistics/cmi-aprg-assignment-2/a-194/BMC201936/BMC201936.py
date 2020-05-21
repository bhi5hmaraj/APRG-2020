
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
    
    def assignsize(self,N):
        if(N != None):
            if(N.left != None):
                self.assignsize(N.left)
            if(N.right != None):
                self.assignsize(N.right)
            N.size = 1 + N.childsize("L") + N.childsize("R")
            
    def rightrotate(self,Y):
        
        X = Y.left
        B = X.right
       
        A = X.left
       
        C = Y.right
        
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
       
        
    def leftrotate(self,X):
       
        Y = X.right
        B = Y.left
        
        A = X.left
        
        C = Y.right
        
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
                            
             
    def insertafternode(self,N,x):
        if(N.value == None):
            N.value = x
        if(N.value != x):
            X = Node(x)
            X.color = "Red"
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
        self.assignsize(self.root)
                    
                
    def insert(self,x):
        self.insertafternode(self.root,x)
        
    def count_less_than_after(self,N,x):
        if(N == None or N.value == None):
            return 0 
        else:
            if(N.value == x):
                return (N.left.size)
            elif(N.value > x):
                return (self.count_less_than_after(N.left,x))
            else:
                return (1 + N.left.size + self.count_less_than_after(N.right,x))
    def count_less_than(self,x):
        return (self.count_less_than_after(self.root,x))
    
    def f (self,N,l,u):
        if(N == None or N.value == None):
            return 0
        else:
            if(N.value < l):
                return (self.f(N.right,l,u))
            elif(N.value == l):
                return (1 + (self.f(N.right,l,u)))
            elif(N.value > l and N.value < u):
                return (1 + (self.f(N.left,l,u))+(self.f(N.right,l,u)))
            elif(N.value == u):
                return (1 + (self.f(N.left,l,u)))
            else:
                return (self.f(N.left,l,u))
    
    def g(self,l,u):
        return (self.f(self.root,l,u))
    

n=int(input())
l=[]
s=[]
for i in range(n):
    l.append(list(input().split()))
i=0
while i<n:
    c=0
    while i<n and l[i][0]=='+':
        k=int(l[i][1])
        if k not in s:
            s=s+[k]
        i+=1
    if i<n:
        for j in s:
            if j>=int(l[i][1]) and j<=int(l[i][2]):
                c=c+1
        print(c)
    i=i+1
