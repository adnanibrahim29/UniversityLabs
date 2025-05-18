"""
Write a Python program that checks to see if the age of a person is greater than or equal to 66. If it is, print out that the person is retired; otherwise, print that they are not retired. Use an integer variable age to represent the age of the person.

Sample inputs	Sample outputs
67	            Person is retired
24	            Person is not retired
"""

age : int = 66

if age >= 66:
    print("Person is retired")
else:
    print("Person is not retired")