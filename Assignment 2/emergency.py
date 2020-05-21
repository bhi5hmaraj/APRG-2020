class Node:
    def __init__(self,col,val):
        self.right=None
        self.left=None 
        self.parent= None
        self.col= col
        self.val= val
        self.size= None
        
class RBT:

    def simple_print(self, curr):
        if curr != None:
            self.simple_print(curr.left)
            print(curr.val)
            self.simple_print(curr.right)

    def print_tree(self):
        l = RBT.pretty_print("", True, [], self.root)
        print('\n'.join(l))

    def pretty_print(prefix, isTail, sb, root):
        if root == None:
            return ["Tree is empty"]


        if root.right != None:
            RBT.pretty_print(prefix + ("|   " if isTail else "    "), False, sb, root.right)

        # sb.append(prefix + "|-- " + str(root.val) + " (p = {}, c = {}, sz = {})".format(root.parent.val, root.color, root.size))
        sb.append(prefix + "|-- " + ("v=%d, s=%d" % (root.val, root.size)) )
        if root.left != None:
            RBT.pretty_print(prefix + ("|   " if not isTail else "    "), True, sb, root.left)

        return sb

    def __init__(self):
        self.root = Node('b',None)
    def newsize(self,node):
        if node.parent != None:
            node.parent.size= node.parent.size +1
            self.newsize(node.parent)
    def left_rotate(self,z):
        
        y=z.right
        T2= y.left
            
        if T2== None:
            y.left= z
            y.parent= z.parent
            z.parent= y
            z.right= T2
            z.size= z.size-y.size
            y.size= y.size+z.size
            
        else:
            y.left= z
            z.right= T2
            y.parent= z.parent
            z.parent= y
            T2.parent= z
            z.size= z.size-y.size+ T2.size
            y.size= z.size+y.size-T2.size
         
        if y.parent!= None:
            if y.parent.left== z:
              y.parent.left=y
            else:
              y.parent.right=y
        
    def right_rotate(self,z):
        y= z.left
        T3= y.right
        
        if T3== None:
            y.right= z
            y.parent= z.parent
            z.parent= y
            z.left= T3
            z.size= z.size-y.size
            y.size= y.size+z.size
        else:
            y.right= z
            z.left= T3
            y.parent= z.parent
            z.parent= y
            T3.parent= z
            z.size= z.size-y.size+ T3.size
            y.size= z.size+y.size-T3.size
        if y.parent!= None:
            if y.parent.right== z:
              y.parent.right=y
            else:
              y.parent.left=y
    def search(self,val,nxt,nd):
        
        
        if nxt is None:
            return nd
        elif nxt.parent== None and nxt.val== None:
            return nxt
        elif nxt.val== val:
            return nxt
        elif nxt.val< val:
            return self.search(val,nxt.right,nxt)
        elif nxt.val> val:
            return self.search(val,nxt.left,nxt)
        
        
    def insert(self,val):
        cur= self.search(val,self.root,None)
        if cur.parent== None and cur.val== None:
            self.root.val= val
            self.root.size=1
        elif cur.val< val:
            cur.right = Node('r',val)
            cur.right.parent= cur
            cur.right.size=1
            self.newsize(cur.right)
            self.rebalance(cur.right)
            
          
        elif cur.val> val:
            cur.left= Node('r',val)
            cur.left.parent= cur
            cur.left.size=1
            self.newsize(cur.left)
            self.rebalance(cur.left)
            
        
    
            
    def rebalance(self,node):
        if node.parent== None:
            node.col= 'b'
        elif node.parent.col=='r':
            if node.parent.parent.right== None:
                if node.parent.right== node:
                    self.left_rotate(node.parent)
                    self.right_rotate(node.parent)
                    node.col='b'
                    node.right.col= 'r'
                    if node.parent== None:
                        self.root= node
                else : 
                    self.right_rotate(node.parent.parent)
                    node.parent.col= 'b'
                    node.parent.right.col='r'
                    if node.parent.parent== None:
                        self.root= node.parent
            elif node.parent.parent.left==None:
                if node.parent.left== node:
                    self.right_rotate(node.parent)
                    self.left_rotate(node.parent)
                    node.col='b'
                    node.left.col= 'r'
                    if node.parent== None:
                        self.root= node
                else:
                    
                    self.left_rotate(node.parent.parent)
                    node.parent.col='b'
                    node.parent.left.col='r'
                    if node.parent.parent== None:
                        self.root= node.parent
                   
                    
            elif node.parent.parent.right.col== 'b':
                if node.parent.right== node:
                    self.left_rotate(node.parent)
                    self.right_rotate(node.parent)
                    node.col='b'
                    node.right.col= 'r'
                    if node.parent== None:
                        self.root= node
                else : 
                    self.right_rotate(node.parent.parent)
                    node.parent.col= 'b'
                    node.parent.right.col='r'
                    if node.parent.parent== None:
                        self.root= node.parent
            elif node.parent.parent.left.col=='b':
                if node.parent.left== node:
                    self.right_rotate(node.parent)
                    self.left_rotate(node.parent)
                    node.col='b'
                    node.left.col= 'r'
                    if node.parent== None:
                        self.root= node
                else:
                    self.left_rotate(node.parent.parent)
                    node.parent.col='b'
                    node.parent.left.col='r'
                    if node.parent.parent== None:
                        self.root= node.parent
            elif node.parent.parent.right.col== 'r':
                    node.parent.col= 'b'
                    node.parent.parent.col= 'r'
                    node.parent.parent.left.col= 'b'
                    self.rebalance(node.parent.parent)
            elif node.parent.parent.left.col== 'r':
                    node.parent.col= 'b'
                    node.parent.parent.col= 'f'
                    node.parent.parent.right.col= 'b'
                    self.rebalance(node.parent.parent)
    def rec(self,x, node):


        if node is None or node.val is None:
            return 0
        elif node.val<x :
          if node.left == None:
             return(1+self.rec(x,node.right))
          else:
             return (node.left.size+1+self.rec(x,node.right))
        elif node.val==x:
          if node.left== None:
              return 1
          else:
              return (node.left.size)
        elif node.val>x:
          if node.left== None:
              return 0
          else:
              return self.rec(x,node.left)
          
    def count_less_than(self,x):
        return self.rec(x,self.root)

def run():
    tree = RBT()
    n = int(input())
    for _ in range(n):
        inp = input().split(' ')
        q = inp[0]
        if q == '+':
            tree.insert(int(inp[1]))
            tree.print_tree()
        elif q=='?':
            a=tree.count_less_than(int(inp[2])+1)-tree.count_less_than(int(inp[1]))
            # print(a)

        # tree.simple_print(tree.root)
        print()
        # print()

run() 
