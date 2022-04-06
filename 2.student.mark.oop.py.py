class student
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = {}

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_dob(self):
        return self.dob

    def get_mark(self):
        return self.marks

    def set_id(self, _id):
        self.id = _id

    def set_name(self, name):
        self.name = name

    def set_dob(self, dob):
        self.dob = dob

    def set_mark(self, course, mark):
        self.marks.update({course: mark})

    def displayStudent(self):
        print("Student ID: " + self.id)
        print("Student name: " + self.name)
        print("Student DoB: " + self.dob)
        print("-------")

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

def numOfStudent():
    while True:
        try:
            std_num = int(input("Enter number of student in the class: "))
            print("-------")
            return std_num
        except ValueError:
            print("Invalid number.")


def studentInfo():
    std_id = input("Enter student ID: ")
    std_name = input("Enter student name: ")
    std_dob = input("Enter student date of birth: ")
    print("-------")
    return std_id, std_name, std_dob


def numOfCourse():
    while True:
        try:
            course_num = int(input("Enter number of courses: "))
            print("-------")
            return course_num
        except ValueError:
            print("Err: Invalid number.")


def courseInfo():
    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    print("-------")
    return course_id, course_name


while True:
    print(f'''\n
    0. Exit
    1. Add student
    2. Upload information
    3. Delete student
    4. Watch 
    5. Watch information
    6. Reseach student
    7. Number student 
    ''')
    select = input("select function:  ")

    if str(select).isdigit():
        select = int(select)
        if select == 0:
            break
        elif select == 1:
            id = input("Input ID:  ")
            name = input("Input name:  ")
            sv = Student(id , name)
            ds.append(sv)

        elif select == 2:
            id = input("Input Id upload:  ")
            for i in ds:
                if i.get_id() == id:
                    i.set_Name( input("Input name new:  ") )
                    i.show_info()

        elif select == 4:
            if len(ds) == 0:
                print("\n There are currently no students. Please add new students to the list !")
            else:
                print(f"\n Have {len(ds)} Student ")
                for i in ds:
                    i.show_info()

        elif select == 3:
            id = input("Input Id delete :  ")
            for i in ds:
                if i.get_id() == id:
                    ds.remove(i)
                    print(" Complete ")
                    continue

        elif select == 5:
            id = input("Input Id student :  ")
            for i in ds:
                if i.get_id() == id:
                    i.show_info()
                    continue

        elif select == 6:
            ten = input("Input Id :  ")
            for i in ds:
                if i.get_Name() == name:
                    i.show_info()

        elif select == 7:
            print(f"\nHave { len(ds) } student \n")
    else:
        print("\nInput number !")


