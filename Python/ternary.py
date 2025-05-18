""" 
Write a Python program that prints out the bus fare depending on whether the user is an adult or a child. If adult, the fare is 2.05, if child the fare is 0.65.

You must use the ternary operator.

A variable of type char called passenger should have the value 'A' or 'C' which shows if the user is an adult or child. A double called fare holds the the fare to pay.

Sample inputs	Sample outputs
A	            The fare is: €2.05
C	            The fare is: €0.65      

"""

passenger : str = 'C'

fare = 2.05 if passenger == 'A' else 0.65
print(f"The fare is: €{fare:.2f}")

