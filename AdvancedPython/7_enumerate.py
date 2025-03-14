l1 = [3,4,23,454,243]
# index =0
# for i in l1:
    
#     print(f"The item number at {index} is {i}")
#     index += 1

#this can be simplified using enumerate function

for index, item in enumerate(l1):
    print(f"The item number at index {index} is {index}")