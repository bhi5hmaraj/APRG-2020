import sys
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.color = 0
        self.size = 0

class RBTree:
    def __init__(self,r):
        self.root = Node(r)
        self.size = 0
        
    def insertnode(self,new_node,a):
        if (new_node.value > a ):
            if (new_node.left is None):
                new_node.left = Node(a)
            else:
                self.insertnode(new_node.left,a)
        elif (new_node.value < a):
            if (new_node.right is None):
                new_node.right = Node(a)
            else:
                self.insertnode(new_node.right,a)

    def insert(self, a):
        if (int(a) < 1 ):
                return
        if ( int(a) > 100000):
            return
        if self.size is 0:
            self.root = Node(a)
            self.size = 1
        else:
            self.insertnode(self.root,a)
            #self.rb_balance(self.root)
            
    def inorder_pr__(self, node):
        if node != None:
            self.inorder_pr__(node.left)
            sys.stdout.write(str(node.value))
            self.inorder_pr__(node.right)
       
    def inorder__(self):
        self.inorder_pr__(self.root)
       
    def print_tree(self):
        self.inorder__()
            
    def inorder_pr__c(self, node, l,r):
        if node != None:
            x = int(self.inorder_pr__c(node.left,l,r))
            if (int(node.value) >= int(l)):
                if (int(node.value) <= int(r)):
                    x = (int)(x)+1;
            y = int(self.inorder_pr__c(node.right,l,r))
            return x+y
        else:
            return 0
       
    def count(self):
        return self.inorder_pr__c(self.root)
       
    def find_custom(self, l, r):
        return self.inorder_pr__c(self.root, l,r)
   
   
           


if __name__ == "__main__":
    bst = RBTree(5)

num = int(input())
#print(num)
for var in list(range(num)):
    #print("\nWhat Operation you want to do ['+' <num> / '?' <left, right>] ?")
    x = input().split()
    if x[0] == '+':
        z = x[1]
        #print("insert " + z)
        bst.insert(z)
    elif x[0] == '?':
        left_range = x[1]
        right_range = x[2]
        #print("find in " + left_range + " , " + right_range)
        v = bst.find_custom(left_range,right_range)
        print(v)
    #else:
        #print("Invalid Input")
    
            
    
