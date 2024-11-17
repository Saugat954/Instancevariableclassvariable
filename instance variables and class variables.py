class Employee:
    #class variable
    company = "Apple"
    numberofEmployee = 0
    def __init__(self,name):
        self.name = name
        Employee.numberofEmployee += 1

    def showDetails(self):
        print(f"The name of Employee is {self.name} and is Working in {self.company} and the number of people working in a company is {self.numberofEmployee}")

Employee1 = Employee("Saugat")
Employee1.showDetails()
#instancevariable
Employee2 = Employee("Bijaya")
Employee2.company = "Google"
Employee2.showDetails()
