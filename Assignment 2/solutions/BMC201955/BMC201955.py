import sys

class Node():
    def __init__(self, value):
        self.value = value
        self.colour = None
        self.left = None 
        self.right = None 


class RBT():
  def __init__(self):
    self.node = None

  def insert(self, x):
    rbtval = self.node
    newval = Node(x)
    if rbtval == None:
      self.node.value = newval
      self.node.colour = "red"
      self.node.left = RBT()
      self.node.right = RBT()
    elif x < rbtval.value:
      self.node.left.insert(x)
    else:
      self.node.right.insert(x)
    self.rebalance()

  def leftrotate(self):
    x = self.node 
    y = self.node.right.node 
    z = y.left.node 
        
    self.node = y 
    y.left.node = x 
    x.right.node = z

  def rightrotate(self):
    x = self.node 
    y = self.node.left.node 
    z = y.right.node 
        
    self.node = y 
    y.right.node = x 
    x.left.node = z

  def rebalance(self):
    if (self.node.left.node.value == None) or (self.node.right.node.value == None):
      return()
    else:
      if (self.node.colour == "black") and (self.node.left.node.colour == "red") and (self.node.right.node.colour == "red") and (self.node.left.node.right.node.colour == "red"):
        self.node.colour = "red"
        self.node.left.node.colour = "black"
        self.node.right.node.colour = "black"
        self.rebalance()

      elif (self.node.colour == "black") and (self.node.left.node.colour == "red") and (self.node.right.node.colour == "red") and (self.node.left.node.left.node.colour == "red"):
        self.node.colour = "red"
        self.node.left.node.colour = "black"
        self.node.right.node.colour = "black"
        self.rebalance()

      elif (self.node.colour == "black") and (self.node.left.node.colour == "red") and (self.node.right.node.colour == "red") and (self.node.right.node.left.node.colour == "red"):
        self.node.colour = "red"
        self.node.left.node.colour = "black"
        self.node.right.node.colour = "black"
        self.rebalance()

      elif (self.node.colour == "black") and (self.node.left.node.colour == "red") and (self.node.right.node.colour == "red") and (self.node.right.node.right.node.colour == "red"):
        self.node.colour = "red"
        self.node.left.node.colour = "black"
        self.node.right.node.colour = "black"
        self.rebalance()

      elif (self.node.colour == "black") and (self.node.left.node.colour == "red") and(self.node.left.node.right.node.colour == "red"):
        self.node.left.node.leftrotate()
        self.rebalance()

      elif (self.node.colour == "black") and (self.node.left.node.colour == "red") and(self.node.left.node.left.node.colour == "red"):
        self.node.rightrotate()
        self.node.colour = "black"
        self.node.left.node.colour = "red"
        self.node.right.node.colour = "red"
        self.rebalance()
    
      elif (self.node.colour == "black") and (self.node.right.node.colour == "red") and(self.node.right.node.left.node.colour == "red"):
        self.node.right.node.rightrotate()
        self.rebalance()

      elif (self.node.colour == "black") and (self.node.left.node.colour == "red") and(self.node.right.node.right.node.colour == "red"):
        self.node.leftrotate()
        self.node.colour = "black"
        self.node.left.node.colour = "red"
        self.node.right.node.colour = "red"
        self.rebalance()

      else:
        self.node.left.node.rebalance()
        self.node.right.node.rebalance()

  def count(self,l,u):
    if (self.node.left.node.value == None) and (self.node.right.node.value == None):
      if (self.node.value <= u) and (self.node.value >= l):
        return(1)
      else:
        return(0)

    elif (self.node.left.node.value == None):
      if (self.node.value <= u) and (self.node.value >= l):
        return(1 + self.node.right.count(l,u))
      else:
        return(self.node.right.count(l,u))

    elif (self.node.right.node.value == None):
      if (self.node.value <= u) and (self.node.value >= l):
        return(1 + self.node.left.count(l,u))
      else:
        return(self.node.left.count(l,u))
      
    else:
      if (self.node.value <= u) and (self.node.value >= l):
        return(1 + self.node.left.count(l,u) + self.node.right.count(l,u))
      elif self.node.value > u:
        return(self.node.left.count(l,u))
      else:
        return(self.node.right.count(l,u))

n = int(input())
inpi = []
for i in range(n):
    inpi = inpi + lst(input())

outp = []
for j in range(n):
    if (inpi[j][0] == '+'):
        rbt.insert(inpi[j][2:])
    else:
        rebt.count(inpi[j][2:])

for ele in outp:
    print(ele)








