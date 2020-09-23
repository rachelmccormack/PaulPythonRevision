"""
Write a program (function!) that takes a list and returns
a new list that contains all the elements of the first list minus all the duplicates.
"""
listWithDuplicates = [3, 5, 2, 5, 7, 10, 14, 3, 14, 9, 15, 2, 3]
def removeDuplicates(list):
    uniqueList = []
    for i in list:
        if i not in uniqueList:
            uniqueList.append(i)
    return uniqueList

print(removeDuplicates(listWithDuplicates))

"""
write a program that prints out all the elements of the list that are less than or equal to 5.
"""

z = [1, 5, 3, 6, 7, 10, 1, 2, 5, 6]
def lessThan5(list):
    result = []
    for item in list:
        if item <= 5:
            result.append(item)
    return result

print(lessThan5(z))

"""
 write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
"""
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def overlap(list1, list2):
    resultList = []
    for item in list1:
        if item in list2 and item not in resultList:
            resultList.append(item)
    return resultList

print(overlap(a, b))


