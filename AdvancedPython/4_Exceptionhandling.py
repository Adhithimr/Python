try:
    a = int(input("Hey, Enter a number:"))
    print(a)
except ValueError as v:
    print("Heyyyy")
    print(v)
except Exception as e:
    print(e) #prints the error
    print("Hey, Enter a valid number")
print(a)


#types of error
#value error
#zero error

a1 = int(input("Enter a number:"))
b1 = int(input("Enter a number:"))
c1 = int(input("Enter a number:"))

if(b1 == 0):
    raise ZeroDivisionError("Hey, our program is not meant to divide numbers by zero")
else:
    print(f"The division a/b is {a1/b1}")


#Try with else 

try:
    a = int(input("Hey, Enter a number:"))
    print(a)

except Exception as e:
    print(e) #prints the error
else:
    print("I am inside else")  #if try gets executed successful else will be executed

#Try with finally

try:
    a = int(input("Hey, Enter a number:"))
    print(a)

except Exception as e:
    print(e) #prints the error

finally:
    print("Hey, Iam inside a finally") 
#finally executes 

def main():
    try:
        a1 = int(input("Hey, Enter a number:"))
        print(a)
        return

    except Exception as e:
        print(e) #prints the error

    finally:
        print("Hey, iam inside finally") #even if try block will return then also finally will get executes

#pgm 
try:
    with open("1.txt", r) as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open("2.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open("3.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)


print("Thank You!")
