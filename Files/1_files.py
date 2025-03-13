#the data will be stored in RAM
f = open('file.txt')
data = f.read()
print(data)
f.close()

# two types of files
#1. text file
#2.binary file

#write
st = "About Python"
f = open('file.txt', "w")

f.write(st)
f.close()

#file mode
#open, read, write, close
#readlines()
#append()
#rt readtext

f = open("file.txt")
print(f.read())
f.close()

#The same can be written using with statement like this:

with open("file.txt") as f:
    print(f.read())

#you dont have to explicity close the file
#f.write() to clear the content