import sys
sys.setrecursionlimit(10**6)

# color = False is Black
RED=True
BLACK=False
class Node:
    def __init__(self,val,parent,color=False,size=0,left=None,right=None):
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right
        self.size = size
        self.color = color
class RedBlackTree:
    def __init__(self):
        self.meganode = Node(None,None)
        self.meganode.parent = self.meganode
        self.meganode.left = self.meganode
        self.meganode.right = self.meganode
        self.root = Node(None,self.meganode)
    
    def printTree(self,nxt=None):
        cur = nxt
        if cur == None:
            cur = self.root
        if cur.val == None:
            return
        par = None
        if cur.parent != None:
            par = cur.parent.val
        
        ans = str(par)+ " - " + str(cur.val) +" red: "+str(cur.color) + " - " + str(cur.left.val) + " , " + str(cur.right.val)
        print(ans)
        self.printTree(nxt=cur.left)
        self.printTree(nxt=cur.right)
        return
        
    def updsize(self,cur):
        if cur==self.meganode:
            return
        
        cur.size+=1
        self.updsize(cur.parent)
    
    def modnil(self,cur,val):
        cur.val = val
        cur.color = RED
        cur.left = Node(None,cur,color=BLACK)
        cur.right = Node(None,cur,color=BLACK)
        self.updsize(cur)
    
    def search(self,val,nxt=None):
        cur=nxt
        if cur==None:
            cur=self.root
        if (cur.val == None) or (cur.val == val):
            return cur
        elif cur.val < val:
            return self.search(val,nxt=cur.right)
        elif cur.val > val:
            return self.search(val,nxt=cur.left)
    
    def cnt(self,val,nxt=None):
        cur=nxt
        if cur==None:
            cur=self.root
        
        if (cur.val == None):
            return 0
        elif cur.val <= val:
            return 1 + cur.left.size + self.cnt(val,nxt=cur.right)
        elif cur.val > val:
            return self.cnt(val,nxt=cur.left)

    def rightrot(self,rt):
        if rt.val == None or rt.left.val == None or rt==self.meganode:
            return
        pvt = rt.left
        t = pvt.right
        #sizes
        pvt.size=rt.size
        rt.size-=pvt.left.size+1
        #
        if rt.parent != self.meganode:
            if rt.parent.right == rt:
                rt.parent.right = pvt
            elif rt.parent.left == rt:
                rt.parent.left = pvt
        
        pvt.parent = rt.parent
        rt.parent = pvt
        pvt.right = rt
        t.parent = rt
        rt.left = t
        if pvt.parent == self.meganode:
            self.root = pvt
        return

    def leftrot(self,rt):
        if rt.val == None or rt.right.val == None or rt==self.meganode:
            return
        pvt = rt.right
        t = pvt.left
        #sizes
        pvt.size=rt.size
        rt.size-=pvt.right.size+1
        #
        if rt.parent != self.meganode:
            if rt.parent.right == rt:
                rt.parent.right = pvt
            elif rt.parent.left == rt:
                rt.parent.left = pvt

        pvt.parent = rt.parent
        rt.parent = pvt
        pvt.left = rt
        t.parent = rt
        rt.right = t
        if pvt.parent == self.meganode:
            self.root = pvt
        return

    def rr(self,val):
        self.rightrot(self.search(val))
    def rl(self,val):
        self.leftrot(self.search(val))

    def fixtree(self,z):
        while z.parent.color == RED:
            
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == RED:
                    z.parent.color = BLACK
                    y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.leftrot(z)
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self.rightrot(z.parent.parent)
            else:
                y=z.parent.parent.left
                if y.color == RED:
                    z.parent.color = BLACK
                    y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.rightrot(z)
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self.leftrot(z.parent.parent)
            self.meganode.color = BLACK
            if z==self.root or z==self.meganode:
                break

        self.root.color = BLACK
        self.meganode.color = BLACK

    def insert(self,val):
        cur=self.search(val)
        if cur.val == None:
            self.modnil(cur,val)
            self.fixtree(cur)


def run():
    tree = RedBlackTree()
    n = int(input())
    while n>0:
        inp = input().split(' ')
        q = inp[0]
        if q == '+':
            tree.insert(int(inp[1]))
        elif q=='p':
            tree.printTree()
        elif q=='rr':
            tree.rr(int(inp[1]))
        elif q=='rl':
            tree.rl(int(inp[1]))
        elif q=='?':
            ans=tree.cnt(int(inp[2]))-tree.cnt(int(inp[1])-1)
            print(ans)

        n-=1

    return 0

run()


