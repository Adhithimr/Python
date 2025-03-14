class Employee:
    a = 1

    @classmethod  # gives class attributes gives priority to class attribute
    def show(cls):
        print(f"The value of a is {cls.a}")

e = Employee()
e.a = 45
e.show()  #45 because it gives priority to instant variables