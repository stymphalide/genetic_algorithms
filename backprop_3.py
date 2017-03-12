import numpy as np


def nonlin(x,deriv=False):
	if(deriv):
		return x*(1-x)
	else:
		return 1/(1+np.exp(-x))
X = np.array([
	[0],
	[0.5],
	[1]
	])
y = np.array([[0,0,1]]).T
input_size = X.shape[1]
sample_length = X.shape[0]
np.random.seed(1)

#Consider the bias as well
syn0 = 2*np.random.random((input_size, sample_length)) -1 #Get values between 1 and -1
syn1 = 2*np.random.random((sample_length,1)) - 1 #Get values between 1 and -1

for j in range(0,100000):
	#Feedforward
	a = np.round(np.random.random((3,1))*3)/3
	b = a.T

	X = a
	y = a
	bias = np.ones((sample_length,1))
	l0 = X
	l1 = nonlin(np.dot(l0, syn0))
	l2 = nonlin(np.dot(l1,syn1))

	#Backpropagation
	#By how much did we miss the desired value
	l2_error = y - l2
	if((j % 10000) == 0):
		print("Error: " + str(np.mean(np.abs(l2_error))))
	# In what direction is the target value?
	delta_l2 = l2_error * nonlin(l2,True)
	# What part of the error comes from the layer above?
	l1_error = np.dot(delta_l2, syn1.T)
	# How much do we have to change l1
	delta_l1 = l1_error * nonlin(l1, True)
	
	syn1 += np.dot(l1.T, delta_l2)
	syn0 += np.dot(l0.T, delta_l1)


print("After Training:")
print(X)
print(l2)