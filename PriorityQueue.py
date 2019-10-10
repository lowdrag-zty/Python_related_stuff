


################################################

class _DoublyLinkedBase:
	class _Node:
		def __init__(self,element,next):
			self._element = element
			self._next = next
	def __init__(self):
		self._header = self._Node(None,None,None)
		self._trailer = self._Node(None,None,None)
		self._header._next = self._trailer
		self._trailer._prev = self._header
		self._size = 0

	def __len__(self):
		return self._size

	def is_empty(self):
		return self._size == 0

	def _insert_between(self,e,predecessor,successor):
		newest = self._Node(e,predecessor,successor)
		predecessor._next = newest
		successor._prev = newest
		self._size += 1
		return newest

######################################################

class PositionalList(_DoublyLinkedBase):
	class Position:
		def __init__(self,container,node):
			self._container = container
			self._node = node

		def element(self):
			return self._node._element

	def _validate(self,p):
		return p._node

	def _make_position(self,node):
		if node is self._header or node is self._trailer:
			return None
		else:
			return self.Position(self,node)

	def first(self):
		return self._make_position(self._header._next)

	def last(self):
		return self._make_position(self._trailer._prev)

	def before(self,p):
		node = self._validate(p)
		return self._make_position(node._prev)

	def after(self,p):
		node = self._validate(p)
		return self._make_position(node._next)

	def _insert_between(self,e,predecessor,successor):
		node = super()._insert_between(e,predecessor,successor)
		return self._make_position(node)

	def add_first(self,e):
		return self._insert_between(e,self._header,self._header._next)

	def add_last(self,e):
		return self._insert_between(e,self._trailer._prev,self._trailer)

	def add_before(self,p,e):
		original = self._validate(p)
		return self._insert_between(e,original._prev,original)

	def add_after(self,p,e):
		original = self._validate(p)
		return self._insert_between(e,original,original._next)

##############################################################

class PriorityQueueBase:
	class _Item:
		__slots__ = '_key','_value'

		def __init__(self,k,v):
			self._key = k
			self._value = v

		def __It__(self,other):
			return self._key < other._key

		def is_empty(self):
			return len(self) == 0

############################################################

class UnsortedPriorityQueue(PriorityQueueBase):

	def _find_min(self):
		small = self._data.first()
		walk = self._data.after(small)
		while walk is not None:
			if walk.element() < small.element:
				small = walk
				walk = self._data.after(walk)
		return small

	def __init__(self):
		self._data = PositionalList()

	def __len__(self):
		return len(self._data)

	def add(self,key,value):
		self._data.add_last(self._Item(key,value))

	def min(self):
		p = self._find_min()
		item = p.element
		return (item._key,item._value)

######################################################

class SortedPriorityQueue(PriorityQueueBase):

	def __init__(self):
		self._data = PositionalList()

	def __len__(self):
		return len(self._data)

	def add(self, key, value):
		newest = self. Item(key, value)
		walk = self. data.last( )
		while walk is not None and newest < walk.element():
  			walk = self. data.before(walk) 
  		if walk is None:
			self. data.add_first(newest) 
		else:
			self. data.add_after(walk, newest)

	def min(self):
		if self.is_empty():
			raise Empty( 'Priority queue is empty. ') 
		p = self. data.first()
		item = p.element()
		return (item. key, item. value)

###################################################

class HeapPriorityQueue(PriorityQueueBase):
	

	

	def _parent(self,j):
		return (j-1) // 2

	def _left(self,j):
		return 2*j + 1

	def _right(self,j):
		return (2*j + 2)

	def _has_left(self,j):
		return self._left(j) < len(self._data)

	def _has_right(self,j):
		return self._right(j) < len(self._data)

	def _swap(self,i,j):
		self._data[i],self._data[j] = self._data[j],self._data[i]

	def _upheap(self,j):
		parent = self._parent(j)
		if j>0 and self._data[j]<self._data[parent]:
			self._swap(j,parent)
			self._upheap(parent)

	def __init__(self):
		self._data = []

	def __len__(self):
		return len(self._data)

	def add(self,key,value):
		self._data.append(self._Item(key,value))
		self._upheap(len(self._data)-1)
	







