"""
    
Write a Python program that uses if selection statements to print out which type of vehicle a driver's license allows them to drive.

Declare a character variable called license. Your program should check the value of the character variable and print out an appropriate message based on the value stored in it.

- 'a' allows you to drive motorcycles
- 'b' allows you to drive cars
- 'c' allows you to drive trucks
- 'd' allows you to drive buses

Following the sample outputs below, print out which vehicle the license holder can drive. You should set the 'license' variable to a in your code.

Sample inputs	Sample outputs
a	            Motorcycle
b	            Car
c	            Truck
d	            Bus
"""

license : str = 'a'

if(license == 'a'):
    print("Motorcycle")
elif(license == 'b'):
    print("Car")
elif(license == 'c'):
    print("Truck")
elif(license == 'd'):
    print("Bus")
else:
    print("Not a valid category")
