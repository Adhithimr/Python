class Employee:
    name = "Adhithi"
    lang = "Python"
    email = "adhithi@gmail.com" 

    def __init__(self, name, lang, email):  #menthods starts with __ called dunder method and they are automatically called only __init__
        self.name = name
        self.lang = lang
        self.email = email
        print("Iam creating an object")

    def getInfo(self): #self is require
        print(f"The language is {self.lang}.")  
@staticmethod #saying that we dont need self means it doesnt take anything from the object
def greet():
    print("Good morning")


Adhithi = Employee("Adhithi", "Java", "adhithi@gmail.com")
Adhithi.id = "AD123"  #instance attribute
print(Adhithi.name, Adhithi.email)
Adhithi.getInfo()  #Employee.getInfo()
# Employee.getInfo(Adhithi)