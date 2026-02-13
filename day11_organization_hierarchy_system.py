class Employee:
    def work(self):
        print("Employee is working")

class Manager(Employee):
    def manage_team(self):
        print("Manager is managing the team")

class Director(Manager):
    def make_decision(self):
        print("Director is making decisions")


# Main Program
director = Director()
director.work()
director.manage_team()
director.make_decision()
