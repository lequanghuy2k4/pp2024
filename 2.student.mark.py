class Students:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

class Courses:
    def __init__(self, id ,name):
        self.id = id
        self.name = name

class Marks:
    def __init__(self, student, course, mark):
        self.student = student
        self.course = course
        self.mark = mark

class StudentMark:
    def __init__(self) :
        self.students = []
        self.courses= []
        self.marks = []

    def input_students(self):
        number_student = int(input("Enter number of students: "))
        for _ in range(number_student):
            id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student's date of birth in DD-MM-YYYY: ")
            self.students.append(Students(id,name,dob))

    def input_courses(self):
        number_course = int(input("Enter number of course: "))
        for _ in range(number_course):
            id = input("Enter course ID: ")
            name = input("Enter course name:")
            self.courses.append(Courses(id,name))

    def input_marks(self):
        for course in self.courses:
            print(f"Enter mark for course {course.name}")
            for student in self.students:
                mark = float(input(f"Enter the mark for student {student.name} in course {course.id}:"))
                self.marks.append(StudentMark(student,course,mark))

    def list_courses(self):
        print("Courses: ")
        for course in self.courses:
            print(f"ID: {course.id}. \nName {course.name}")

    def list_students(self):
        print("Student: ")
        for student in self.students:
            print(f"ID: {student.id}. \nName {student.name}. \nDate of Birth {student.dob}")

    def show_marks(self):
        course_id = input("Enter the ID of the course to see the mark: ")
        for mark in self.marks:
            if mark.course.id == course_id:
                print(f"Student {mark.student.name} gets {mark.mark} in course {mark.course.id}")
            else:
                print(f"No marks entered for student {mark.student.name} in course {mark.course.id}")
                
school = StudentMark()
school.input_students()
school.input_courses()
school.input_marks()
school.list_courses()
school.list_students()
school.show_marks()
        
        

    