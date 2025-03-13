#Function is a set of code or instruction that perform specific task

#def is a keyword used to define function

def avg(a, b,c):   #function definiton
    return (a+b+c)/3
result = avg(2,4,6)  #function call
print(result)

 #greeting function

def greet(name):
    print(f"Hello, {name}")

greet("Adhithi")

#default parameter

def greet1(name, ending="Good day"):   #ending is a default parameter
    print(f"Hello, {name}")
    print(ending)

greet1("Adhithi")

#pgm
def largest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
    
a = 2
b = 5
c = 8

print(largest(a,b,c))

#inch to cm

def inch_to_cm(inch):
    return inch*2.54

n = int(input("Enter value in inches:"))
print(f"The value in cm is {inch_to_cm(n)}")


#pgm

def rem(l, word):
    for item in l:
        if not (item == word):
            n.append(item.strip(word))
l = ['AAa', 'BBb','CCc','aa']
print(rem(l,"aa"))
