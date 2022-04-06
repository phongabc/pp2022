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

def GPA(self):
        while True:
            try:
                stuid = int(input(f"Enter student id you want to calculate GPA: "))
                while sid <= 0:
                    stuid = int(input(f"ID must be positive. Enter again student id: "))
                
                check = 0
                for mark in self.marks:
                    if check == (len(self.marks) - 1):
                        print(f"Error. Student id {stuid} not existed!!!")
                        break
                    elif stuid != mark.get_student().get_stuid():
                        check = check + 1
                    else:
                        print("Student id is existed!")
            except:
                print("ID must be positive. Enter again student id!")
            else:
                break

        list_score = np.array([])
        list_credit = np.array([])

        check = 0
        for mark in self.marks:
            if stuid == mark.get_student().get_stuid():
                list_score = np.append(list_score, mark.get_mark())
                list_credit = np.append(list_credit, mark.get_course().get_credit())

        gpa = np.dot(list_score, list_credit) / np.sum(list_credit)

        for student in self.students:
            if stuid == student.get_stuid():
                student.set_gpa(gpa)

    def sort_list_of_student(self):
        if len(self.students) == 0:
            print("List of student information is empty!") 
        else:
            data_type = [('stuid', 'S30'), ('stuname', 'S30'), ('gpa', float)]
            new_students = []
            for student in self.students:
                new_student_infor = (student.get_stuid(), student.get_stuname(), student.get_gpa())
                new_students.append(new_student_infor)
            sorting_new_students = np.array(new_students, dtype=data_type)
            sorted_list = np.sort(sorting_new_students, order = 'gpa')
            print(sorted_list)

    

    def list_of_mark(self):
        if len(self.marks) == 0:
            print("The mark list is empty!")
        else:
            while True:
                try:
                    courseid = int(input("Enter id of course you want to list marks: "))
                    while courseid <= 0:
                        courseid = int(input("Course id must be positive.Enter  again course id you want to list marks: "))
                     
                    check = 0
                    for mark in self.marks:
                        if check == (len(self.marks) - 1):
                            print("Error")
                            break
                        elif courseid != mark.get_course().get_courseid():
                            check = check + 1
                        else:
                            print("Course id is existed!")
                except:
                    print("Course id must be positive.Enter again course id you want to list marks!!!")
                else:
                    break
            for mark in self.marks:
                if courseid == mark.get_course().get_courseid():
                    print(mark.get_student().get_stuname(), mark.get_course().get_coursename(), mark.get_mark(), sep="-")
