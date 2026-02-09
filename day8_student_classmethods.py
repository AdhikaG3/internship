class Student:
    college_name = "ABC Engineering College"

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("College:", Student.college_name)

    @classmethod
    def change_college(cls, new_name):
        cls.college_name = new_name

    @staticmethod
    def is_valid_roll(roll_no):
        return roll_no > 0


# Objects
s1 = Student("Rahul", 101)
s2 = Student("Anita", 102)

s1.display()
s2.display()

print()

# Update college name for all students
Student.change_college("XYZ Institute of Technology")

s1.display()
s2.display()

print()

# Static method usage
print(Student.is_valid_roll(101))
print(Student.is_valid_roll(-5))
