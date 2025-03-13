name = "Adhithi"

name1 = 'Neha'

#String is a sequence of characters
#String are immutable
#immutable means once they are created they can not be changed

n_index = name[5]
print(n_index)

#slice
s1 = name[0:4] #4 is not included
print(s1)

#slicing can be done using -ve numbers
s2 = name[0:-2]
print(s2)

s3 = name[:3] #starts from 0
print(s3)

s4 = name[2:] # ends at last
print(s4)

#using steps fr slice
s5  = name[0: 2: 5]
print(s5)