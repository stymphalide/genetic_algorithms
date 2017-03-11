import numpy as np


def nonlin(x,deriv=False):
	if(deriv):
		return x*(1-x)
	else:
		return 1/(1+np.exp(-x))


X = np.array([
	[0,0,1],
	[0,1,1],
	[1,1,0],
	[0,0,0]
	])
y = np.array([[0,1,1,0]]).T

np.random.seed(1)

syn0 = 2*np.random.random((3,1)) -1 #Get values between 1 and -1


for j in range(0,10000):
	l0 = X
	l1 = nonlin(np.dot(l0,syn0))
	l1_error = y -l1
	delta_l1 = l1_error * nonlin(l1, True)
	syn0 += np.dot(l0.T, delta_l1)
	if((j % 1000) == 0):
		print("Error: " + str(np.mean(np.abs(l1_error))))

print("After Training:")
print(nonlin(np.dot(X,syn0)))