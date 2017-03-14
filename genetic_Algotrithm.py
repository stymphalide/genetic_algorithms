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
	def __init__(self, DNA):
		self.DNA = DNA
		self.fitness = 0
	def calcFitness(self, target):
		self.fitness = 0
		for i, c in enumerate(target):
			if(c == self.DNA[i]): 
				self.fitness += 1
		return self.fitness

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
				self.population.append(Organism(self.breed_first(len(self.target))))
		else:
			#Determine fitness score
			pool = []
			for o in self.population:
				f = o.calcFitness(self.target)
				for i in range(0,f):
					pool.append(o)
			# Sort the population according to their fitness
			self.population.sort(key=lambda x: x.fitness, reverse = True)
			# Kill half of the population (Can be improved)
			self.population = self.population[:int(round(self.n_pop/2))]
			# Choose two random objects from pool
			l = len(pool) - 1
			for i in range(0,round(self.n_pop/2)):
				A = pool[int(r.random() * l)]
				B = pool[int(r.random() * l)]
				new_DNA = self.breed_new(A,B)
				new_org = Organism(new_DNA)
				self.population.append(new_org)
		print(p.population[0].DNA, p.population[0].fitness)
		print(p.gen)
		print()
		self.gen += 1
	def breed_new(self, A, B):
		DNA = ""
		for i, c in enumerate(A.DNA):
			rand = r.random()
			if(rand > (0.5 + mutation_rate/2)): # Leaving some space to evolve
				DNA += c
			elif(rand > mutation_rate):
				DNA += B.DNA[i]
			else:# Ever so often choose a random character
				DNA += characters[int(round(r.random()*(len(characters)-1)))]
		return DNA
	def breed_first(self, n):
		DNA = ""
		for i in range(0,n):
			DNA += characters[int(round(r.random()*(len(characters)-1)))]
		return DNA


characters="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,;: -_!?'1234567890=)(/&%ç*+"



target = "To be or not to be, this is the question."
mutation_rate = 0.01
p = Population(100, target, mutation_rate)
p.next_gen()
while p.population[0].DNA != target:
	p.next_gen()