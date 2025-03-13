#loops is used to repeat some task

for i in range(1,10):
    print(i)

#while loop

#while loop will get executed when condition is true

i = 2
while i < 10:
    print(i)
    i += 1

'''
output:
1
2
3
4
5
6
7
8
9

'''

#list using while

l1 = [1, 'Adhithi', False, 'hello']

i =0
while i <len(l1):
    print(l1[i])
    i += 1

#for loop in list
 
for i in l1:
    print(i)

#tuple 

t = (2,4,5,6,8)

for i in t:
    print(i)

#String

s = "Hello"
for i in s:
    print(i)

#for loop with else

l3= [1, 'Adhithi', False, 'hello']

for item in l3:
    print(item)
else:
    print("Done")  #this is printed when the loop is exhausts

#pgm

n = int(input("Enter a number:"))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

#pgm
l = ['Adhtihi', 'Sneha', 'Sharath', 'Rahul']

for name in l:
    if name.startswith("S"):
        print(f"Hello, {name}")

#pgm 
n = int(input("Enter a number:"))

i = 1
while i < 11:
    print(f"{n} x {i} = {n*i}")
    i += 1

#prime number 

n = int(input("Enter a number:"))
for i in range(1,n):
    if n%i == 0:
        print("NOt prime")
        break
else:
    print("Prime")

#factorial

n = int(input("ENter a number:"))
f = 1
for i in range(1,n+1):
    f *=i
print(f)

#pattern

n = input()
for i in range(1,n+1):
    print(" "* (n-i) , end ="")
    print("*"* (2*i-1), end ="")
    print()