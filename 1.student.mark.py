students = []
courses = []
marks = {}

def input_students():
    num_students = int(input("Enter number of students: "))
    for _ in range(num_students):
        id = input("Enter student id: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth (in format dd-mm-yyyy): ")
        students.append((id, name, dob))

def input_courses():
    num_courses = int(input("Enter number of courses: "))
    for _ in range(num_courses):
        id = input("Enter course id: ")
        name = input("Enter course name: ")
        courses.append((id, name))

def input_marks_for_course(course_id):
    for student in students:
        mark = float(input(f"Enter the mark for student {student[1]} in course {course_id}: "))
        marks[(student[0], course_id)] = mark

def input_marks():
    for course in courses:
        print(f"Entering marks for course {course[1]}")
        input_marks_for_course(course[0])

def list_courses():
    print("Courses:")
    for course in courses:
        print(f"ID: {course[0]}, Name: {course[1]}")

def list_students():
    print("Students:")
    for student in students:
        print(f"ID: {student[0]},\nName: {student[1]},\nDoB: {student[2]}")

def show_marks():
    course_id = input("Enter the id of the course to show marks for: ")
    for student in students:
        if (student[0], course_id) in marks:
            print(f"Student {student[1]} gets {marks[(student[0], course_id)]} in course {course_id}")
        else:
            print(f"No marks entered for student {student[1]} in course {course_id}")

input_students()
input_courses()
input_marks()
list_courses()
list_students()
show_marks()
