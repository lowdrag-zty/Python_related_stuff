
class ArrayStack:

	def __init__(self):
		self._data = []

	def __len__(self):
		return len(self._data)

	def is_empty(self):
		return len(self._data) == 0

	def push(self,e):
		self._data.append(e)

	def top(self):
		if(self.is_empty()):
			raise Exception('The stack is empty,pal')
		else:
			return self._data[-1]

	def pop(self):
		if(self.is_empty()):
			raise Exception('The stack is empty, pal')
		else:
			return self._data.pop()

	
def reverse(a):
	array = ArrayStack()  
	for i in a:
		array.push(i)
		rev = ''
	for i in range(len(a)):
		rev += array.pop()
	return rev

def is_palin(n):
	n1 = reverse(str(n))
	if(n1 == str(n)):
		return True
	else:
		return False

def is_matched(a):
	left = '({['
	right = ')}]'
	array = ArrayStack()

	for i in a:
		if(i in left):
			array.push(i)
		elif(i in right):
			if(array.is_empty()):
				return False
			if(right.index(i) != left.index(array.pop())):
				return False
	return array.is_empty()


def revfile(filename):
	S = ArrayStack()
	original = open(filename)

	for line in original:
		S.push(line.rstrip('\n'))
	original.close()

	output = open(filename,'w')
	while not S.is_empty():
		output.write(S.pop() + '\n')
	output.close()


#P238--Matching tags in a markup language
def is_matched_html(raw):
	S = ArrayStack()
	j = raw.find('<')
	while(j != -1):
		k = raw.find('>',j+1)
		if(k==-1):
			return False
		else:
			tag = raw[j+1:k]

		if not tag.startswith('/'):
			S.push(tag)

		else:
			if(S.is_empty()):
				return False
			if(tag[1:]!=S.pop()):
				return False
		j = raw.find('<',k+1)
	return S.is_empty()























 
 
