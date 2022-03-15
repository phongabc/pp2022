class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person
p1.name="John"
p1.age=15
print(p1.name)
print(p1.age)

ef display(self, ob):
			print("Name : ", ob.name)
			print("RollNo : ", ob.rollno)
			print("Marks1 : ", ob.m1)
			print("Marks2 : ", ob.m2)
			print("\n")	
		

	def search(self, rn):
		for i in range(ls.__len__()):
			if(ls[i].rollno == rn):
				return i	
							
	def delete(self, rn):
		i = obj.search(rn)
		del ls[i]

	def update(self, rn, No):
		i = obj.search(rn)
		roll = No
		ls[i].rollno = roll;