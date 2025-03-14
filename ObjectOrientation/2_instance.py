class Employee:
    name = "Adhithi"
    lang = "Python"
    email = "adhithi@gmail.com" 
#class is like a blueprint to create an object

Adhithi = Employee()
Adhithi.id = "AD123"
Adhithi.lang = "JavaScript"
print(Adhithi.name, Adhithi.email, Adhithi.lang)

#Instance attribute takes first preference then the class attribute
