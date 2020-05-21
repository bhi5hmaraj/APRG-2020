# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 00:09:36 2020

@author: kaneki
"""

class Node:
    def __init__(self,val,col,s):
        self.value=val
        self.color=col
        self.size=s
        self.left=None
        self.right=None
        self.parent=None


class RedBlackTree:
    def __init__(self,r=None):
        self.root=r
        
    def search(self,a):
        n=self.root
        while n.value != a:
            if n.value>a:
                n=n.left
            elif n.value<a:
                n=n.right
            if n.value==None:
                return False
        return True
    
    def insertnode(self,a):
        nn=Node(a,0,1)
        nn.left=Node(None,1,0)
        nn.right=Node(None,1,0)
        n=self.root
        if not self.root:
            self.root=nn
            return
        else:
            while n.left.value != None or n.right.value !=None:
                if n.value>a:
                    if n.left.value != None:
                        n.size=n.size+1
                        n=n.left
                    else:
                        break
                else:
                    if n.right.value != None:
                        n.size=n.size+1
                        n=n.right
                    else:
                        break
            if n.value>a:
                n.size=n.size+1
                n.left=nn
            else:
                n.size=n.size+1
                n.right=nn
            nn.parent=n


    def rebalance(self,x):
        if self.root.value==x:
            self.root.color=1
        else:
            n=self.root
            while n.value != x:
                if n.value>x:
                    n=n.left
                else:
                    n=n.right
            if n.parent.color!=1:
                parent=n.parent
                grand=parent.parent
                if grand.left==parent and grand.right.color==0:
                    grand.right.color=1
                    parent.color=1
                    grand.color=0
                    self.rebalance(grand.value)
                elif grand.left==parent and grand.right.color==1 and parent.left==n:
                    parent.color=1
                    grand.color=0
                    self.right_rotate(grand.value)
                elif grand.left==parent and grand.right.color==1 and parent.right==n:
                    self.left_rotate(parent.value)
                    self.rebalance(parent.value)
                elif grand.right==parent and grand.left.color==0:
                    grand.left.color=1
                    parent.color=1
                    grand.color=0
                    self.rebalance(grand.value)
                elif grand.right==parent and grand.left.color==1 and parent.right==n:
                    parent.color=1
                    grand.color=0
                    self.left_rotate(grand.value)
                elif grand.right==parent and grand.left.color==1 and parent.left==n:
                    self.right_rotate(parent.value)
                    self.rebalance(parent.value)
                
                
    def left_rotate(self,x):
        if self.root.value==x:
            b=self.root
            y=b.right
            a=y.left
            sx=b.size
            sy=y.size
            sb=b.left.size
            sa=a.size
            self.root=y
            y.left=b
            b.parent=y
            b.right=a
            a.parent=b
            y.size=sx
            b.size=sa+sb+1
        else:
            n=self.root
            while n.value != x:
                if x>n.value:
                    n=n.right
                else:
                    n=n.left
            y=n.right
            a=y.left
            sx=n.size
            sy=y.size
            sb=n.left.size
            sa=a.size
            y.parent=n.parent
            if y.parent.value>y.value:
                y.parent.left=y
            else:
                y.parent.right=y
            y.left=n
            n.parent=y
            n.right=a
            a.parent=n
            y.size=sx
            n.size=sa+sb+1
            
    def right_rotate(self,x):
        if self.root.value==x:
            b=self.root
            y=b.left
            a=y.right
            sx=b.size
            sy=y.size
            sb=b.right.size
            sa=a.size
            self.root=y
            y.right=b
            b.parent=y
            b.left=a
            a.parent=b
            y.size=sx
            b.size=sa+sb+1
        else:
            n=self.root
            while n.value != x:
                if x>n.value:
                    n=n.right
                else:
                    n=n.left
            y=n.left
            a=y.right
            sx=n.size
            sy=y.size
            sb=n.right.size
            sa=a.size
            y.parent=n.parent
            if y.parent.value>y.value:
                y.parent.left=y
            else:
                y.parent.right=y
            y.right=n
            n.parent=y
            n.left=a
            a.parent=n
            y.size=sx
            n.size=sa+sb+1

            
    def insert(self,a):
        if not self.root:
            self.insertnode(a)
            self.rebalance(a)
        elif self.root and self.search(a)==False:
            self.insertnode(a)
            self.rebalance(a)
            
    def count_less_than(self,a):
        if self.root.value==a:
            return self.root.left.size
        else:
            n=self.root
            t=0
            while n.value != a and n.value!=None:
                if n.value>a:
                    n=n.left
                else:
                    t=t+n.left.size+1
                    n=n.right
            if  n.value!=None:    
                return (t+n.left.size)
            else:
                return t
            
def count_between (tree,a,b):
    return (tree.count_less_than( b+1)- tree.count_less_than(a))
 


tree = RedBlackTree()
    
n =  int(input())
for i in range(n):
    s = input().split()
    if len(s) == 2:
        y = int(s[1])
        tree.insert(y)
      
    else:
        y = int(s[1])
        x = int(s[2])
        print(count_between(tree,y, x))
        
        
