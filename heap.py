#coding:utf-8
from collections import deque

class Heap:

	def __init__(self,l):
		self.l = l

	def swap(self,i,j):
		self.l[i],self.l[j] = self.l[j],self.l[i]

	def max_heap(self,a,b):
		temp = self.l[a]
		i = a
		j = 2 * i
		while j <= b:
			if (j<b) and (self.l[j] < self.l[j+1]):
				j += 1
			if(temp < self.l[j]):
				self.l[i] = self.l[j]
				i = j
				j  = 2 * i 
			else:
				break
		self.l[i] = temp

	def sort(self):
		length = len(self.l) - 1
		nodes_num = length // 2
#实现大根堆		
		for i in range(nodes_num):
			self.max_heap(nodes_num-i,length)
#在实现了大根堆的基础上实现小根堆		
		for i in range(length - 1):
			self.swap(1,length - i)
			self.max_heap(1,length - i - 1)
		return [self.l[i] for i in range(1,len(self.l))]

test_heap = deque([40,30,50,70,100,10,60])
test_heap.appendleft(0)
heap = Heap(test_heap)
result = heap.sort()
print(result)












