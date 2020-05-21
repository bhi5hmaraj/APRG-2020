
class Node:
  def __init__(self,value=0,c=0):
    self.val=value
    self.col=c
    self.lc=None
    self.rc=None
    self.p=None
    self.size=0


class RBtree:
  def __init__(self,root=None):
    self.root=root
  def search(self,r,x):
    if  self.root==None:
      return False
    elif  r==None:
      return False
    elif r.val==None:
      return False
    elif x==r.val:
      return True
    elif r.val>x:
      return self.search(r.lc,x)
    else:
      return self.search(r.rc,x)
  def ins(self,a):
    nn=Node(a,0)
    nn.lc=Node(None,1)
    nn.rc=Node(None,1)
    nn.size=1
    y=Node(None,1)
    n=self.root
    if n==None:
      self.root=nn
      #self.root.colour=1
      return
    else:
      while n.lc.val !=None or n.rc.val!=None:
        if n.val>a:
          if n.lc.val!=None:
            n.size+=1
            n=n.lc
            
          else:
            break
        else:
          if n.rc.val!=None:
            n.size+=1
            n=n.rc
            
          else:
            break
      
      if n.val>a:
        n.lc=nn
      else:
        n.rc=nn
      n.size += 1  
      nn.p=n                     #black=1

  def leftrotate(self,x):

     if x==self.root:
       if x.rc.lc!= None:
        y=x.rc
        sx=x.size
        sy=y.size
        sa=x.lc.size
        sb=y.lc.size
        sc=y.rc.size
        self.root = y
        y.p = None
        b = y.lc
        y.lc=x
        x.p = y
        x.rc=b
        b.p = x
        y.size=sx
        x.size=sa+sb+1
       else:
         y=x.rc
         sx=x.size
         sy=y.size
         sa=x.lc.size
         #sc=y.rc.size
         self.root=y
         y.p=None
         y.lc=x
         x.p=y
         y.size=x
         x.size=sa+1
     else:
       y=x.rc
       gc=y.lc
       sx=x.size
       sy=y.size
       sa=y.lc.size
       sb=y.rc.size
       sc=x.lc.size
       y.lc=x
       y.p=x.p
       if x.p.rc==x:
         y.p.rc=y
       else:
         y.p.lc=y
       x.p=y
       x.rc=gc
       gc.p=x
       y.size=sx
       x.size=sc+sa+1

  def rightrotate(self,x):
     if x==self.root:
      if x.lc.rc!=None:
        y=x.lc
        sx=x.size
        sy=y.size
        sa=y.rc.size
        sb=y.lc.size
        sc=x.rc.size
        a=y.rc
        self.root=y
        y.p=None
        y.rc=x
        x.p=y
        x.lc=a
        a.p=x
        y.size=sx
        x.size=sa+sc+1
      else:
        y=x.lc
        sx=x.size
        sy=y.size
        sb=y.lc.size
        sc=x.rc.size
        self.root=y
        y.p=None
        y.rc=x
        x.p=y
        x.lc=None
        y.size=sx
        x.size=sc+1
     else:
      if x.lc.rc!=None:
       if x.lc.rc!=None:
        y=x.lc
        sx=x.size
        sy=y.size
        sa=y.rc.size
#        sb=y.lc.size
        sc=x.rc.size
        a=y.rc
        w=x.p
        if x==w.rc:
          w.rc=y
        else:
          w.lc=y   
        y.p=w
        y.rc=x
        x.p=y
        x.lc=a
        a.p=x
        y.size=sx
        x.size=sa+sc+1
       else:
        y=x.lc
        sx=x.size
        sy=y.size
   #     sb=y.lc.size
        sc=x.rc.size
        w=x.p
        if x==w.rc:
          w.rc=y
        else:
          w.lc=y  
        y.p=w
        y.rc=x
        x.p=y
        x.lc=None
        y.size=sx
        x.size=sc+1
  def searchnode(self,r,x):
    if r==None:
      return r
    elif r.val==x:
      return r
    elif r.val>x:
       return self.searchnode(r.lc,x)
    else:
       return self.searchnode(r.rc,x)
  def fixredblackproperty(self,x):         #red=0                     #black=1
    b=self.searchnode(self.root,x)
    if b==self.root:
      self.root.col=1
      return
    elif b.p.col==1:
      return
    else:  
      if b.p==b.p.p.rc:
        u=b.p.p.lc
      else:
        u=b.p.p.rc
      if u.col==0:
        b.p.col=1
        u.col=1
        gp=b.p.p
        gp.col=0
        return self.fixredblackproperty(gp.val)
      else:
        if b==b.p.lc and b.p.p.rc==u:
          b.p.col=1
          b.p.p.col=0
          self.rightrotate(b.p.p)
          return
        elif b.p.rc==b and b.p.p.lc==u:
          b.p.col=1
          b.p.p.col=0
          self.leftrotate(b.p.p)
          return
        elif u==b.p.p.rc and b==b.p.rc:
          self.leftrotate(b.p)
          return self.fixredblackproperty(b.p.val)
        else:  
          self.rightrotate(b.p)
          return self.fixredblackproperty(b.p.val)
  def insert(self,x):
    if self.search(self.root,x)==True:
     return
    else:
      self.ins(x)
      self.fixredblackproperty(x)
  def countlessthan(self,x):
      n=self.root
      count=0
      while n.val !=x and n.val!=None:
        if n.val>x:
          n=n.lc
        else:
          count+=(n.lc.size+1)
          n=n.rc 
      if n.val==x:
        count+=(n.lc.size)
        return count
      else:
        return count
def count_in_between(tree,a,b):
  return (tree.countlessthan(1+b)-tree.countlessthan(a))

tree=RBtree()
n=int(input())
matrix=[]
flag=1
for i in range(n):
  a=(input().split())
  
  if a[0]=="+":
    tree.insert(int(a[1]))
    flag=2
  elif a[0]=="?" and flag==2:
    print(count_in_between(tree,int(a[1]),int(a[2])))
  else:
    print(0)

