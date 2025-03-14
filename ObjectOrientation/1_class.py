class Employee:
    name = "Adhithi"
    lang = "Python"
    email = "adhithi@gmail.com" 
#class is like a blueprint to create an object

Adhithi = Employee()
Adhithi.id = "AD123"
print(Adhithi.name, Adhithi.email)

#object is a real word entity
#They have attributes (properties) and behaviour(action)

#name lang and email are class attribute
#id is an instance attribute

class TwoDvector:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")

class ThreeDvector(TwoDvector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")

a = TwoDvector(1,2)
b = ThreeDvector(1,2,3)