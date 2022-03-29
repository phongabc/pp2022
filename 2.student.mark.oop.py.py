class Student:

    count = 0

    def __init__(self , id , name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = {}
        Student.count += 1

     def set_id(self , id):
         self.id = id

    def get_id(self):
        return self.id

    def set_Name(self, name):
        self.name = name

    def get_Name(self):
        return self.name

    def get_dob(self):
        return self.dob

    def set_dob(self, dob):
        self.dob = dob

    def get_mark(self):
        return self.marks

    def set_mark(self, course, mark):
        self.marks.update({course: mark})


def display(self, ob):
            print("Name : ", ob.name)
            print("dob : ", ob.dob)
            print("ID : ", ob.ID)
            print("Mark : ", ob.m)
            print("\n") 

def displayMark(self, course):
        print(self.name + "'s mark: " + str(self.marks.get(course)))
        
class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def displayCourse(self):
        print("Course ID: " + self.id)
        print("Course name: " + self.name)
        print("-------")