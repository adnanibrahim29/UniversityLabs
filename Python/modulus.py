""" 
Write a Python program that uses an int variable called num that stores a 4 digit number. 

Your program should then break up this number using the modulus operator into its component digits and print the message exactly as given below. 

Make sure to test your program with another 4 digit number, but 1981 should be used for your final answer.

Sample input	Sample output
N/A	            The digits in the number 1981 are:
                1
                9
                8
                1
"""
num : int = 1981
print(f"The digits in the number {num} are: ")
print(num // 1000)  
print((num % 1000) // 100)  
print((num % 100) // 10)  
print(num % 10) 