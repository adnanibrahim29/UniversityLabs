""" 
Write a program that initialises a variable to store a single character and two variables to store whole numbers. The character should be either '+', '-', '/' or '*'. The program should check the character and perform the appropriate arithmetic. That is, if the character is '+' then the result of the two numbers added together should be printed to the screen.

Sample inputs	Sample outputs
+ 9 3	        12
/ 24 4	        6
"""

operation : str = '+'
num1 : int = 9
num2 : int = 3

if(operation == '+'):
    print(num1 + num2)
elif(operation == '-'):
    print(num1 - num2)
elif(operation == '*'):
    print(num1 * num2)
elif(operation == '/'):
    print(num1 / num2)
else:
    print("Not a Valid Operation")