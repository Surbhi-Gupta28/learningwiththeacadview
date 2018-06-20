#question:1
class Animals:
	def __init__(self,name):
		self.name=name

	def animal_atribute(self,name):
		print(name)

class Tiger(Animals):
	def __init__(self,no_of_tigers):
		self.no=no_of_tigers
		print("Number of tigers = {}".format(no_of_tigers))
t=Tiger(2)
t.animal_atribute("tiger")

#question:2
#output= A B
#        A B

#question 4:
class Shape:
	def __init__(self,ln,br):
		self.ln=ln
		self.br=br

	def area(self):
		ar=self.ln*self.br
		print("area is {}".format(ar))

class Square(Shape):
	def __init__(self):
		self.ln=self.br=int(input())

class Rectangle(Shape):
	def __init__(self):
		self.ln=int(input())
		self.br=int(input())

l=Square()
l.area()

r=Rectangle()
r.area()



















