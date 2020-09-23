#This is an example of creating functions, calling functions,
# using lists and looping through them, as well as using < and > for basic maths.

def biggest(numberList):
    bigNumber = -1000 # In our list, any number is going to be bigger than -1000.
    for number in numberList:
        if number > bigNumber:
            bigNumber  = number
    return bigNumber

def smallest(numberList):
    smallNumber = 1000 #In our list, any number is going to be smaller than  1000.
    for number in numberList:
        if number < smallNumber:
            smallNumber  = number
    return smallNumber

array =  [4, 8, 2, 54, 6] #array is another term for list - most likely this will be used in your classes.
print(smallest(array))
print(biggest(array))
