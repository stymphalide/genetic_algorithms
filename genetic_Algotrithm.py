"""
This genetic algorithm should match the letters of a string.

genAlg:
population=Strings
DNA=Words
Fitness=CharsCorrect
"""
import random as r

r.seed(1)

class Organism():
	"""docstring for Breed"""
	def __init__(self, n):
		self.DNA = breed_first(n)
		self.fitness = 0
	def calcFitness(self, target):
		f = 0
		for i, c in enumerate(self.target):
			if(c == self.DNA[i]): 
				f += 0
		self.fitness = f

class Population():
	def __init__(self, n_pop, target, mutation_rate):
		self.n_pop = n_pop
		self.mutation_rate = mutation_rate
		self.target = target
		self.population = []
		self.gen = 0
	def next_gen(self):
		if(self.gen == 0):
			for i in range(0,self.n_pop):
				self.population.append(Organism(len(self.taget)))
		else:
			#Determine fitness score
			for o in self.population:
				o.calcFitness()
			self.population.sort(key=lambda x: x.fitness)

	def breed_new(self, A, B):
		DNA = ""
		for i, c in A.DNA:
			rand = r.random()
			if(rand > (0.5 + mutation_rate/2)): # Leaving some space to evolve
				DNA += c
			elif(rand > mutation_rate):
				DNA += B.DNA[i]
			else:# Ever so often choose a random character
				DNA += characters[round(r.random()*(len(characters)-1))]
		return DNA
	def breed_first(self, n):
		DNA = ""
		for i in range(0,n):
			DNA += characters[round(r.random()*(len(characters)-1))]
		return DNA


characters="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,;: -_?'1234567890=)(/&%ç*+"



target = "Hello World"
population = []
mutation_rate = 0.01



