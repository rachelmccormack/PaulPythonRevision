#Simple example of writing out to a file. 
file = open("test.txt", "w") #Opening a file. The "w" parameter here indicates we are "writing" to this file.
#This will also create test.txt in your folder even if it does not exist.
file.write("hello")
file.write("Hello")
file.write("Another line")
file.write("\n Don't forget your new line character")
file.close() #This is very important
