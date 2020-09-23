#This is a simple function to give an understanding of variable scope
def exampleFunction():
    notice = "I love London!" #Here "notice" is a local variable - it is only useable in this function
    print(notice)

notice = "I love Paris!"
exampleFunction()
print(notice) #The variable "notice" here is a global variable- running the exampleFunction has no impact on its value. 
