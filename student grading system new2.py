
# Define the global dictionaries
users = {
    "teacher1": "abc123",
    "teacher2": "efg456"
}

students = {}  # Initialize the students dictionary

# Login Function
def teacher_login():
    print("Teacher login system")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users and users[username] == password:
        print(f"Login successful! Welcome, {username}")
    else:
        print("Invalid username or password. Please try again.")

# Create Account Function
def create_account():
    username = input("Enter your username: ")
    if username in users:
        print("Username already exists!")
    else:
        password = input(f"Enter a password for {username}: ")
        users[username] = password
        print(f"Account for {username} created successfully!")

# Add Student Function
def add_student():
    name = input("Enter student name: ").strip()
    if not name:
        print("Student name cannot be empty.")
        return
    if name in students:
        print(f"Student {name} already exists.")
    else:
        students[name] = []  # Create an empty list for the student's grades
        print(f"Student {name} added successfully.")


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

# Add Student Grade Function
def add_student_grade():
    name = input("Enter student name: ")
    if name in students:
        try:
            grade = float(input(f"Enter grade for {name}: "))
            students[name].append(grade)
            print(f"Grade {grade} added for {name}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    else:
        print(f"Student {name} does not exist.")

# Remove Student Function
def remove_student():
    name = input("Enter student name to remove: ")
    if name in students:
        del students[name]
        print(f"Student {name} removed successfully.")
    else:
        print(f"Student {name} does not exist.")

# Display Student Grades Function
def display_student_grades():
    if not students:
        print("No student records available.")
        return
    for name, grades in students.items():
        avg_grade = sum(grades) / len(grades) if grades else 0
        print(f"Student: {name}, Grades: {grades}, Average: {avg_grade:.2f}")

# Main Menu Function
def menu():
    while True:
        print("\n==== WELCOME TO STUDENT GRADING SYSTEM ====")
        print("1. Add Student")
        print("2. Add Grade to Student")
        print("3. Remove Student")
        print("4. View Student Grades and Average")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            add_student_grade()
        elif choice == "3":
            remove_student()
        elif choice == "4":
            display_student_grades()
        elif choice == "5":
            print("Exiting the system. Thank you.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

