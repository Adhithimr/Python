#list is a collection of ordered items.
#list allows duplicate

fruits = ['Apple','Berry','Mango']
print(fruits[2]) #indexes start from 0

fruits.append('Orange')

#supports slicing

#it can store different types of data
list1 = [23,'hello',4.5,'bye',True]
print(list1)

#explore list functions
# sort, rev, insert, append, pop, remove etc

# marks = []

# m1 = int(input())
# marks.append(m1)
# m2 = int(input())
# marks.append(m2)
# m3 = int(input())
# marks.append(m3)
# m4 = int(input())
# marks.append(m4)

# print(marks)

#find item in list

list2 = ['Adhithi','Neha','Pooja','Arya']

name = input("Enter your name:")

if name in list2:
    print("Name is in the list")
else:
    print("Name is not in the list")