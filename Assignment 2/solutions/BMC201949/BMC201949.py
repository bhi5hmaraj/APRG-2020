from sys import stdin, stdout  
import sys
import time
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self,initval=None,size1=0,color1="black",l=None,r=None,p=None):
        self.left=l
        self.right=r
        self.parent=p
        self.val=initval
        self.size=size1
        self.color=color1
    def new_parent(self):
        if self.left!=None:
            self.left.parent=self
        if self.right!=None:
            self.right.parent=self    
        
    
            
    
class RedBlackTree:
    def __init__(self):
        self.root=None
    def isEmptyNode(self,N):
        if N.val==None:
            return True
        else:
            return False

    def isEmpty(self):
        if self.root==None:
            return True
        else:
            return False
            


    def get_size(self,node):
        if node==None: return 0
        return node.size

    def find(self,N,v):    
        if(N.val>v):
            if(N.left!=None):
                return self.find(N.left,v)
            else:
                return False
        elif(N.val<v):
            if(N.right==None):
                return False
            else:
                return self.find(N.right,v)
        else:    
            return True
    def left_rotate(self,Nd):
        if(Nd.right==None):
            return
        else:
            y=Nd
            Nd=Nd.right
            if self.root==y:
                self.root=Nd
            else:
                if y==y.parent.left:
                    y.parent.left=Nd
                else:
                    y.parent.right=Nd
                Nd.parent=y.parent  
            y.right=Nd.left
            Nd.left=y
            Nd.new_parent()
            y.new_parent() 
            Nd.size = y.size
            y.size = self.get_size(y.left)+self.get_size(y.right)+1

    def right_rotate(self,Nd):
         if(Nd.left==None):
            return
         else:
            y=Nd
            Nd=Nd.left
            if self.root==y:
                self.root=Nd
            else:
                if y==y.parent.right:
                    y.parent.right=Nd
                else:
                    y.parent.left=Nd
                Nd.parent=y.parent  
            
            y.left=Nd.right

            Nd.right=y
            Nd.new_parent()
            y.new_parent()
            Nd.size = y.size
            y.size = self.get_size(y.left)+self.get_size(y.right)+1
        
    def sibling(self,Nd):
        if(self.isEmpty()==None):
            return None
        else:
            if(Nd.parent==None):
                return None
            else:
                if(Nd.parent.left==Nd):
                    return Nd.parent.right
                else:
                    return Nd.parent.left
                
        
    def find_color(self,No):
        if(No==None):
            return "black"
        else:
            return No.color

        
    def insert(self,v):
        if(self.root==None):
            self.root=Node(v,1,"black")
        else:
            if(self.find(self.root,v)==False):
                self.insert1(self.root,v)
        
    def insert1(self,N,v):        
            if(N.val<v):
                if N.right!=None :
                    N.size=N.size+1
                    self.insert1(N.right,v)
                
                else:
                    y=Node(v,1,"red")
                    N.right=y
                    y.parent=N
                    N.size = N.size+1
                    if(N.color=="red"):
                        self.rebalance(y)

            if(N.val>v):
                if(N.left!=None):
                    N.size=N.size+1
                    self.insert1(N.left,v)
                else:
                    y=Node(v,1,"red")
                    N.left=y
                    y.parent=N
                    N.size = N.size+1
                    if(N.color=="red"):
                        self.rebalance(y)
                
    def rebalance(self,Nd):
        if Nd == self.root:
            Nd.color = "black"
            return
        if Nd == None: return
        if Nd.parent == Nd.parent.parent.left:
            if Nd.parent.parent.right != None and Nd.parent.parent.right.color == "red":
                Nd.parent.color = "black"
                Nd.parent.parent.right.color = "black"
                Nd.parent.parent.color = "red"
                if Nd.parent.parent == self.root or Nd.parent.parent.parent.color == "red":
                    self.rebalance(Nd.parent.parent)
                return
            else:
                if Nd == Nd.parent.right:
                    self.left_rotate(Nd.parent)
                    Nd.color = "black"
                    Nd.parent.color = "red"
                    self.right_rotate(Nd.parent)
                else:
                    Nd.parent.color = "black"
                    Nd.parent.parent.color = "red"
                    self.right_rotate(Nd.parent.parent)
                return
        else:
            if Nd.parent.parent.left != None and Nd.parent.parent.left.color == "red":
                Nd.parent.color = "black"
                Nd.parent.parent.left.color = "black"
                Nd.parent.parent.color = "red"
                if Nd.parent.parent == self.root or Nd.parent.parent.parent.color == "red":
                    self.rebalance(Nd.parent.parent)
                return
            else:
                if Nd == Nd.parent.left:
                    self.right_rotate(Nd.parent)
                    Nd.color = "black"
                    Nd.parent.color = "red"
                    self.left_rotate(Nd.parent)
                else:
                    Nd.parent.color = "black"
                    Nd.parent.parent.color = "red"
                    self.left_rotate(Nd.parent.parent)
                return
                
                

                
    def count_less_than_node(self,N,x):
        if(N==None):
            return 0
        else:
            if(N.val>x):
                if N.left == None:
                    return 0
                else:
                    return self.count_less_than_node(N.left,x)
            elif(N.val<x):
                if N.right != None:
                    p1=self.get_size(N.left)
                    p2=self.count_less_than_node(N.right,x)
                    return 1+p1+p2
                else:
                    p1=self.get_size(N.left)
                    return 1+p1
                
            else: return self.get_size(N.left)

    def count_less_than(self,x):
        if(self.root==None):
            return 0
        else:
             return self.count_less_than_node(self.root,x)    

st = time.time()
T=RedBlackTree()
#T.insert(0)
#print(T.count_less_than(2)-T.count_less_than(1))
#T.insert(2)
#print(T.count_less_than(4)-T.count_less_than(1))
#T.insert(4)
#print(T.count_less_than(6)-T.count_less_than(1))
#T.insert(6)
#print(T.count_less_than(8)-T.count_less_than(1))
#T.insert(8)
#print(T.count_less_than(9)-T.count_less_than(1))
#T.insert(10)
#print(T.count_less_than(11)-T.count_less_than(1))

#print(T.find(T.root,30))
#print(T.find(T.root,17))
#print(T.find(T.root,20))
"""c = []
for i in range(75000):
    T.insert(2*i)
    c.append(T.count_less_than(2*i+2) - T.count_less_than(1))
for i in c: print(str(i))
print(time.time()-st)"""
n=int(input())
lines=[]
i=1

for i in range(0,n):
    x=list(input().split())
    a=int(x[1])

    if x[0]=='+':
        T.insert(a) 
    else:
        b=int(x[2])
        
        if a>b:
            print(0)
        else:
            z=T.count_less_than(b+1)-T.count_less_than(a)
            print(z)
