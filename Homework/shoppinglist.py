# Fill out Shopping List Program

print("Welcome to the shopping list program...")

shoppingList = [] 

finalise = False


        
def finaliseList():
    print("Your final list is: ")
    for item in shoppingList: print(item)
    print("Thank you!")
    return True
    
"""
Here we need functions for adding to the list and for removing from the list. 
"""


while finalise == False:
    print("The current shopping list contains: ")
    for item in shoppingList: print(item)
    option = int(input("To add an item, press 1\nTo remove an item, press 2\nTo finalise the list press 3:  "))

    """
    We need to tell the program what to do when 1 and 2 are pressed
    """
    
    if option == 3:
        finalise = finaliseList()


    """
    What should we do if a user types 4? 
    """
