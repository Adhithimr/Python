#conditional expression

#if , if else,  if elif 

#if
age = input("Enter your age:")
if age>18:
    print("Eligible")

#if elif
if age<=13:
    print("Kids")
elif age <= 16:
    print("Teen")
else:
    print("Adult")

#if elif else ladder
a = input("Enter the age:")
if a>= 18:
    print("You are above the age of consent")
elif a<0:
    print("Enter a valid age, you are entering negative value")
elif a==0:
    print("you are entering 0 which is valid age")
else:
    print("You are below the age of consent")

print("End of program")

#relational operators are used to evaluate the conditions inside if statement they are also called comparison operator

#multiple if statement
a =input()

if a%2 == 0:
    print("Even")
if a%2 != 0:
    print("Odd")

#else can not be alone if can be alone

n1 = int(input("Enter number 1:"))
n2 = int(input("Enter number 2:"))
n3 = int(input("Enter number 3:"))
n4 = int(input("Enter number 4:"))

if n1>n2 and n1>n3 and n1>n4:
    print("Greatest is ",n1)
elif n2>n1 and n2>n3 and n2>n4:
    print("Greatest is",n2)
elif n3>n1 and n3>n2 and n3>n4:
    print("Greatest is",n3)
else:
    print("Greatest is ",n4)
#if elif else in this if there is else block also code will work


#spam words detech
sentence = input("Enter sentence")

p1 = "Make a lot of money"
p2 = "buy now"  
p3 = "subscribe this"  
p4 = "click this"

if p1 in sentence or p2 in sentence or p3 in sentence or p4 in sentence:
    print("This is a spam")
else:
    print("This is not a spam")

#simple pgm

name = input("Enter username:")

if len(name)< 10:
    print("Accepted")
else:
    print("Too long")

#pgm
post = input()

if "Adhithi".lower() in post:
    print("They are talking about Adhithi")
else:
    print("They are not talking about Adhithi")