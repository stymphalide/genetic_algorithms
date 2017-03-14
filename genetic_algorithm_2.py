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
		self.dis = 0
	def fitness(self):
		distance = 0
		for i, e in enumerate(self.DNA):
			distance += e.calc_distance(self.DNA[i-1])
		self.dis = distance
		return distance
	def print_travel(self):
		for p in self.DNA:
			print(p.x, p.y)
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
		for x in range(len(self.points)-1, -1, -1):
			rand = r.random()
			if(rand < self.mut_rate):
				# Get some random point
				point = points[int(r.random() * (x-1))]
			elif(rand < (0.5 + self.mut_rate/2)):
				point = pA[x]
			else:
				point = pB[x]
			pA.remove(point)
			pB.remove(point)
			points.remove(point)
			DNA.append(point)
		return tuple(DNA)

	def next_gen(self):
		if(self.gen == 0):
			self.pop = []
			for i in range(self.size):
				DNA = self.create_organism()
				self.pop.append(Traveller(DNA))
		else:
			for t in self.pop:
				t.fitness()
			self.pop.sort(key=lambda x: x.dis)
			self.pop = self.pop[:int(self.size/2)]
			pool = []
			for x in self.pop:
				# here I may tweak the constant c
				c = 10 * self.dens
				#print(c)
				t = int(x.dis*c)
				#print(t)
				for i in range(t):
					pool.append(x)
			for x in range(int(self.size/2), self.size):
				l = len(pool)
				A = pool[int(r.random()*l)]
				B = pool[int(r.random()*l)]
				C = Traveller(self.reproduce_organism(A,B))
				self.pop.append(C)

		#print(self.pop[0], self.pop[0].dis)
		#print(self.gen)
		#print()
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


p = [ Point(0,0), 
	  Point(1,1), 
	  Point(-1,-1), 
	  Point(2,2), 
	  Point(-5,10), 
	  Point(10,10),
	  Point(-10,10),
	  Point(-4,3)
	 ]

pop = Population(10, 0.01, p)


pop.next_gen()
pop.pop[0].print_travel()
for i in range(100):
	pop.next_gen()
	pop.next_gen()

pop.pop[0].print_travel()