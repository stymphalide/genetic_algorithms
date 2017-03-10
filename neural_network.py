from random import randrange

class Perceptron():
	"""docstring for Perceptron"""
	def __init__(self, n):
		self.weights = []
		for i in range(0,n):
			self.weights.append(randrange(-1,1))
	def feedforward(self, inputs):
		sum = 0.0
		for i, e in enumerate(inputs):
			sum += self.weights[i]*e

		return activate(sum)

def activate(sum):
	if(sum> 0):
		return 1
	else:
		return -1

p = Perceptron(3)

point = [50,-12,1]

result = p.feedforward(point)
print(result)