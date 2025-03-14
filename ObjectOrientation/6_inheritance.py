class Employee:
    company = "ITC"
    def show(self):
        print(f"The name is {self.name} and salary is {self.salary}")

class Programmer:
    company = "ITC infotech" 
    def show(self):
        print(f"The name is {self.name} and salary is {self.salary}")
    def showLang(self):
        print(f"The name is {self.name} and he knows is {self.lang}")

#Inheritance means inheriting properties and behivour from parent class to child class

class Programmer(Employee):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")


a = Employee()
b = Programmer()

print(a.company, b.company)

#Types of inheritance
#1. Single inheritance
#2.Multilevel inheritance
#3.Multiple inheritance
