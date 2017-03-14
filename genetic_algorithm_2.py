"""
The goal is to find the fastest connection between a number of points
The path must be cyclic
All points must be connected for any cell


fitness=length smaller = better
DNA=sequence of points
"""
import random as r
import math

r.seed(1)

class Point():
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def calc_distance(self, A):
		dx = self.x - A.x
		dy = self.y - A.y
		return math.sqrt(dx**2 + dy**2)

class Traveller():
	def __init__(self, DNA):
		self.DNA = DNA #Points in ordered list
		self.fitness = 0
	def fitness(self):
		distance = 0
		for i, e in enumerate(self.DNA):
			distance += e.calc_distance(self.DNA[i-1])
		self.fitness = distance
		return distance
class Population():
	def __init__(self, size, mut_rate, points):
		self.size=size
		self.mut_rate=mut_rate
		self.points = points
		self.gen=0
		self.d = largest_distance(points)
		self.dens = density(len(points), self.d)
	def create_organism(self):
		# Take random points
		points = list(self.points)
		DNA = []
		for x in range(len(self.points), 0, -1):
			DNA.append(points.pop(int(r.random()*(x))))
		return tuple(DNA)
	def reproduce_organism(self, A, B):
		points = list(self.points)
		pA = list(A.DNA)
		pB = list(B.DNA)
		DNA = []
		for x in range(len(self.points), 0, -1):
			rand = r.random()
			if(rand < self.mut_rate):
				# Get some random point
				point = points[r.random() * (x-1)]
				pA.remove(point)
				pB.remove(point)
				DNA.append(point)
			elif(rand < (0.5 + self.mut_rate/2)):
				point = pA[x]
				pB.remove(point)
				points.remove(point)
				DNA.append(point)
			else:
				point = pB[x]
				pA.remove(point)
				points.remove(point)
				DNA.append(point)
		return tuple(DNA)

	def next_gen(self):
		if(self.gen == 0):
			self.pop = []
			for i in range(self.size):
				DNA = create_organism()
				self.pop.append(Traveller(DNA))
		else:
			for t in self.pop:
				t.fitness()
			self.pop.sort(key=lambda x: x.fitness)
			self.pop = self.pop[:int(self.size/2)]
			pool = []
			for x in self.pop:
				# here I may tweak the constant c
				c = 1 * self.dens
				print(c)
				t = int(x.distance*c)
				for i in range(t):
					pool.append(x)
			for x in range(int(self.size/2), self.size):
				l = len(pool)
				A = pool[int(r.random()*l)]
				B = pool[int(r.random()*l)]
				C = Traveller(reproduce_organism(A,B))
				self.pop.append(C)

		print(self.pop[0], self.pop[0].fitness)
		print(self.gen)
		print()
		self.gen += 1

def largest_distance(points):
	d = 0
	for x in points:
		for y in points:
			d1 = y.calc_distance(x)
			if(d<d1):
				d = d1
	return d
def density(size, d):
	A = math.pi*(d/2)**2
	return size/A


p = [Point(0,0), Point(1,1), Point(-1,-1), Point(2,2)]

pop = Population(10, 0.01, p)



