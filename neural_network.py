from random import random

class Perceptron():
	"""docstring for Perceptron"""
	def __init__(self, n):
		self.weights = []
		self.learn_const = 0.01
		for i in range(0,n):
			self.weights.append(random()*2-1)
	def feedforward(self, inputs):
		sum = 0.0
		for i, e in enumerate(inputs):
			sum += self.weights[i]*e

		return self.activate(sum)

	def activate(self, sum):
		if(sum > 0):
			return 1
		else:
			return -1

	def train(self, inputs, desired):
		guess = self.feedforward(inputs)
		error = float(desired) - float(guess)
		print(guess, error)
		for i, e in enumerate(self.weights):
			e += self.learn_const*error*inputs[i]
class Trainer():
	"""docstring for Trainer"""
	def __init__(self, x,y,a):
		self.inputs = [x,y,1]
		self.answer = a

def f(x):
	return 2*x + 1
def findAns(x,y):
	if(f(x)>y):
		return 1
	else:
		return -1
def makeSamplePoints(n):
	t = []
	for e in range(0,n):
		x = random()*200-100
		y = random()*200-100
		a = findAns(x,y)
		t.append(Trainer(x,y,a))
	return t
def trainPerc(p, t):
	for e in t:
		p.train(e.inputs, e.answer)

p = Perceptron(3)
t = makeSamplePoints(2000)

trainPerc(p,t)

print(p.feedforward([-10,0,1]))
print(p.feedforward([-10,0,1]))