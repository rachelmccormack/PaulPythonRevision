# Fill out Shopping List Program

print("Welcome to the shopping list program...")

shoppingList = [] 

finalise = False

def finaliseList():
    print("Your final list is: ")
    for item in shoppingList: print(item)
    print("Thank you!")
    return True

def addItem(item):
    shoppingList.append(item)

def removeItem(item):
    shoppingList.remove(item)

while finalise == False:
    print("The current shopping list contains: ")
    for item in shoppingList: print(item)
    option = int(input("To add an item, press 1\nTo remove an item, press 2\nTo finalise the list press 3:  "))

    if option == 1:
        item = input("What do you want to add to the list? ")
        addItem(item)

    elif option == 2:
        item  = input("Which item should be removed? ")
        while item not in shoppingList:
            item = input("Please choose an item in the shopping list to remove.")
        removeItem(item)

    elif option == 3:
        finalise = finaliseList()

    else:
        print("Please input a valid option")


