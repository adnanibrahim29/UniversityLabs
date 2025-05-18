""" 
Write a Python program that will take a String and reverse it. To complete this question Declare a String called reverse and assign it the value "programming". Your program should then reverse this string using a loop.

Sample Input
    programming
Sample Output
    gnimmargorp
"""

string : str = "programming"
reversed : str = ""

for i in range(len(string) - 1, -1, -1):
    reversed += string[i]
print(reversed)