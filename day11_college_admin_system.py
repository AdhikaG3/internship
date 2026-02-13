class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def show_student(self):
        print("Student Name:", self.name)

class Staff(Person):
    def show_staff(self):
        print("Staff Name:", self.name)

class Professor(Staff):
    def show_professor(self):
        print("Professor Name:", self.name)


# Main Program
prof = Professor("Dr. Rao")
prof.show_professor()
