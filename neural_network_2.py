#neural_network_2.py
from random import random
class Neuron():
	"""docstring for Neuron"""
	def __init__(self, x,y):
		self.location = [x,y]
		self.connections = []
		self.sum = 0
	def addConnection(self, c):
		connections.append(c)
	def feedforward(self, input):
		self.sum += input
		if(self.sum >1):
			self.fire()
		else:
			self.sum = 0
	def fire(self):
		for c in self.connections:
			c.feedforward(sum)
class Network():
	def __init__(self, x,y):
		self.location = [x,y]
		self.neurons = []
	def addNeuron(self, n):
		self.neurons.append(n)
	def connect(self, a,b):
		c = Connection(a,b, random())
		a.addConnection(c)
	def feedforward(self, input):
		start = self.neurons[0]
		start.feedforward(input)
class Connection():
	def __init__(self, a,b w):
		self.weight = w
		self.a = a
		self.b = b
	def feedforward(self, val):
		b.feedforward(self.weight*val)


