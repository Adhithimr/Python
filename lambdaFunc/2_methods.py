from functools import reduce

#join method
a = ['Harish', 'Rahul','Ayan']

final = "-".join(a)
print(final) 

#format 
#not used more
a = " {} is a good {1}".format("Adhithi", "girl")

name = input("Enter name: ")
marks = int(input("Enter marks: "))
phone = int(input("Phone number: "))

s = "The name of the student is {}, his marks are {} and phone number is {}".format(name, marks, phone)

print(s)

#map function
#map(function, function lsit)
#map is used to perform some operation on all the elements in the list

#filter
#filters according to some specific condition

#reduce function 
#reduce has to be imported from functools
l = [1,2,3,4,5]
def sum(a, b):
    return a + b

mul = lambda x,y:x*y

print(reduce(sum, l))
print(reduce(mul, l))
#reduce steps
# 1+2, 3, 4, 5
# 3+3, 4,5
# 6+4,5
#10+5
#15