#Match is introduced after 3.10

def http_status(status):
    match status:
        case 200:
            return "Ok"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown status"
        
print(http_status)

#Similar to switch

#merging dictionary
dict1 = {'a': 1, 'b':2}
dict2 = {'c': 3 , 'd':4}
merge = dict1 | dict2
print(merge)