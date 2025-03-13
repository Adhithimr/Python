#Recursion means function inside a function or which calls itself

def factorial(n):
    if n ==1 or n==0:
        return 1
    return n*factorial(n-1)

n = int(input("Enter a number:"))
print(f"The factorial of {n} is: {factorial(n)}")


#sum of n natural number

def sum(n):
    if n == 1:
        return 1
    return sum(n-1) + n

print(sum(4))

#pattern

def pattern(n):
    if n == 0:
        return
    print("*"*n)
    pattern(n-1)

pattern(5)