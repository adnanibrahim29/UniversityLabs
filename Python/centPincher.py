""" 
Paddy is trying to save money for a rainy day. He decides that he will begin by saving one cent and doubling how much he saves each day. 

Write a program to find out how many cent he will have saved on a given day. 

Please use a while loop to solve this question.

Sample code
Day 1: 1
Day 2: 1 + 2 = 3
Day 3: 1 + 2 + 4 = 7

Sample inputs	Sample outputs
2               3
3	            7
"""

days : int = 3
currentDays : int = 1
savings : int = 1
totalSavings : int = 0

while currentDays <= days:
    totalSavings += savings

    savings *= 2
    currentDays += 1
print(totalSavings)
