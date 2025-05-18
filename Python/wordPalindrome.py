""" 
Write a Python program that will determine if a String, called text, is a palindrome. A String is a palindrome if the word remains the same when spelled in reverse. For example:

    NAVAN is a palindrome
    CAVAN is NOT a palindrome
Note: Please use "navan" as your first test String when evaluating. The program should work irrespective of case. Print all test Strings with Uppercase letters

Sample Output
   NAVAN is a palindrome
Sample Output
   CAVAN is NOT a palindrome

"""

text : str = 'navan'.lower()
revCheck : str = ''
for i in range(len(text) -1, -1, -1):
    revCheck += text[i]
    revCheck.lower()

if(text == revCheck):
    print(f"{text} is a palindrome")
else:
    print(f"{text} is NOT a palindrome")