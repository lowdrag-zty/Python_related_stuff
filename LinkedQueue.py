class LinkedQueue:

	class _Node:

		def __init__(self,element,next):
			self._element = element
			self._next = next

	
	def __init__(self):
		self._head = None
		self._tail = None
		self._size = 0


	def __len__(self):
		return self._size

	def is_empty(self):
		return self._size == 0

	def first(self):
		if(self.is_empty()):
			raise Exception('The queue is empty')
		return self._head._element

	def dequeue(self):
		if self.is_empty():
			raise Exception('The queue is empty')
		anwser = self._head._element
		self._head = self._head._next
		self._size -= 1
		if(self.is_empty()):
			self._tail = None
		return anwser

	def enqueue(self,e):
		newest = self._Node(e,None)
		if(self.is_empty()):
			self._head = newest
		else:
			self._tail._next = newest
		self._tail = newest
		self._size += 1


def finding(n):
	A = LinkedQueue()
	B = LinkedQueue()
	C = LinkedQueue()
	A.enqueue(3)
	B.enqueue(4)
	C.enqueue(1)
	count = 1
	k = n
	while(count<=k):
		if(A.first()<B.first()):
			A.enqueue(A.first()*2+1)
			B.enqueue(A.first()*3+1)
			anwser = A.dequeue()
			C.enqueue(anwser)
			count += 1
		else:
			A.enqueue(B.first()*2+1)
			B.enqueue(B.first()*3+1)
			anw = B.dequeue()
			C.enqueue(anw)
			count += 1
		
	for i in range(0,n-1):
		C.dequeue()
	return C.first()























