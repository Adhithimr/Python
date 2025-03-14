class Employee:
    name = "Adhithi"
    lang = "Python"
    email = "adhithi@gmail.com" 

    def getInfo(self): #self is require
        print(f"The language is {self.lang}.")  
@staticmethod #saying that we dont need self means it doesnt take anything from the object
def greet():
    print("Good morning")


Adhithi = Employee()
Adhithi.id = "AD123"  #instance attribute
print(Adhithi.name, Adhithi.email)
Adhithi.getInfo()  #Employee.getInfo()
# Employee.getInfo(Adhithi)