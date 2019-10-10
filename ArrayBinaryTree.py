
class Node(object):

		def __init__(self,element = None,left = None,right = None):
			self.element = element
			self.left = left
			self.right = right

		def get_element(self):
			return self.element



class ArrayBinaryTree(object):
	def __init__(self,node = None):
		self.root = node
		

	def add(self,element):
		node = Node(element)

		if self.root is None:
			self.root = node

		else:
			q = []
			q.append(self.root)

			while len(q):
				node_ = q.pop(0)
				if node_.left is None:
					node_.left = node
					return
				elif node_.right is None:
					node_.right = node
					return
				else:
					q.append(node_.left)
					q.append(node_.right)

	def pre(self,root):
		if root is None:
			return
		print(root.element)
		self.pre(root.left)
		self.pre(root.right)

	def mid(self,root):
		if root is None:
			return
		self.mid(root.left)
		print(root.element)
		self.mid(root.right)

	def post(self,root):
		if root is None:
			return 
		self.post(root.left)
		self.post(root.right)
		print(root.element)




























