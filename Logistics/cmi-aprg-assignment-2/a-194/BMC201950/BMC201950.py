class Node:
    def __init__(self,v,c,s):
        self.left=None
        self.right=None
        self.parent=None
        self.value=v
        self.colour=c
        self.size=s

class RedBlackTree:
    def __init__(self,r=None):
        self.root=r
        
    def fix(self,x):
        y=self.root
        while (y.value != x):
            if y.value==None:
                return False
            
            if (y.value<x):
                y=y.right
            elif (y.value>x):
                y=y.left
                
        return True
    
    
    def LeftRotate(self,x):
        if(self.root.value!=x):
            y=self.root
            while y.value != x:
                if x>y.value:
                    y=y.right
                else:
                    y=y.left
            z=y.right
            w=z.left
            size1=y.size
            size2=y.left.size
            size3=w.size
            z.parent=y.parent
            if z.parent.value>z.value:
                z.parent.left=z
            else:
                z.parent.right=z
            z.left=y
            y.parent=z
            y.right=w
            w.parent=y
            z.size=size1
            y.size=size2+size3+1
        else :
            y=self.root
            z=y.right
            w=z.left
            size1=y.size
            size2=y.left.size
            size3=w.size
            self.root=z
            z.left=y
            y.parent=z
            y.right=w
            w.parent=y
            z.size=size1
            y.size=size2+size3+1
        
                
    def RightRotate(self,x):
        if self.root.value==x:
            y=self.root
            z=y.left
            w=z.right
            size1=y.size
            size2=z.size
            size3=y.right.size
            size4=w.size
            self.root=z
            z.right=y
            y.parent=z
            y.left=w
            w.parent=y
            z.size=size1
            y.size=size3+size4+1
        else:
            y=self.root
            while y.value != x:
                if x>y.value:
                    y=y.right
                else:
                    y=y.left
            z=y.left
            w=z.right
            size1=y.size
            size2=z.size
            size3=y.right.size
            size4=w.size
            z.parent=y.parent
            if z.parent.value>z.value:
                z.parent.left=z
            else:
                z.parent.right=z
            z.right=y
            y.parent=z
            y.left=w
            w.parent=y
            z.size=size1
            y.size=size3+size4+1

    def insert(self,x):
        z=Node(x,0,1)
        z.left=Node(None,1,0)
        z.right=Node(None,1,0)
        y=self.root
        if not self.root:
            self.root=z
            return
        else:
            while y.left.value != None or y.right.value !=None:
                if y.value<x:
                    if y.right.value != None:
                        y.size=y.size+1
                        y=y.right
                    else:
                        break
                else:
                    if y.left.value != None:
                        y.size=y.size+1
                        y=y.left
                    else:
                        break
            if y.value<x:
                y.size=y.size+1
                y.right=z
            else:
                y.size=y.size+1
                y.left=z
            z.parent=y
            
            
    def Rebalance(self,x):
        if self.root.value==x:
            self.root.colour=1
        else:   
            y=self.root
            while y.value != x:
                if y.value>x:
                    y=y.left
                else:
                    y=y.right
            if (y.parent.colour==0):
                p=y.parent
                g=p.parent
                if g.left==p and g.right.colour==0:
                    g.right.colour=1
                    p.colour=1
                    g.colour=0
                    self.Rebalance(g.value)
                elif g.right==p and g.left.colour==1 and p.right==y:
                    p.colour=1
                    g.colour=0  
                    self.LeftRotate(g.value)
                elif g.right==p and g.left.colour==1 and p.left==y:
                    self.RightRotate(p.value)
                    self.Rebalance(p.value)
                elif g.right==p and g.left.colour==0:
                    g.left.colour=1
                    p.colour=1
                    g.colour=0
                    self.Rebalance(g.value)
                elif g.left==p and g.right.colour==1 and p.left==y:
                    p.colour=1
                    g.colour=0
                    self.RightRotate(g.value)
                elif g.left==p and g.right.colour==1 and p.right==y:
                    self.LeftRotate(p.value)
                    self.Rebalance(p.value)
                    
    def insert2(self,x):
        if not self.root:
            self.insert(x)
            self.Rebalance(x)
        elif self.root and self.fix(x)==False:
            self.insert(x)
            self.Rebalance(x)
            
    def calcu(self,x):
        
        if(self.root.value!=x):
            y=self.root
            counter=0
            while y.value != x and y.value!=None:
                if y.value>x:
                    y=y.left
                else:
                    counter+=y.left.size+1
                    y=y.right
            if  y.value!=None:    
                return (counter+y.left.size)
            else:
                return counter
        else: 
            return self.root.left.size

n=int(input())
listshreyam=[]
for j in range(n):
  listshreyam.append(input().split())

listshreyam2=[]
b=1
x=RedBlackTree()

for j in listshreyam:
  if j[0]=='+':
    x.insert2(int(j[1]))
    b=2
  elif j[0]=='?' and b==2:
    listshreyam2.append(x.calcu(int(j[2])+1)-x.calcu(int(j[1])))
  else:
    listshreyam2.append(0)
    
for j in listshreyam2:
  print(j)



 

        
                
    

        
