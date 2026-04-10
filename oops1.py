class Employee:
    def __init__(self):
        self.id = 1
        self.salary = 50000
        self.designation = 'Software developer'

    def travel(self, destination):
        print(f"trvelling to the {destination}")

sam = Employee()

sam.travel("Pune")