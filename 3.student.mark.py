import math
import numpy as np

class Students:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

class Courses:
    def __init__(self, id ,name, credits):
        self.id = id
        self.name = name
        self.credits = credits

class Marks:
    def __init__(self, student, course, mark):
        self.student = student
        self.course = course
        self.mark = mark

class StudentMark:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []

    def input_students(self):
        number_student = int(input("Enter number of students: "))
        for _ in range(number_student):
            id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student's date of birth in DD-MM-YYYY: ")
            self.students.append(Students(id, name, dob))

    def input_courses(self):
        number_course = int(input("Enter number of courses: "))
        for _ in range(number_course):
            id = input("Enter course ID: ")
            name = input("Enter course name: ")
            credits = int(input("Enter course credits: "))
            self.courses.append(Courses(id, name, credits))

    def input_marks(self):
        for course in self.courses:
            print(f"Enter marks for course {course.name}")
            for student in self.students:
                mark = float(input(f"Enter the mark for student {student.name} in course {course.id}:"))
                mark = math.floor(mark)  
                self.marks.append(Marks(student, course, mark))

    def list_courses(self):
        print("Courses: ")
        for course in self.courses:
            print(f"ID: {course.id}. Name: {course.name}. Credits: {course.credits}")

    def list_students(self):
        print("Students: ")
        for student in self.students:
            print(f"ID: {student.id}. Name: {student.name}. Date of Birth: {student.dob}")

    def show_marks(self):
        course_id = input("Enter the ID of the course to see the marks: ")
        for mark in self.marks:
            if mark.course.id == course_id:
                print(f"Student {mark.student.name} gets {mark.mark} in course {mark.course.id}")
            else:
                print(f"No marks entered for student {mark.student.name} in course {mark.course.id}")

    def calculate_gpa(self, student_id):
        student_marks = [mark for mark in self.marks if mark.student.id == student_id]
        if not student_marks:
            print("No marks found for the student.")
            return

        credits = np.array([next(course.credits for course in self.courses if course.id == mark.course.id) for mark in student_marks])
        marks = np.array([mark.mark for mark in student_marks])

        weighted_sum = np.sum(np.multiply(marks, credits))
        total_credits = np.sum(credits)

        gpa = weighted_sum / total_credits
        print(f"The GPA for student {student_id} is: {gpa}")

    def sort_students_by_gpa(self):
        student_gpas = []

        for student in self.students:
            student_id = student.id
            student_marks = [mark for mark in self.marks if mark.student.id == student_id]

            if not student_marks:
                print(f"No marks found for the student {student_id}.")
                continue

            credits = np.array([next(course.credits for course in self.courses if course.id == mark.course.id) for mark in student_marks])
            marks = np.array([mark.mark for mark in student_marks])

            weighted_sum = np.sum(np.multiply(marks, credits))
            total_credits = np.sum(credits)

            gpa = weighted_sum / total_credits
            student_gpas.append((student_id, gpa))

        sorted_student_gpas = sorted(student_gpas, key=lambda x: x[1], reverse=True)

        print("Students sorted by GPA (descending):")
        for student_id, gpa in sorted_student_gpas:
            print(f"Student {student_id}: GPA {gpa}")

school = StudentMark()
school.input_students()
school.input_courses()
school.input_marks()
school.list_courses()
school.list_students()
school.show_marks()

student_id_to_calculate_gpa = input("Enter the student ID to calculate GPA: ")
school.calculate_gpa(student_id_to_calculate_gpa)
school.sort_students_by_gpa()
