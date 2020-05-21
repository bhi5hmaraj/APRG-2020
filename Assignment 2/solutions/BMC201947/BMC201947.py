class Node:
    def __init__(self,v,c,s):
        self.leftc=None
        self.rightc=None
        self.p=None
        self.val=v
        self.col=c
        self.size=s

class RedBlackTree:
    def __init__(self,r=None):
        self.root=r
    def sear(self,a):
        n=self.root
        while n.val != a:
            if n.val==None:
                return False
            if (n.val>a):
                n=n.leftc
            elif (n.val<a):
                n=n.rightc
        return True
    def left_rotate(self,x):
        if self.root.val==x:
            b=self.root
            y=b.rightc
            a=y.leftc
            sx=b.size
            sy=y.size
            sb=b.leftc.size
            sa=a.size
            self.root=y
            y.leftc=b
            b.p=y
            b.rightc=a
            a.p=b
            y.size=sx
            b.size=sa+sb+1
        else:
            n=self.root
            while n.val != x:
                if x>n.val:
                    n=n.rightc
                else:
                    n=n.leftc
            y=n.rightc
            a=y.leftc
            sx=n.size
            sy=y.size
            sb=n.leftc.size
            sa=a.size
            y.p=n.p
            if y.p.val>y.val:
                y.p.leftc=y
            else:
                y.p.rightc=y
            y.leftc=n
            n.p=y
            n.rightc=a
            a.p=n
            y.size=sx
            n.size=sa+sb+1
    def right_rotate(self,x):
        if self.root.val==x:
            b=self.root
            y=b.leftc
            a=y.rightc
            sx=b.size
            sy=y.size
            sb=b.rightc.size
            sa=a.size
            self.root=y
            y.rightc=b
            b.p=y
            b.leftc=a
            a.p=b
            y.size=sx
            b.size=sa+sb+1
        else:
            n=self.root
            while n.val != x:
                if x>n.val:
                    n=n.rightc
                else:
                    n=n.leftc
            y=n.leftc
            a=y.rightc
            sx=n.size
            sy=y.size
            sb=n.rightc.size
            sa=a.size
            y.p=n.p
            if y.p.val>y.val:
                y.p.leftc=y
            else:
                y.p.rightc=y
            y.rightc=n
            n.p=y
            n.leftc=a
            a.p=n
            y.size=sx
            n.size=sa+sb+1
    def ins(self,a):
        nn=Node(a,0,1)
        nn.leftc=Node(None,1,0)
        nn.rightc=Node(None,1,0)
        n=self.root
        if not self.root:
            self.root=nn
            return
        else:
            while n.leftc.val != None or n.rightc.val !=None:
                if n.val<a:
                    if n.rightc.val != None:
                        n.size=n.size+1
                        n=n.rightc
                    else:
                        break
                else:
                    if n.leftc.val != None:
                        n.size=n.size+1
                        n=n.leftc
                    else:
                        break
            if n.val<a:
                n.size=n.size+1
                n.rightc=nn
            else:
                n.size=n.size+1
                n.leftc=nn
            nn.p=n
    def rebalance(self,x):
        if self.root.val==x:
            self.root.col=1
        else:   
            n=self.root
            while n.val != x:
                if n.val>x:
                    n=n.leftc
                else:
                    n=n.rightc
            if n.p.col!=1:
                par=n.p
                gp=par.p
                if gp.leftc==par and gp.rightc.col==0:
                    gp.rightc.col=1
                    par.col=1
                    gp.col=0
                    self.rebalance(gp.val)
                elif gp.rightc==par and gp.leftc.col==1 and par.rightc==n:
                    par.col=1
                    gp.col=0  
                    self.left_rotate(gp.val)
                elif gp.rightc==par and gp.leftc.col==1 and par.leftc==n:
                    self.right_rotate(par.val)
                    self.rebalance(par.val)
                elif gp.rightc==par and gp.leftc.col==0:
                    gp.leftc.col=1
                    par.col=1
                    gp.col=0
                    self.rebalance(gp.val)
                elif gp.leftc==par and gp.rightc.col==1 and par.leftc==n:
                    par.col=1
                    gp.col=0
                    self.right_rotate(gp.val)
                elif gp.leftc==par and gp.rightc.col==1 and par.rightc==n:
                    self.left_rotate(par.val)
                    self.rebalance(par.val)
    def insert(self,a):
        if not self.root:
            self.ins(a)
            self.rebalance(a)
        elif self.root and self.sear(a)==False:
            self.ins(a)
            self.rebalance(a)
    def count_less_than(self,a):
        if self.root.val==a:
            return self.root.leftc.size
        else:
            n=self.root
            const=0
            while n.val != a and n.val!=None:
                if n.val>a:
                    n=n.leftc
                else:
                    const=const+n.leftc.size+1
                    n=n.rightc
            if  n.val!=None:    
                return (const+n.leftc.size)
            else:
                return const

n=int(input())
list1=[]
for i in range(n):
  list1.append(input().split())

list2=[]
b=1
a=RedBlackTree()

for i in list1:
  if i[0]=='+':
    a.insert(int(i[1]))
    b=2
  elif i[0]=='?' and b==2:
    list2.append(a.count_less_than(int(i[2])+1)-a.count_less_than(int(i[1])))
  else:
    list2.append(0)
    
for i in list2:
  print(i)


