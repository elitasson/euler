# -*- coding: utf-8 -*-
"""
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by moving left, right, up, and down, is indicated in bold red and is equal to 2297.

131,673,234,103,18
201,96,342,965,150
630,803,746,422,11
537,699,497,121,956
805,732,524,37,331

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by moving left, right, up, and down.
"""

import sys

# node class
class Node:
	def __init__(self, x, y, weight):
		self.weight = int(weight)
		self.cost = 10*100000
		self.x = int(x)
		self.y = int(y)
		self.originateX = -1
		self.originateY = -1
		self.added = False
		self.done = False
		self.nodes = []


	def addNode(self, node):
		self.nodes.append(node)

	def __repr__(self):
		return "Y: %s, X: %s\nweight: %d, cost: %d, done: %s\noriginY: %d, originX: %d\n\n" % (self.y, self.x, self.weight, self.cost, self.done, self.originateY, self.originateX)


def orderO(o):
	return o.sort(key = lambda x: x.cost)


def checkNextNode(nextNode, currentNode, o):
	if nextNode.cost > currentNode.cost + nextNode.weight:
		nextNode.cost = currentNode.cost + nextNode.weight
		nextNode.originateX = currentNode.x
		nextNode.originateY = currentNode.y

	if not nextNode.added:
		nextNode.added = True
		o.append(nextNode)	


# initiate
#fh = open('test.txt')
fh = open('p083_matrix.txt')
arr = []
arr2 = []

for y, line in enumerate(fh):
	l = []
	for x, weight in enumerate(line.replace('\n', '').split(',')):
		l.append(Node(x, y, weight))
	arr.append(l)

# open nodes (un done)
o = []

# init first node
arr[0][0].cost = arr[0][0].weight
arr[0][0].added = True
o.append(arr[0][0])

while o:
	node = o.pop(0)

	if node.x == len(arr)-1 and node.y == len(arr)-1:
		o = []
		continue

	# right
	if node.x+1 < len(arr):
		nextNode = arr[node.y][node.x+1]
		checkNextNode(nextNode, node, o)

	# left
	if node.x-1 >= 0:
		nextNode = arr[node.y][node.x-1]
		checkNextNode(nextNode, node, o)

	# top
	if node.y+1 < len(arr):
		nextNode = arr[node.y+1][node.x]
		checkNextNode(nextNode, node, o)

	# bottom
	if node.y-1 >= 0:
		nextNode = arr[node.y-1][node.x]
		checkNextNode(nextNode, node, o)

	orderO(o)

# print bottom right node
print(arr[len(arr)-1][len(arr)-1])