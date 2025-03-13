#Dictionary stores data in the form of key value pair
#where it allows duplicate of values, but duplicate of key is not allowed
#indexes are not allowed
#we can use keys to find the required information
#these are mutable

info = {'name' : 'Adhihti', 'age': 23, 'email':'adhithimr@gmail.com'}
print(type(info))

#methods
print(info.items())

print(info.keys())

print(info.values())

info.update({'age': 22})

print(info)

print(info.get("age1"))  #prints none
print(info("age1"))  #prints error
#pgm
words = {
    'kurshi': 'chair',
    'nahi':'no',
    'billi': 'cat'
}
word = input("Enter the word to convert:")
print(words[word])

d = {}

name = input()
lang = input()

d.update({name:lang})