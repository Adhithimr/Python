#walrus operator is introduced after python 3.8 onwards
#It used to assign a variable

#using walrus operator

if (n:=len([1,2,3,4,5])) > 3:
    print(f"List is too long {n} elements, expected <= 3")

