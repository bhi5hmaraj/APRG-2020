import sys
sys.setrecursionlimit(10**6)

numbers_list = []
for ite in range(100000 + 1):
    numbers_list.append(0)

'''
class sentinel:
    def __init__(self):
        self.color = RED
        self.size = 0
        self.value = None

SENTINEL = sentinel()

'''

class Node:

  def __init__(self , val , p = None , col = "red"):
    self.value = val
    self.left = None
    self.right = None
    self.parent = p
    self.size = 1
    self.color = col

  def updateSize(self):
    if self.left == None and self.right == None:
      self.size = 1
    elif self.left == None:
      self.size = 1 + self.right.size
    elif self.right == None:
      self.size = 1 + self.left.size
    else:
      self.size = 1 + self.left.size + self.right.size

  def updateParent(self):
    if self.left != None:
      self.left.parent = self
    if self.right != None:
      self.right.parent = self

class RedBlackTree:

  def __init__(self):
    self.root = None

  def left_rotate(self , new_node):
    if new_node.right != None:
      temp = new_node
      new_node = new_node.right
      if self.root == temp:
        self.root = new_node
        new_node.parent = None
      else:
        if temp == temp.parent.left:
          temp.parent.left = new_node
        else:
          temp.parent.right = new_node
        new_node.parent = temp.parent
      temp.right = new_node.left
      new_node.left = temp
      new_node.updateParent()
      new_node.left.updateParent()
      new_node.left.updateSize()
      new_node.updateSize()
      if(self.root != new_node):
        new_node.parent.updateSize()

  def right_rotate(self , new_node):
    if new_node.left != None:
      temp = new_node
      new_node = new_node.left
      if self.root == temp:
        self.root = new_node
        new_node.parent = None
      else:
        if temp == temp.parent.left:
          temp.parent.left = new_node
        else:
          temp.parent.right = new_node
        new_node.parent = temp.parent
      temp.left = new_node.right
      new_node.right = temp
      new_node.updateParent()
      new_node.right.updateParent()
      new_node.right.updateSize()
      new_node.updateSize()
      if self.root != new_node:
        new_node.parent.updateSize()

  '''
  def count_less_than3(self,x):
        if self.root == None:
            return 0
        return self.count_less_than4(self.root,x)
    def count_less_than4(self,node,x):
        if node.value == None:
            return 0
        if node.value < x:
            return 1 + node.left.size + self.count_less_than4(node.right,x)
        else:
            return self.count_less_than4(node.left,x)

  '''

  def rebalance(self , node):
    if (node == self.root):
      node.color = "black"
      return
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
    numbers_list[x] = 1
    if(self.root == None):
      newnode = Node(x , None , "black")
      self.root = newnode
      return
    else:
      while(node != None):
        if x < node.value:
            if node.left == None:
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
        elif x > node.value:
            if node.right == None:
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

  def count_less_than(self , node , x):
    if node == None:
      return 0
    else:
      if node.value > x:
        return self.count_less_than(node.left , x)
      else:
        p = self.count_less_than(node.right , x)
        if(node.left == None):
          return p + 1
        else:
          return p + 1 + node.left.size

  def count_greater_than(self , node , x):
    if node == None:
      return 0
    else:
      if node.value < x:
        return self.count_greater_than(node.right , x)
      else:
        p = self.count_greater_than(node.left , x)
        if(node.right == None):
          return p + 1
        else:
          return p + 1 + node.right.size

  '''
  def print_tree(self):
        self.print_tree2(self.root)
    def print_tree2(self,node):
        if node == SENTINEL:
            print("")
            return
        self.print_tree2(node.left)
        print(node.value)
        self.print_tree2(node.right)

    def compute_subtree_size(self):
        if self.root == None:
            return
        self.compute_subtree_size2(self.root)
    def compute_subtree_size2(self,node):
        if node == SENTINEL:
            return 0
        self.compute_subtree_size2(node.left)
        self.compute_subtree_size2(node.right)
        node.size = self.compute_subtree_size2(node.left) + self.compute_subtree_size2(node.right)+1
        return node.size

  '''

  def find_ans(self , node , l , r):
    if node == None:
      return 0
    else:
      if node.value > r:
        return self.find_ans(node.left , l , r)
      elif(node.value < l):
        return self.find_ans(node.right , l , r)
      else:
        x = self.count_greater_than(node.left , l)
        y = self.count_less_than(node.right , r)
        return 1 + x + y

tree = RedBlackTree()
queries = int(raw_input())

for i in range(queries):
    line = list(raw_input().split())
    if(line[0] == "+"):
        if(numbers_list[int(line[1])] == 0):
            tree.insert(tree.root , int(line[1]))
    else:
        a = int(line[1])
        b = int(line[2])
        if(a > b):
            print(0)
        elif(a == b):
            if(numbers_list[b] == 1):
                print(1)
            else:
                print(0)
        else:
            print(tree.find_ans(tree.root , a , b))
