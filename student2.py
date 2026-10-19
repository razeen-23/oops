class Student:
    def __init__(self, sid, name):
        self.sid = sid
        self.name = name
        self.courses = {}

    def assign_course(self, course):
        if course not in self.courses:
            self.courses[course] = None
            print("Course assigned successfully!")
        else:
            print("Course already assigned!")

    def add_marks(self, course, marks):
        if course in self.courses:
            if 0 <= marks <= 100:
                self.courses[course] = marks
                print("Marks added successfully!")
            else:
                print("Marks must be between 0 and 100.")
        else:
            print("Course not assigned to student!")

    def grade(self, marks):
        if marks is None:
            return "Not graded"
        elif marks >= 90:
            return "A"
        elif marks >= 80:
            return "B"
        elif marks >= 70:
            return "C"
        elif marks >= 60:
            return "D"
        else:
            return "F"

    def display(self):
        print("\nStudent ID:", self.sid)
        print("Name:", self.name)
        print("Courses and Marks:")
        if not self.courses:
            print("No courses assigned.")
        for course, marks in self.courses.items():
            print(course, "- Marks:", marks,
                  "- Grade:", self.grade(marks))


class StudentManagement:
    def __init__(self):
        self.students = {}
        self.courses = []

    def add_student(self, sid, name):
        if sid not in self.students:
            self.students[sid] = Student(sid, name)
            print("Student added successfully!")
        else:
            print("Student ID already exists!")

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            print("Course added successfully!")
        else:
            print("Course already exists!")

    def assign_course(self, sid, course):
        if sid not in self.students:
            print("Student not found!")
        elif course not in self.courses:
            print("Course not found!")
        else:
            self.students[sid].assign_course(course)

    def add_marks(self, sid, course, marks):
        if sid in self.students:
            self.students[sid].add_marks(course, marks)
        else:
            print("Student not found!")

    def display_student(self, sid):
        if sid in self.students:
            self.students[sid].display()
        else:
            print("Student not found!")

    def search_student(self, sid):
        if sid in self.students:
            print("Student found!")
            self.students[sid].display()
        else:
            print("Student not found!")


sms = StudentManagement()

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. Add Course")
    print("3. Assign Course")
    print("4. Add Marks")
    print("5. Display Student Details")
    print("6. Search Student by ID")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        sid = input("Enter student ID: ")
        name = input("Enter student name: ")
        sms.add_student(sid, name)

    elif choice == "2":
        course = input("Enter course name: ")
        sms.add_course(course)

    elif choice == "3":
        sid = input("Enter student ID: ")
        course = input("Enter course name: ")
        sms.assign_course(sid, course)

    elif choice == "4":
        sid = input("Enter student ID: ")
        course = input("Enter course name: ")
        try:
            marks = float(input("Enter marks (0-100): "))
            sms.add_marks(sid, course, marks)
        except ValueError:
            print("Please enter valid numeric marks!")

    elif choice == "5":
        sid = input("Enter student ID: ")
        sms.display_student(sid)

    elif choice == "6":
        sid = input("Enter student ID to search: ")
        sms.search_student(sid)

    elif choice == "7":
        print("Exiting Student Management System.")
        break

    else:
        print("Invalid choice! Try again.")