
Red = True
Black = False

class Node:
    def __init__(self, value, size, color):
        self.value = value
        self.size = size
        self.color = color
        self.left = None
        self.right = None

class RedBlackTree:

    def __init__(self):
        self.root = None

    def isRed(self, h):
        if(h == None):
            return False
        else:
            return h.color

    def size(self, h):
        if(h == None):
            return 0
        else:
            return h.size

    def rotateLeft(self, h):
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = Red
        x.size = h.size
        h.size = 1 + self.size(h.left) + self.size(h.right)
        return x

    def rotateRight(self, h):
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = Red
        x.size = h.size
        h.size = 1 + self.size(h.left) + self.size(h.right)
        return x

    def flipColors(self, h):
        h.color = Red
        h.left.color = Black
        h.right.color = Black

    def put(self, h, val):
        if(h == None):
            return Node(val, 1, Red)

        if(val < h.value):
            h.left = self.put(h.left, val)
        elif(val > h.value):
            h.right = self.put(h.right, val)
        else:
            h.value = val

        if(self.isRed(h.right) and not self.isRed(h.left)):
            h = self.rotateLeft(h)
        if(self.isRed(h.left)):
            if(self.isRed(h.left.left)):
                h = self.rotateRight(h)
        if(self.isRed(h.left) and self.isRed(h.right)):
            self.flipColors(h)

        h.size = 1 + self.size(h.left) + self.size(h.right)
        return h

    def insert(self, val):
        self.root = self.put(self.root, val)
        self.root.color = Black

    def count(self, h, val):
        if(h == None):
            return 0
        if(h.value <= val):
            return 1 + self.size(h.left) + self.count(h.right, val)
        if(h.value > val):
            return self.count(h.left, val)

    def inRange(self, l, r):
        return self.count(self.root, r) - self.count(self.root, l-1)

spec = int(input())

BST = RedBlackTree()

for i in range(spec):
    a = input()

    a1 = list(map(int, a[2:].split()))
    if(a[0] == "+"):
        BST.insert(int(a1[0]))
        
    elif(a[0] == "?"):
        print(BST.inRange(int(a1[0]), int(a1[1])))
