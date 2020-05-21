#an implementation of red-black trees along with an application in 
#ran
import sys
sys.setrecursionlimit(10**6)
thislist = []
for i in range(100000 + 1):
    thislist.append(0)
class Node: 
  def __init__(self , val , par = None , col = "red"):
    self.value = val
    self.left = None
    self.right = None
    self.parent = par
    self.size = 1
    self.color = col
  def updateSize(self):
    if (self.left == None and self.right == None):
      self.size = 1
    elif (self.left == None):
      self.size = 1 + self.right.size
    elif (self.right == None):
      self.size = 1 + self.left.size
    else:
      self.size = 1 + self.left.size + self.right.size
  def updateParent(self):
    if(self.left != None):
      self.left.parent = self
    if(self.right != None):
      self.right.parent = self
class RedBlackTree:
  def __init__(self):
    self.root = None
  def left_rotate(self , node):
    if(node.right != None):
      temp = node
      node = node.right
      if(self.root == temp):
        self.root = node
        node.parent = None
      else:
        if(temp == temp.parent.left):
          temp.parent.left = node
        else:
          temp.parent.right = node
        node.parent = temp.parent
      temp.right = node.left
      node.left = temp
      node.updateParent()
      node.left.updateParent()
      node.left.updateSize()
      node.updateSize()
      if(self.root != node):
        node.parent.updateSize()
  def right_rotate(self , node):
    if(node.left != None):
      temp = node
      node = node.left
      if(self.root == temp):
        self.root = node
        node.parent = None
      else:
        if(temp == temp.parent.left):
          temp.parent.left = node
        else:
          temp.parent.right = node
        node.parent = temp.parent
      temp.left = node.right
      node.right = temp
      node.updateParent()
      node.right.updateParent()
      node.right.updateSize()
      node.updateSize()
      if(self.root != node):
        node.parent.updateSize()
  #rebalance is always called on a red node, and only if parent
  #of the current node is red
  def rebalance(self , node):
    if (node == self.root):
      node.color = "black"
      return 
    #case 1, when node's uncle is a right child
    if(node.parent == node.parent.parent.left):
      if(node.parent.parent.right != None and node.parent.parent.right.color == "red"):
        node.parent.color = "black";
        node.parent.parent.right.color = "black"
        node.parent.parent.color = "red"
        if(node.parent.parent == self.root or node.parent.parent.parent.color == "red"):
          self.rebalance(node.parent.parent)
        return
      else:
        if(node == node.parent.right):
          self.left_rotate(node.parent)
          node.color = "black"
          node.parent.color = "red"
          self.right_rotate(node.parent)
        else:
          node.parent.color = "black"
          node.parent.parent.color = "red"
          self.right_rotate(node.parent.parent)
        return
    #case 2, when node's uncle is a left child
    else:
      if(node.parent.parent.left != None and node.parent.parent.left.color == "red"):
        node.parent.color = "black";
        node.parent.parent.left.color = "black"
        node.parent.parent.color = "red"
        if(node.parent.parent == self.root or node.parent.parent.parent.color == "red"):
          self.rebalance(node.parent.parent)
      else:
        if(node == node.parent.left):
          self.right_rotate(node.parent)
          node.color = "black"
          node.parent.color = "red"
          self.left_rotate(node.parent)
        else:
          node.parent.color = "black"
          node.parent.parent.color = "red"
          self.left_rotate(node.parent.parent)
        return
  def insert(self , node , x):
    thislist[x] = 1
    if(self.root == None):
      newnode = Node(x , None , "black")
      self.root = newnode
      return 
    else:
      while(node != None):
        if(x < node.value):
            if(node.left == None):
                newnode = Node(x , node , "red")
                node.left = newnode
                node.size = node.size + 1
                if(node.color == "red"):
                    self.rebalance(newnode)
                break
            else:
                node.size = node.size + 1
                node = node.left
                continue
        elif(x > node.value):
            if(node.right == None):
                newnode = Node(x , node , "red")
                node.right = newnode
                node.size = node.size + 1
                if(node.color == "red"):
                    self.rebalance(newnode)
                break
            else:
                node.size = node.size + 1
                node = node.right
                continue
  def lessThan(self , node , x):
    if (node == None):
      return 0
    else:
      if(node.value > x):
        return self.lessThan(node.left , x)
      else:
        p = self.lessThan(node.right , x)
        if(node.left == None):
          return p + 1
        else:
          return p + 1 + node.left.size
  def greaterThan(self , node , x):
    if (node == None):
      return 0
    else:
      if(node.value < x):
        return self.greaterThan(node.right , x)
      else:
        p = self.greaterThan(node.left , x)
        if(node.right == None):
          return p + 1
        else:
          return p + 1 + node.right.size
  def inRange(self , node , l , r):
    if(node == None):
      return 0
    else:
      if(node.value > r):
        return self.inRange(node.left , l , r)
      elif(node.value < l):
        return self.inRange(node.right , l , r)
      else:
        p1 = self.greaterThan(node.left , l)
        p2 = self.lessThan(node.right , r)
        return 1 + p1 + p2
tree = RedBlackTree()
q = int(input())
while(q > 0):
    q = q - 1
    line = list(input().split())
    if(line[0] == "+"):
        if(thislist[int(line[1])] == 0):
            tree.insert(tree.root , int(line[1]))
    else:
        s = int(line[1])
        t = int(line[2])
        if(s > t):
            print(0)
        elif(s == t):
            if(thislist[t] == 1):
                print(1)
            else:
                print(0)
        else:
            print(tree.inRange(tree.root , s , t))




  
    





