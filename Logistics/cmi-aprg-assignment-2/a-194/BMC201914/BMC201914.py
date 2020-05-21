class Node:
  def __init__(self,v,c,s):
    self.val=v
    self.col=c
    self.size=s
    self.lc=None
    self.rc=None
    self.p=None


class RedBlackTree:
  def __init__(self,r=None):
    self.root=r
  def sear(self,a):
    n=self.root
    while n.val != a:
      if n.val>a:
        n=n.lc
      elif n.val<a:
        n=n.rc
      if n.val==None:
        return False
    return True
  def ins(self,a):
    nn=Node(a,0,1)
    nn.lc=Node(None,1,0)
    nn.rc=Node(None,1,0)
    n=self.root
    if not self.root:
      self.root=nn
      return
    else:
      while n.lc.val != None or n.rc.val !=None:
        if n.val>a:
          if n.lc.val != None:
            n.size=n.size+1
            n=n.lc
          else:
            break
        else:
          if n.rc.val != None:
            n.size=n.size+1
            n=n.rc
          else:
            break
      if n.val>a:
        n.size=n.size+1
        n.lc=nn
      else:
        n.size=n.size+1
        n.rc=nn
      nn.p=n
  def lR(self,x):
    if self.root.val==x:
      b=self.root
      y=b.rc
      a=y.lc
      sx=b.size
      sy=y.size
      sb=b.lc.size
      sa=a.size
      self.root=y
      y.lc=b
      b.p=y
      b.rc=a
      a.p=b
      y.size=sx
      b.size=sa+sb+1
    else:
      n=self.root
      while n.val != x:
        if x>n.val:
          n=n.rc
        else:
          n=n.lc
      y=n.rc
      a=y.lc
      sx=n.size
      sy=y.size
      sb=n.lc.size
      sa=a.size
      y.p=n.p
      if y.p.val>y.val:
        y.p.lc=y
      else:
        y.p.rc=y
      y.lc=n
      n.p=y
      n.rc=a
      a.p=n
      y.size=sx
      n.size=sa+sb+1
  def rR(self,x):
    if self.root.val==x:
      b=self.root
      y=b.lc
      a=y.rc
      sx=b.size
      sy=y.size
      sb=b.rc.size
      sa=a.size
      self.root=y
      y.rc=b
      b.p=y
      b.lc=a
      a.p=b
      y.size=sx
      b.size=sa+sb+1
    else:
      n=self.root
      while n.val != x:
        if x>n.val:
          n=n.rc
        else:
          n=n.lc
      y=n.lc
      a=y.rc
      sx=n.size
      sy=y.size
      sb=n.rc.size
      sa=a.size
      y.p=n.p
      if y.p.val>y.val:
        y.p.lc=y
      else:
        y.p.rc=y
      y.rc=n
      n.p=y
      n.lc=a
      a.p=n
      y.size=sx
      n.size=sa+sb+1
  def fix(self,x):
    if self.root.val==x:
      self.root.col=1
    else:
      n=self.root
      while n.val != x:
        if n.val>x:
          n=n.lc
        else:
          n=n.rc
      if n.p.col!=1:
        par=n.p
        gp=par.p
        if gp.lc==par and gp.rc.col==0:
          gp.rc.col=1
          par.col=1
          gp.col=0
          self.fix(gp.val)
        elif gp.lc==par and gp.rc.col==1 and par.lc==n:
          par.col=1
          gp.col=0
          self.rR(gp.val)
        elif gp.lc==par and gp.rc.col==1 and par.rc==n:
          self.lR(par.val)
          self.fix(par.val)
        elif gp.rc==par and gp.lc.col==0:
          gp.lc.col=1
          par.col=1
          gp.col=0
          self.fix(gp.val)
        elif gp.rc==par and gp.lc.col==1 and par.rc==n:
          par.col=1
          gp.col=0
          self.lR(gp.val)
          #print(par.lc.val)
        elif gp.rc==par and gp.lc.col==1 and par.lc==n:
          self.rR(par.val)
          self.fix(par.val)
           
 
           
  def insert(self,a):
    if not self.root:
      self.ins(a)
      self.fix(a)
    elif self.root and self.sear(a)==False:
      self.ins(a)
      self.fix(a)
  def countLessThan(self,a):
    if self.root.val==a:
      return self.root.lc.size
    else:
      n=self.root
      t=0
      while n.val != a and n.val!=None:
        if n.val>a:
          n=n.lc
        else:
          t=t+n.lc.size+1
          n=n.rc
      if  n.val!=None:    
        return (t+n.lc.size)
      else:
        return t

def count_in_btw (x,a,b):
  return (x.countLessThan(b+1)-x.countLessThan(a))
  #return x.countLessThan(b+1)
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
    d.append(count_in_btw(a,int(i[1]),int(i[2])))
for i in d:
  print(i)
