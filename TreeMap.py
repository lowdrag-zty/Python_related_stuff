class Tree:
	class Position:
		def element(self):
			raise NotImplementedError('must be implemented by subclass')
		def __eq__(self,other):
			raise NotImplementedError('must be implemented by subclass')
		def __ne__(self,other):
			return not (self==other)

	def root(self):
		raise NotImplementedError('must be implemented by subclass')
	def parent(self,p):
		raise NotImplementedError('must be implemented by subclass')
	def num_children(self,p):
		raise NotImplementedError('must be implemented by subclass')
	def children(self,p):
		raise NotImplementedError('must be implemented by subclass')
	def __len__(self):
		raise NotImplementedError('must be implemented by subclass')
	def is_root(self,p):
		return self.root() == parent
	def is_leaf(self,p):
		return self.num_children(p) == 0
	def is_empty(self):
		return len(self) == 0
###################################################################
class BinaryTree(Tree):
	def left(self,p):
		raise NotImplementedError('must be implemented by subclass')
	def right(self,p):
		raise NotImplementedError('must be implemented by subclass')
	def sibling(self,p):
		parent = self.parent(p)
		if parent is None:
			return None
		else:
			if p == self.left(parent):
				return self.right(parent)
			else:
				return self.left(parent)
	def children(self,p):
		if self.left(p) is not None:
			yield self.left(p)
		if self.right(p) is not None:
			yield self.right(p)
####################################################################
class LinkedBinaryTree(BinaryTree):
	class _Node:
		def __init__(self,element,parent = None,left = None,right = None):
			self._element = element
			self._parent = parent
			self._left = left
			self._right = right
	class Position(BinaryTree.Position):
		def __init__(self,container,node):
			self._container = container
			self._node = node
		def element(self):
			return self._node._element
		def __eq__(self,other):
			return type(other) is type(self) and other._node is self._node
	
	def _validate(self,p):
		if not isinstance(p,self.Position):
			raise TypeError('p must be proper Position type')
		if p._container is not self:
			raise ValueError('p does not belong to this container')
		if p._node._parent is p._node:
			raise ValueError('p is no longer valid')
		return p._node
	def _make_position(self,node):
		return self.Position(self,node) if node is not None else None

	def __init__(self):
		self._root = None
		self._size = 0

	def __len__(self):
		return self._size
	def root(self):
		return self._make_position(self._root)
	def parent(self,p):
		node = self._validate(p)
		return self._make_position(node._parent)
	def left(self,p):
		node = self._validate(p)
		return self._make_position(node._left)
	def right(self,p):
		node = self._validate(p)
		return self._make_position(node._right)
	def num_children(self,p):
		node = self._validate(p)
		count = 0
		if node._left is not None:
			count += 1
		if node._right is not None:
			count += 1
		return count

	def _add_root(self,e):
		if self._root is not None:
			raise ValueError('Root exists')
		self._size = 1
		self._root = self._Node(e)
		return self._make_position(self._root)

	def _add_left(self,p,e):
		node = self._validate(p)
		if node._left is not None:
			raise ValueError('Left child exists')
		self._size += 1
		node._left = self._Node(e,node)
		return self._make_position(node._left)

	def _add_right(self,p,e):
		node = self._validate(p)
		if node._right is not None:
			raise ValueError('Right child exists')
		self._size += 1
		node._right = self._Node(e,node)
		return self._make_position(node._right)

	def pre(self,_root):
		if _root is None:
			return
		print(_root._element)
		self.pre(_root._left)
		self.pre(_root._right)

	def mid(self,_root):
		if _root is None:
			return 
		self.mid(_root._left)
		print(_root._element)
		self.mid(_root._right)

	def post(self,_root):
		if _root is None:
			return
		self.post(_root._left)
		self.post(_root._right)
		print(_root._element)

class MapBase(MutableMapping):
	class _Item:
		def __init__(self,k,v):
			self._key = k
			self._value = v

		def __eq__(self,other):
			return self._key == other._key

		def __ne__(self,other):
			return not (self==other)

		def __It__(self,other):
			return self._key < other._key

class TreeMap(LinkedBinaryTree,MapBase):

	class Position(LinkedBinaryTree.Position):
		def key(self):
			return self.element()._key

		def value(self):
			return self.element()._value


	def _subtree_search(self,p,k):
		if k == p.key():
			return p
		elif k < p.key():
			if self.left(p) is not None:
				return self._subtree_search(self.left(p),k)
		else:
			if self.right(p) is not None:
				return self._subtree_search(self.right(p),k)
		return p


	def _subtree_first_position(self,p):
		walk = p
		while self.left(walk) is not None:
			walk = self.left(walk)
		return walk

	def _subtree_last_position(self,p):
		walk = p
		while self.right(walk) is not None:
			walk = self.right(walk)
		return walk

	def first(self):
		return self._subtree_first_position(self.root()) if len(self)>0 else None

	def last(self):
		return self._subtree_last_position(self.root()) if len(self)>0 else None

	def before(self,p):
		self._validate(p)
		if self.left(p):
			return self._subtree_last_position(self.left(p))
		else:
			walk = p
			above = self.parent(walk)
			while above is not None and walk == self.left(above):
				walk = above
				above = self.parent(walk)
			return above

	def after(self,p):
		if self.right(p):
			return self._subtree_first_position(self.right(p))
		else:
			walk = p
			above = self.parent(walk)
			while above is not None and walk == self.right(above):
				walk = above
				above = self.parent(walk)
			return above

	def delete(self,p):
		self._validate(p)
		if self.left(p) and self.right(p):
			replacement = self._subtree_last_position(self.left(p))
			self._replace(p,replacement.element())
			p = replacement
		parent = self.parent(p)
		self._delete(p)
		self._rebalance_delete(parent)

	def __delitem__(self,k):
		if not self.is_empty():
			p = self._subtree_search(self.root(),k)
			if k == p.key():
				self.delete(p)
				return
			self._rebalance_access(p)
		raise KeyError('Key Error' + repr(k))



















