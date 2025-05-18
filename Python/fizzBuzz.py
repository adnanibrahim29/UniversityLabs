""" 
Write a Python program that prints a message based on the value of an integer. Your program should have a variable called num.

If the value in "num" is divisible by 3, your program should print "fizz".
If the value in "num" is divisible by 5, your program should print "buzz".
If the value in "num" is divisible by both 3 and 5, your program should print "fizzbuzz".
If the value in "num" is divisible by neither 3 nor 5, your program should simply print the value of num.

You must use a series of if, elif and else statements to solve this problem.

Sample inputs	Sample outputs
3	            fizz
14	            14
"""

num : int = 14

if(num % 3 == 0 and num % 5 == 0):
    print("fizzbuzz")
elif(num % 3 == 0):
    print("fizz")
elif(num % 5 == 0):
    print("buzz")
else:
    print(num)