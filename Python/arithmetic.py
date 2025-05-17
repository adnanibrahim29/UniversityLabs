"""
Write a Python program and:

1. Declare integers, called num1, num2 and num3, with values of 5, 10 and 15 respectively.
2. Declare integers called result1, result2 and set each to a default value of 0.
3. Declare a double called result3 and set it to the value 0.0.    
4. Add num1, num2 and num3 together and store the result in result1.    
5. Multiply num2 by num3 and store the result in result2.    
6. Divide num3 by num1 and store the result in result3.    
7. Print the values stored in the variables result1, result2 and result3 to the screen, each on a new line using the same structure as shown in the sample output below.    

Please note you will need to create variables one per line

Sample input	Sample output
5               Addition: 30
10              Multiplication: 150
15              Division: 3.0
"""
num1 : int = 5
num2 : int = 10
num3 : int = 15

result1 : int = 0
result2 : int = 0
result3 : float = 0.0

result1 = num1 + num2 + num3
result2 = num2 * num3
result3 = num3 / num1

print(f"Addition: {result1}")
print(f"Multiply: {result2}")
print(f"Divide: {result3}")

