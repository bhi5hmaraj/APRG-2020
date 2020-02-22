class RedBlackTree():

	@staticmethod
	def inorder_print(curr):
		if curr != None:
			inorder_print(curr.left)
			print("val = %d, cnt = %d" % (curr.val, curr.cnt))
			inorder_print(curr.right)


	def print_tree(self):
		inorder_print(self.root)


	@staticmethod
	def ht(node):
		return 0 if node == None else node.height

	@staticmethod
	def insert_(curr, x):
		if curr == None:
			return Node(val=x)
		elif curr.val == x:
			curr.cnt += 1
			return curr
		else:
			new_tree = insert_(curr.right, x) if curr.val < x else insert_(curr.left, x)
			
			if curr.val < x :
				curr.right = new_tree
			else:
				curr.left = new_tree

			new_tree.parent = curr
			curr.height = 1 + max(ht(curr.left), ht(curr.right))

			return curr

	def insert(self, x):
		root = insert_(self.root, x)

	def __init__(self, root=None):
		self.root = None


	class Node:

		def __init__(self, val, left=None, right=None, parent=None, height=0, cnt=1):
			self.val = val
			self.left = left
			self.right = right
			self.parent = parent
			self.height = height
			self.cnt = cnt




rbtree = RedBlackTree()
rbtree.insert(val=3)
rbtree.insert(val=2)
# rbtree.insert(1)
# rbtree.insert(3)
# rbtree.insert(3)
# rbtree.insert(5)
rbtree.print_tree()
