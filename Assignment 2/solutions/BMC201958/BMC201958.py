class Color:
    black = 0
    red = 1

class Node:
    def __init__(self,info=None,color=None):
        self.info = info
        self.color = color
        self.l = None
        self.r = None
        self.p = None
        self.size = 1

class RedBlackTree:
    def __init__(self):
        self.ext = Node(-1,Color.black)
        self.ext.size=0
        self.root = self.ext

    def insert(self,val):
        temp = Node()
        ptr = self.root
        par = self.ext
        while ptr != self.ext:
            par = ptr
            if ptr.info > val:
                ptr = ptr.l
            elif ptr.info < val:
                ptr = ptr.r
            else: return
        temp.info = val
        temp.l = self.ext
        temp.r = self.ext
        temp.color = Color.red
        temp.p = par
        if par == self.ext:
            self.root = temp
        elif temp.info < par.info:
            par.l = temp
        else:
            par.r = temp
        if temp.p == self.ext:
            temp.color = Color.black
            return
        if temp.p.p == self.ext: return
        x=temp.p
        while x != self.ext:
            x.size=x.size+1
            x=x.p
        if temp!=self.root and temp.p!=self.root: self.rebalance(temp)

    def rebalance(self,ptr):
        while ptr.p.color == Color.red and ptr.p != self.ext:
            par = ptr.p
            gPar = par.p
            if par == gPar.l:
                unc = gPar.r
                if unc!=self.ext and unc.color == Color.red:
                    par.color = Color.black
                    unc.color = Color.black
                    gPar.color = Color.red
                    ptr = gPar
                else:
                    if ptr == par.r:
                        self.left_rotate(par)
                        ptr = par
                        par.p.color = Color.black
                        gPar.color = Color.red
                        self.right_rotate(gPar)
                    else:
                        par.color = Color.black
                        gPar.color = Color.red
                        self.right_rotate(gPar)

            else:
                unc = gPar.l
                if unc!=self.ext and unc.color == Color.red:
                    par.color = Color.black
                    unc.color = Color.black
                    gPar.color = Color.red
                    ptr = gPar
                else:
                    if ptr == par.l:
                        self.right_rotate(par)
                        ptr = par
                        par.p.color = Color.black
                        gPar.color = Color.red
                        self.left_rotate(gPar)
                    else:
                        par.color = Color.black
                        gPar.color = Color.red
                        self.left_rotate(gPar)
            if ptr == self.root: break
        self.root.color = Color.black
        
    def left_rotate(self,ptr):
        rptr = ptr.r 
        a = ptr.l.size
        b = rptr.l.size
        c = rptr.r.size
        ptr.r = rptr.l
        if rptr.l!=self.ext:
            rptr.l.p = ptr
        rptr.p = ptr.p
        if ptr.p == self.ext:
            self.root = rptr
        elif ptr == ptr.p.l:
            ptr.p.l = rptr
        else:
            ptr.p.r = rptr
        rptr.l = ptr
        ptr.p = rptr
        ptr.size = a+b+1
        rptr.size = a+b+c+2

    def right_rotate(self,ptr):
        lptr = ptr.l 
        a = lptr.l.size
        b = lptr.r.size
        c = ptr.r.size
        ptr.l = lptr.r
        if lptr.r!=self.ext:
            lptr.r.p = ptr
        lptr.p = ptr.p
        if ptr.p == self.ext:
            self.root = lptr
        elif ptr == ptr.p.r:
            ptr.p.r = lptr
        else:
            ptr.p.l = lptr
        lptr.r = ptr
        ptr.p = lptr
        ptr.size = b+c+1
        lptr.size = a+b+c+2
    def count_less_than(self,val):
        ptr = self.root
        y=0
        while ptr != self.ext:
            if ptr.info < val:
                y += 1+ptr.l.size
                ptr=ptr.r
            elif ptr.info > val:
                ptr = ptr.l
            else: 
                y += ptr.l.size
                break
        return y
rbt = RedBlackTree()
n = int(input())
for i in range(n):
    l = (input().split())
    if l[0] == '+':
        rbt.insert(int(l[1]))
    else:
        print(rbt.count_less_than(int(l[2])+1)-rbt.count_less_than(int(l[1])))

