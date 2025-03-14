class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode

p = Programmer("Adhihti", 30000, 560062)
print(p.name, p.salary, p.pincode)
r = Programmer("Neha", 27000, 560072)
print(r.name, r.salary, r.pincode)

  #use self when you want to  access the instance variable of the class
  
     