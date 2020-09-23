"""
Fizzbuzz- this will test how well you understand mathematics operations, if statements, and while loops. 
Loop through the numbers 1 to 100. Print out these numbers. If a number is divisible by 3, print "fizz" instead of the number.
If the number is divisible by 5, print buzz instead. If the number is divisible by both 3 and 5, print fizzbuzz. example:
1, 2, fizz, 4, buzz, fizz, 7, 8, fizz, buzz, 11, fizz, 13, 14, fizzbuzz

Please extend this into a function which takes in a number to loop up to,  ie fizzbuzz(200) gives you fizzbuzz 1-200. 
"""


def fizzbuzz(number):
    for item in range(1, number+1): #We must offset by 1, as python counts from 0. 
        if item % 3 == 0 and item % 5 == 0:
            print("fizzbuzz")
      
        elif item % 3 == 0:
            print("fizz")
        
        elif item % 5 == 0:
            print("buzz") 
        else:
            print(item)

fizzbuzz(200)
