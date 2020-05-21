class Node():
    def __init__(self,value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1
        self.size = 1
        
class RedBlackTree():
    def __init__(self):
        self.luffy = Node(None)
        self.luffy.color = 0
        self.luffy.left = None
        self.luffy.right = None
        self.root = self.luffy
        
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if(y.left != self.luffy):
            l_size = y.left.size
        else:
            l_size = 0

        if y.left != self.luffy:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
        ys = y.size
        y.size = x.size
        x.size  = y.size - ys + l_size


        
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if(y.right != self.luffy):
            r_size = y.right.size
        else:
            r_size = 0
        if y.right != self.luffy:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
        ys = y.size
        y.size = x.size
        x.size  = y.size - ys + r_size
        
    def  rebalance(self, new):
        while new.parent.color == 1:
            if new.parent == new.parent.parent.right:
                uncle = new.parent.parent.left
                if new.color == 1:
                    uncle.color = 0
                    new.parent.color = 0
                    new.parent.parent.color = 1
                    new = new.parent.parent
                else:
                    if new == new.parent.left:
                        new = new.parent
                        self.right_rotate(new)
                    new.parent.color = 0
                    new.parent.parent.color = 1
                    self.left_rotate(new.parent.parent)
            else:
                uncle = new.parent.parent.right
                if uncle.color == 1:
                    uncle.color = 0
                    new.parent.color = 0
                    new.parent.parent.color = 1
                    new = new.parent.parent 
                else:
                    if new == new.parent.right:
                        new = new.parent
                        self.left_rotate(new)
                    new.parent.color = 0
                    new.parent.parent.color = 1
                    self.right_rotate(new.parent.parent)
            if new == self.root:
                break
        self.root.color = 0

    def insert(self, n):
        new = Node(n)
        new.parent = None
        new.value = n
        new.left = self.luffy
        new.right = self.luffy


        y = None
        x = self.root

        while x != self.luffy:
            y = x
            x.size += 1
            if new.value < x.value:

                x = x.left
            else:
                x = x.right

        new.parent = y
        if y == None:
            self.root = new
            new.color = 0
            return
        elif new.value < y.value:
            y.left = new
        else:
            y.right = new


        #print(new.value)     
        self.rebalance(new) 


    def count_less_than(self,x):
        size = 0
        if(self.root == self.luffy):
            return 0
        k = self.root
        while True:
            if(k.left != self.luffy):
                lsize = k.left.size+1
            else:
                lsize = 1

            if( x >= k.value):
                size += lsize
                k = k.right
            else:
                k = k.left

            if(k == self.luffy):
                return size

    
q=int(input()) 

s=RedBlackTree()
while(q) :
    q=q-1
    a=input()
    if a[0]== "+" :
        x=  int(a[2:])
        if(s.count_less_than(x) - s.count_less_than(x-1) == 0):
            s.insert(x)
    else:
        l,r = map(int, a[2:].split())
        t= s.count_less_than(r)- s.count_less_than(l-1)
        print(t ,end="\n")

            
        
        
        
        
        

        
            
    
        
        
