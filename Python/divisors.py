""" 
Write a Python program that uses a for loop to print all of the divisors of a given number. An example can be been in the sample input / output. You should print your answer as a comma seperated list.

Sample input	Sample output
24	            1,2,3,4,6,8,12,24
"""

num : int = 24
string = ""
for i in range(1, num + 1):
    if num % i == 0:
        string += str(i) + ","
print(string[:-1])
