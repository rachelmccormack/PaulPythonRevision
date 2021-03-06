"""
Write a program which asks the user to input a number between 0 and 23.
This input should be stored in a variable called "hour".
Have the program output the equivalent time using the 12 hour clock
(ie a number between 1 and 12, followed by am or pm.)
For example:
- Input 0 return 12am
- Input 4 returns 4am
- Input 12 returns 12pm
- Input 15 returns 3pm. 
"""

userTime = (int(input("Please enter a number between 0 and 23 ")))

if userTime > 12:
    userTime = userTime % 12
    print((str)(userTime) + "pm")

elif userTime == 12:
    print("12pm")

elif userTime == 0:
    print("12am")

else:
    print((str)(userTime) + "am")