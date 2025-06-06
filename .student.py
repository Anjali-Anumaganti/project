


# Teacher Login System
users = {
    "teacher1": "abc123",
    "teacher2": "efg456"
}

def teacher_login():
    print("Teacher Login System")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if username in users and users[username] == password:
        print("Login successful! Welcome,", username)
    else:
      return {student_id: student.get_details() for student_id, student in self.students.items()}
users = {
    "teacher1":"abc123",
    "teacher2" :"efg456"
    }
def teacher_login():
    print("teacher login system")
    username=input("enter your username ")
    password=input("enter your password ")
    if username in users and users[username]==password:
        print("login successful!welcome,",username)
    else:
        print("invalid username or password.please try again")

teacher_login()

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []
        self.final_grade = None

    def add_grade(self, grade):
        self.grades.append(grade)
        self.calculate_final_grade()

def remove_student(self, student_id):
        if student_id in self.students:
            removed_student = self.students.pop(student_id)
            print(f"Student {removed_student['name']} removed successfully.")
        else:
            print("Student ID not found.")

def display_students(self):
        if not self.students:
            print("No students available.")
        else:
            for student_id, data in self.students.items():
                print(f"ID: {student_id}, Name: {data['name']}, Grades: {data['grades']}")

def calculate_final_grade(self):
        if self.grades:
            self.final_grade = sum(self.grades) / len(self.grades)
        else:
            self.final_grade = None

def get_details(self):
        return {
            'Name': self.name,
            'Student ID': self.student_id,
            'Grades': self.grades,
            'Final Grade': self.final_grade
        }

class Teacher:
    def __init__(self, name):
        self.name = name

    def assign_grade(self, student, grade):
        student.add_grade(grade)

class Admin:
    def __init__(self):
        self.students = {}
        self.teachers = {}

    def add_student(self, name, student_id):
        self.students[student_id] = Student(name, student_id)

    def add_teacher(self, name):
        self.teachers[name] = Teacher(name)

    def get_student_info(self, student_id):
        student = self.students.get(student_id)
        if student:
            return student.get_details()
        return "Student not found."

    def get_all_students(self):
        return {student_id: student.get_details() for student_id, student in self.students.items()}

# Example Usage
admin = Admin()
admin.add_student("shyam", 1120)
admin.add_student("ram", 1121)
admin.add_teacher("Mrs.kumari")

teacher = admin.teachers["Mrs.kumari"]
teacher.assign_grade(admin.students[1120], 85)
teacher.assign_grade(admin.students[1120], 90)
teacher.assign_grade(admin.students[1121], 78)
teacher.assign_grade(admin.students[1121],85)



grade_system.display_students()

grade_system.remove_student(1120)
grade_system.display_students()



print(admin.get_student_info(1120))
print(admin.get_student_info(1121))


