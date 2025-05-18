""" 
Write a Python program that determines and prints the digits that make up every five-digit palindromic number that is divisible by 53. 

For example, for the palindromic number 97679 the program should print as below in the sample output. This is not the solution.


Sample input	Sample output
N/A	            97679
                9
                7
                6
                7
                9
                **********
"""

for i in range(10000, 99999):
    if i % 53 == 0:
        str_num = str(i)
        if str_num == str_num[::-1]:  # Check if the number is a palindrome
            print(i)
            for digit in str_num:
                print(digit)
            print("**********")
        