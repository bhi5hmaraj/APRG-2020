import sys
sys.setrecursionlimit(100000)
class RedBlackTreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.size = 1
        self.isRed = True


class RedBlackTree:
    def __init__(self):
        self.root = leaf
    
    def height(self, r):
        if r != leaf:
            return 1 + max(self.height(r.left), self.height(r.right))
        else:
            return 0

    def leftRotate(self, x):    
        y = x.right
        l = y.left
        size_y = y.size
        if (x == self.root):
            self.root = x.right
        y.left = x
        y.parent = x.parent
        if (x.parent != leaf):
            if (x.parent.left == x):
                x.parent.left = y
            else:
                x.parent.right = y
        x.parent = y
        x.right = l
       
        if (l != leaf):
            l.parent = x
           
        x.size = x.size + l.size - size_y
        y.size = y.size + x.size - l.size
   
    def rightRotate(self, x):
        y = x.left
        r = y.right
        size_y = y.size
        if (x == self.root):
            self.root = y
        y.right = x
        y.parent = x.parent
        if (x.parent != leaf):
            if (x.parent.right == x):
                x.parent.right = y
            else:
                x.parent.left = y
        x.parent = y
        x.left = r
       
        if (r != leaf):
            r.parent = x
           
        x.size = x.size + r.size - size_y
        y.size = y.size + x.size - r.size

class RedBlackTree(object):
    def __init__(self):
        self.root = None

    def sizeOf(self, node):
        return node.size if node else 0

    @property
    def size(self):
        return self.sizeOf(self.root)

    def rotateLeft(self, root):
        right = root.right

        root.size, right.size = self.sizeOf(root.left) + self.sizeOf(right.left) + 1, root.size
           
        root.right = right.left
        right.left = root

        right.isRed = root.isRed
        root.isRed = True

        return right

    def rotateRight(self, root):
        left = root.left

        root.size, left.size = self.sizeOf(root.right) + self.sizeOf(left.right) + 1, root.size

        root.left = left.right
        left.right = root

        left.isRed = root.isRed
        root.isRed = True

        return left

    def flipColor(self, root):
        root.left.isRed = False
        root.right.isRed = False
        root.isRed = True
        return root

    def insertTo(self, root, val):
        if not root:
            return RedBlackTreeNode(val)

        if val > root.val:
            root.right = self.insertTo(root.right, val)
        else:
            root.left = self.insertTo(root.left, val)

        if (root.right and root.right.isRed) and not (root.left and root.left.isRed):
            root = self.rotateLeft(root)

        if (root.left and root.left.isRed) and (root.left.left and root.left.left.isRed):
            root = self.rotateRight(root)

        if (root.left and root.left.isRed) and (root.right and root.right.isRed):
            root = self.flipColor(root)

        root.size = sum(map(self.sizeOf, (root.left, root.right))) + 1
        return root

    def insert(self, val):
        self.root = self.insertTo(self.root, val)
        self.root.isRed = False
    
    def getCount(self, root, low, high): 
        if root == None:        #Base case
            return 0
 
        if root.val == high and root.val == low:    #Optional, for efficiency
            return 1
     
        if root.val <= high and root.val >= low:  
            return (1 + self.getCount(root.left, low, high) + self.getCount(root.right, low, high))
                         

        elif root.val < low:  
            return self.getCount(root.right, low, high) 
  
        else: 
            return self.getCount(root.left, low, high)
        
    
# if __name__ == "__main__":
NumberOfOperations = int(input())
entered = []
INPUT = []
res = []
RBObject = RedBlackTree()
for i in range(0, NumberOfOperations):
    INPUT.append(input())
if NumberOfOperations > 100000:
    NumberOfOperations = 100000


for i in range(0,NumberOfOperations):
    inp = INPUT[i].split(" ")
    if inp[0] == "+":
        if int(inp[1]) in entered:
            continue
        RBObject.insert(int(inp[1]))
        entered.append(int(inp[1]))
    else:
        result = RBObject.getCount(RBObject.root, int(inp[1]), int(inp[2]))
        # result = len(list(x for x in entered if int(inp[1]) <= x <= int(inp[2])))
        res.append(str(result))

print("\n".join(res))