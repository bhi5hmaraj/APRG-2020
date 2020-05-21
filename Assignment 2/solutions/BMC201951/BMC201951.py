class Node:
  def __init__(self,v,c,s):
    self.data=v
    self.colour=c
    self.size=s
    self.left=None
    self.right=None
    self.p=None


class RedBlackTree:
  def __init__(self,r=None):
    self.root=r
  def sear(self,a):
    n=self.root
    while n.data != a:
      if n.data>a:
        n=n.left
      elif n.data<a:
        n=n.right
      if n.data==None:
        return False
    return True
    
  def rR(self,x):
    if self.root.data==x:
      b=self.root
      y=b.left
      a=y.right
      sx=b.size
      sy=y.size
      sb=b.right.size
      sa=a.size
      self.root=y
      y.right=b
      b.p=y
      b.left=a
      a.p=b
      y.size=sx
      b.size=sa+sb+1
    else:
      n=self.root
      while n.data != x:
        if x>n.data:
          n=n.right
        else:
          n=n.left
      y=n.left
      a=y.right
      sx=n.size
      sy=y.size
      sb=n.right.size
      sa=a.size
      y.p=n.p
      if y.p.data>y.data:
        y.p.left=y
      else:
        y.p.right=y
      y.right=n
      n.p=y
      n.left=a
      a.p=n
      y.size=sx
      n.size=sa+sb+1
  
  def lR(self,x):
    if self.root.data==x:
      b=self.root
      y=b.right
      a=y.left
      sx=b.size
      sy=y.size
      sb=b.left.size
      sa=a.size
      self.root=y
      y.left=b
      b.p=y
      b.right=a
      a.p=b
      y.size=sx
      b.size=sa+sb+1
    else:
      n=self.root
      while n.data != x:
        if x>n.data:
          n=n.right
        else:
          n=n.left
      y=n.right
      a=y.left
      sx=n.size
      sy=y.size
      sb=n.left.size
      sa=a.size
      y.p=n.p
      if y.p.data>y.data:
        y.p.left=y
      else:
        y.p.right=y
      y.left=n
      n.p=y
      n.right=a
      a.p=n
      y.size=sx
      n.size=sa+sb+1
      
  def ins(self,a):
    nn=Node(a,0,1)
    nn.left=Node(None,1,0)
    nn.right=Node(None,1,0)
    n=self.root
    if not self.root:
      self.root=nn
      return
    else:
      while n.left.data != None or n.right.data !=None:
        if n.data>a:
          if n.left.data != None:
            n.size=n.size+1
            n=n.left
          else:
            break
        else:
          if n.right.data != None:
            n.size=n.size+1
            n=n.right
          else:
            break
      if n.data>a:
        n.size=n.size+1
        n.left=nn
      else:
        n.size=n.size+1
        n.right=nn
      nn.p=n
 
  def fix(self,x):
    if self.root.data==x:
      self.root.colour=1
    else:
      n=self.root
      while n.data != x:
        if n.data>x:
          n=n.left
        else:
          n=n.right
      if n.p.colour!=1:
        par=n.p
        gp=par.p
        if gp.left==par and gp.right.colour==0:
          gp.right.colour=1
          par.colour=1
          gp.colour=0
          self.fix(gp.data)
        elif gp.left==par and gp.right.colour==1 and par.left==n:
          par.colour=1
          gp.colour=0
          self.rR(gp.data)
        elif gp.left==par and gp.right.colour==1 and par.right==n:
          self.lR(par.data)
          self.fix(par.data)
        elif gp.right==par and gp.left.colour==0:
          gp.left.colour=1
          par.colour=1
          gp.colour=0
          self.fix(gp.data)
        elif gp.right==par and gp.left.colour==1 and par.right==n:
          par.colour=1
          gp.colour=0
          self.lR(gp.data)
          #print(par.left.data)
        elif gp.right==par and gp.left.colour==1 and par.left==n:
          self.rR(par.data)
          self.fix(par.data)
           
 
           
  def insert(self,a):
    if not self.root:
      self.ins(a)
      self.fix(a)
    elif self.root and self.sear(a)==False:
      self.ins(a)
      self.fix(a)
  def countLessThan(self,a):
    if self.root.data==a:
      return self.root.left.size
    else:
      n=self.root
      t=0
      while n.data != a and n.data!=None:
        if n.data>a:
          n=n.left
        else:
          t=t+n.left.size+1
          n=n.right
      if  n.data!=None:    
        return (t+n.left.size)
      else:
        return t

def messi (x,a,b):
  return (x.countLessThan(b+1)-x.countLessThan(a))
  return x.countLessThan(b+1)
n=int(input())
mat=[]
for i in range(n):
  mat.append(input().split())
a=RedBlackTree()
d=[]
b=1
for i in mat:
  if i[0]=='+':
    a.insert(int(i[1]))
    b=2
  elif i[0]=='?' and b==1:
    d.append(0)
  else:
    d.append(messi(a,int(i[1]),int(i[2])))
for i in d:
  print(i)
