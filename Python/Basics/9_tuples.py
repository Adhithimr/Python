#tuple is a collect of similar items. where duplicate is not allowed
#tuples are immutable

days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday','Saturday', 'Sunday')

print(len(days))
print(type(days))

#simple program to sum all the elements in the tuples

num = (1,2,3,4)
sum = 0 
for n in num:
    sum += n
print(sum)
print(type(num))