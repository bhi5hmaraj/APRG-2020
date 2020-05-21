class Node:
  def __init__(self,val,c):
    self.val=val
    self.p=None
    self.lc=None
    self.rc=None
    self.size=1
    self.color=c

class RBT:
  def __init__(self,r=None):
    self.root=r
  def elem(self,x,a):
    if x==None:
      return False
    elif x.val==a:
      return True
    elif a<x.val:
      if x.lc.size==0:
        return False
      else:
        return self.elem(x.lc,a)   
    else:
      if x.rc.size==0:
        return False
      else:
        return self.elem(x.rc,a)             
  def insert(self,x):
    b=Node(x,1)
    c1=Node(None,0)
    c2=Node(None,0)
    b.lc=c1
    b.rc=c2
    c1.size=0
    c2.size=0
    r=self.root
    if self.elem(self.root,x)==True:
      return self
    else:  
      if  self.root == None:
        self.root=b
        self.root.color=0
        return
      else:
        while r.lc != None and r.rc != None:
          if r.val>x:
            if r.lc != None and r.lc.size>0:
              r.size += 1
              r=r.lc
            else:
              break
          else:
            if r.rc != None and r.rc.size>0:
              r.size += 1
              r=r.rc
            else:
              break
        if r.val>x:
          r.lc=b
        else:
          r.rc=b
        b.p=r
        r.size += 1
    return self.fixrbp(x)  
  def lRotate(self,x):
    if x==self.root:
      y=x.rc
      z=y.lc
      x.size =x.size- (y.rc.size+1)
      self.root=y
      y.p=None
      y.lc=x
      x.p=y
      x.rc=z
      z.p=x
      y.size = y.lc.size+1+y.rc.size
    else:
      y=x.rc
      z=y.lc
      w=x.p
      if w.rc==x:
        x.size -= (y.rc.size+1)
        w.rc=y
        y.p=w
        y.lc=x
        x.p=y
        x.rc=z
        z.p=x
      else:
        x.size -= (y.rc.size+1)
        w.lc=y
        y.p=w
        y.lc=x
        x.p=y
        x.rc=z
        z.p=x  
      y.size = y.lc.size+1+y.rc.size
  def rRotate(self,x):
    if x==self.root:
      y=x.lc
      z=y.rc
      y.size=x.size
      x.size -= (y.lc.size+1)
      self.root=y
      y.p=None
      y.rc=x
      x.p=y
      x.lc=z
      z.p=x
    else:
      y=x.lc
      z=y.rc
      w=x.p
      if w.rc==x:
        x.size -= (y.lc.size+1)
        w.rc=y
        y.p=w
        y.rc=x
        x.p=y
        x.lc=z
        z.p=x
      else:
        x.size -= (y.lc.size+1)
        w.lc=y
        y.p=w
        y.rc=x
        x.p=y
        x.lc=z
        z.p=x
      y.size = y.lc.size+1+y.rc.size      
  def fixrbp(self,x):
    b=self.search(self.root,x)  
    if self.root.val==x:
      self.root.color=0
      return
    elif b.p.color==0:
      return
    elif b.p.color==1 :
      gp=b.p.p
      par=b.p
      if gp.lc==par:
        unc=gp.rc
      else:
        unc=gp.lc
      if unc.color==1:
        par.color=0
        unc.color=0
        gp.color=1
        return self.fixrbp(gp.val)
      else:
        if par.lc==b:
          if unc==gp.rc:
            par.color=0
            gp.color=1
            self.rRotate(gp)
            return
          else: 
            self.rRotate(par)
            return self.fixrbp(par.val)  
        else:
          if unc==gp.rc:
            self.lRotate(par)
            return self.fixrbp(par.val)
          else:
            gp.color=1
            par.color=0
            self.lRotate(gp)
            return 
  def search(self,r,x):
    if r.val==x:
      b=r
      return b
    else:
      if x<r.val:
        r=r.lc
        return self.search(r,x)
      else:
        r=r.rc
        return self.search(r,x)          
  def countlessthan(self,a):
    if self.root==None:
        return 0
    elif self.root.val==a:
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
p=int(input())
a=[]
b=[]
for i in range (p):
  a.append(input().split())
x=RBT()
for i in range(p):
  if a[i][0]=='+':
    x.insert(int(a[i][1]))
  elif a[i][0]=='?':
    c=(x.countlessthan(int(a[i][2]))-x.countlessthan(int(a[i][1])))
    if x.elem(x.root,int(a[i][2]))==True:
      b.append(c+1)
    else:
      b.append(c)  
for i in range(len(b)):
  print (b[i])
print()

