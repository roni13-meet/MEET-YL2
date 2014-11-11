class animal():
	def __init__(self, name, age):
		self.age = age
		self.name = name
	def sleep(self):
		print str(self.name) + " of " + str(self.age) + " is sleeping"
	def eat(self, food):
		print str(self.name) + " of " + str(self.age) + " is eating " + food

class bird(animal):
	def __init__(self, name, age, wingscolor):
		animal.__init__(self, name, age)
		self.wingscolor = wingscolor
	def fly(self):
		print str(self.name) + " of " + str(self.age) + "'s wings are " + self.wingscolor

x = animal("meet", 11)
x.sleep()
x.eat("apple")
y = animal("cat", 2)
y.sleep()
y.eat("pizza")
z = bird("bird", 4, "red")
z.fly()


	

