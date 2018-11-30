from Queue import PriorityQueue
class Node:
	def __init__(self, key, value, upPointer, downPointer):
		self.upPointer = upPointer
		self.downPointer = downPointer
		self.key = key
		self.value = value

	def __repr__(self):
		return "Node{"+"freq="+str(self.getKey())+", char="+str(self.getValue())+"}"
	def getKey(self):
		return self.key
	def setKey(self, key):
		self.key = key
	def getValue(self):
		return self.value
	def setValue(self, newVal):
		self.value = newVal
	def getUp(self):
		return self.upPointer
	def getDown(self):
		return self.downPointer
	def isLeaf(self):
		return self.downPointer == None and self.upPointer == None
	def __cmp__(self, other):
		if(self.getKey()<other.getKey()):
			return -1
		elif(self.getKey()==other.getKey()):
			return 0
		return 1
class Huffman():
	def __init__(self, string):
		self.root = None
		self.queue = PriorityQueue()
		arr = {}
		for char in string:
			if(char in arr):
				arr[char] += 1
			else:
				arr[char] = 1
		for key in arr:
			self.queue.put(Node(arr[key], key, None, None))
		self.construct()
	def __repr__(self):
		"[" + self.toString(self.root) + "]"
	def toString(self, root):
		print(self.root)
		if(root.isLeaf()):
			return str(root)
		else:
			if(root.getUp()!=None and root.getDown!=None):
				return str(root) + self.toString(root.getUp()) + self.toString(root.getDown())
			elif(root.getUp!=None):
				return str(root) + self.toString(root.getUp())
			else:
				return str(root) + self.toString(root.getDown())

	def construct(self):
		while(self.queue.qsize()!=1):			
			first = self.queue.get()
			print(first)

			if(self.queue.qsize()!=0):
				second = self.queue.get()
			else:
				second = Node(0, "-1", None, None)
			newElem = Node(first.getKey()+second.getKey(), "*", first, second)
			self.queue.put(newElem)
		self.root = self.queue.get()
huffman = Huffman("hello there I am vaughns")
print(huffman)
