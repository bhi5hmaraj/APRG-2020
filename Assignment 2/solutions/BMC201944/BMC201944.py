import sys
sys.setrecursionlimit(10**6)

Black = 0
Red = 1

class Node:
    def __init__(self, val = None):
        self.value = val
        self.left = None
        self.right = None
        self.parent = None
        self.colour = 1
        self.size = 1


class RBTree:
    def __init__(self, root = None):
        self.root = root

    def isTempty(self):
        return(self.root == None)

    def leftR(self,N):
        M = N.right
        N.right = M.left
        if M.left != None:
            (M.left).parent = N
            c = M.left.size
        else: 
            c = 0
        M.parent = N.parent
        if N.parent == None:
            self.root = M
        elif N == (N.parent).left:
            (N.parent).left = M
        else:
            (N.parent).right = M
        M.left = N
        N.parent = M
        tt = M.size
        M.size = N.size
        N.size = M.size - tt + c

    def rightR(self,N):
        M = N.left
        N.left = M.right
        if M.right != None:
            (M.right).parent = N
            c = M.right.size
        else:
            c = 0
        M.parent = N.parent
        if N.parent == None:
            self.root = M
        elif N == (N.parent).right:
            (N.parent).right = M
        else:
            (N.parent).left = M
        M.right = N
        N.parent = M
        tt = M.size
        M.size = N.size
        N.size = M.size - tt + c



    def BSTinsert(self,N):
        temp = None
        R = self.root
        while R!=None:
            R.size += 1
            temp = R
            if N.value < R.value:
                R = R.left
            else:
                R = R.right
        N.parent = temp
        if temp == None:
            self.root = N
        elif N.value < temp.value:
            temp.left = N
        else:
            temp.right = N
        N.left = None
        N.right = None
        N.colour = 1

    def BalanceBST(self,N):
        while (N.parent).colour == 1:
            if N.parent == ((N.parent).parent).left:
                M = ((N.parent).parent).right
                if M.colour == 1:
                    (N.parent).colour = 0
                    M.colour = 0
                    ((N.parent).parent).colour = 1
                    N = (N.parent).parent
                else:
                    if N == (N.parent).right:
                        N = N.parent
                        self.leftR(self,N)
                    (N.parent).colour = 0
                    ((N.parent).parent).colour = 1
                    self.rightR(self,((N.parent).parent))
            else:
                M = ((N.parent).parent).left
                if M.colour == 1:
                    (N.parent).colour = 0
                    M.colour = 0
                    ((N.parent).parent).colour = 1
                    N = (N.parent).parent
                else:
                    if N == (N.parent).left:
                        N = N.parent
                        self.rightR(self,N)
                    (N.parent).colour = 0
                    ((N.parent).parent).colour = 1
                    self.leftR(self,((N.parent).parent))
        (self.root).colour = 0

    def insert(self,N):
        N.BSTinsert()
        N.BalanceBST()

    def count_less_than(self,v,n):

        if(v == None):
            return 0
        if(v.left == None):
            s = 0
        else:
             s = v.left.size

        if v.value == n:
            return(s+1)
        elif v.value > n:
            return(self.count_less_than(v.left,n))
        else:
            return(s + 1 + self.count_less_than(v.right,n))

q = int(input())

s = RBTree()

while q:
    q -= 1
    inp = input()
    if(inp[0] == "+"):
        x = int(inp[2:])
        if(s.count_less_than(s.root,x) - s.count_less_than(s.root,x-1) == 0):
            s.BSTinsert(Node(x))
    else:
        l,r = map(int, inp[2:].split())
        print(s.count_less_than(s.root,r) - s.count_less_than(s.root,l-1))

