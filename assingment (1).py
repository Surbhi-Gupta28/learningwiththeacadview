#question:1
class Circle:
	def __init__(self,x):
		self.radius=x

	def getarea(self,radius):
		area=3.14*radius*radius
		print(area)

	def getcircumference(self,r):
		rad=2*3.14*r
		print(rad)

v=Circle(10)
v.getarea(10)
#question:2
class Student:
	def __init__(self,name,rollno):
		self.name=name
		self.rollno=rollno

	def printdetails(self):
		print(self.name)
		print(self.rollno)

c=Student("Surbhi",271)
c.printdetails()

#question:3
class Temprature:
	def __init__(self,temp):
		self.temp=temp

	def convertFahrenhiet(self):
		print((self.temp*1.8)+32)

	def convertCelcius(self):
		print((self.temp-32)/1.8)

a=Temprature(32)
a.convertCelcius()
a.convertFahrenhiet()
\
#question:4
class MovieDetails:

	def __init__(self,name,artistname,YOR,rat):
		self.name=name
		self.artistname=artistname
		self.YOR=YOR
		self.rat=rat

	def Display(self):
		print(self.name)
		print(self.artistname)
		print(self.YOR)
		print(self.rat)

	def update(self,name1,artistname1,YOR1,rat1):
		self.name=name1
		self.artistname=artistname1
		self.YOR=YOR1
		self.rat=rat1

w=MovieDetails("kick","salman",2016,4)
w.Display()

#Question:5
class Expenditure:
	def __init__(self,expend,sav):
		self.expenditure=expend
		self.saving=sav

	def view(self):
		print("the Expenditure is {} and savings are {}".format(self.expenditure,self.saving))

	def TotalSalary(self):
		self.tot=self.expenditure+self.saving
		print("total salary is {}".format(self.tot))

	def DisplaySalary(self):
		print(self.tot)

emp1=Expenditure(10000,5000)

emp1.view()
emp1.TotalSalary()
emp1.DisplaySalary()

















