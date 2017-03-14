"""
This genetic algorithm should match the letters of a string.

genAlg:
population=Strings
DNA=Words
Fitness=CharsCorrect
"""
import random as r
# Initiate random seed to get comparable results
r.seed(1)

class Organism():
	"""These are the individuals of my population, it has a DNA and can calculate its fitness
		The DNA is a string.
		The fitness function compares letters with a target string and adds one to that fitness value for each matching character.
	"""
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
	"""
		Population object contains all relevant Information:
		number of individuals, the target value, mutation rate
	"""

	def __init__(self, n_pop, target, mutation_rate):
		self.n_pop = n_pop
		self.mutation_rate = mutation_rate
		self.target = target
		self.population = []
		self.gen = 0
	def next_gen(self):
		""" Will kill half of the population and recombine the DNA of the leftover
		"""
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

		#Print out the "fittes" aka best matching string
		print(p.population[0].DNA, p.population[0].fitness)
		# Print generation number
		print(p.gen)
		print()
		self.gen += 1
	def breed_new(self, A, B):
		# return new "child" of A and B
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
		#Return random characters of desired length
		DNA = ""
		for i in range(0,n):
			DNA += characters[int(round(r.random()*(len(characters)-1)))]
		return DNA


characters="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,;: -_!?'1234567890=)(/&%ç*+"



target = "To be or not to be, this is the question."
mutation_rate = 0.01
p = Population(100, target, mutation_rate)
p.next_gen()

# run next_gen until string is matched.
while p.population[0].DNA != target:
	p.next_gen()