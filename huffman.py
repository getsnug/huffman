from Queue import PriorityQueue
import os
class Node:
	def __init__(self, key, value, upPointer, downPointer):
		self.upPointer = upPointer
		self.downPointer = downPointer
		self.key = key
		self.value = value
		self.depth = 0

	def __repr__(self):
		return str(self.getKey())+":"+str(self.getValue())
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
		if(self is not None and other is not None):
			if(self.getKey()<other.getKey()):
				return -1
			elif(self.getKey()==other.getKey()):
				return 0
			return 1
		return 1


class Huffman():
	def __init__(self, string):
		self.root = None
		self.queue = PriorityQueue()
		self.myArr = []
		arr = {}
		for char in string:
			if(char in arr):
				arr[char] += 1
			else:
				arr[char] = 1
		for key in arr:
			self.queue.put(Node(arr[key], key, None, None))
		self.construct()
	def setDepth(self):
		self.setDepthRec(self.root, 1)
	def setDepthRec(self, root, size):
		if(root.isLeaf()):
			root.depth = size
			return 1
		else:
			size += 1
			if(root.getUp()!=None and root.getDown!=None):
				return self.setDepthRec(root.getUp(), size) + self.setDepthRec(root.getDown(), size)
			elif(root.getUp!=None):
				return self.setDepthRec(root.getUp(), size)
			else:
				return self.setDepthRec(root.getDown(), size)

	def __str__(self):
		return str(self.myArr[::-1])

	def construct(self):
		while(self.queue.qsize()!=1):			
			first = self.queue.get()
			if(self.queue.qsize()!=0):
				second = self.queue.get()
			else:
				second = Node(0, "-1", None, None)
			newElem = Node(first.getKey()+second.getKey(), "*", first, second)
			self.myArr.append(first)
			self.myArr.append(second)
			self.queue.put(newElem)
		self.root = self.queue.get()
		self.myArr.append(self.root)
		self.setDepth()
	def compressedChar(self, root, char, path):
		if(root.isLeaf()):
			if(char==root.getValue()):
				return path
			else:
				return ""
		else:
			return self.compressedChar(root.getUp(), char, path+"1")+self.compressedChar(root.getDown(), char, path+"0")





filename = "txt.txt"
encodedText = ""
file = open(filename, "r")
lines = file.read()
lines.replace("\n", "\\n")
huffman = Huffman(lines)
for char in lines:
	encodedText+=huffman.compressedChar(huffman.root, char, "")
tempStr = str(huffman)
encodedTree = ''.join(format(ord(x), 'b') for x in tempStr)
print("Tree:")
print(str(huffman))
print("Encoded Tree:")
print(encodedTree)
print("Encoded Text:")
print(encodedText)
print("Compression Ratio:")
print((len(lines)*32.0)/(len(encodedText)+len(encodedTree)))




