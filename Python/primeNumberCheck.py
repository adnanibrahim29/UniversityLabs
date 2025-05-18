""" 

Write a Python program that uses a loop to determine if a positive integer number is a prime number. A number is prime if it is divisible only by 1 and itself. For example, 13 is prime but 12 is not (divisible by 1, 2, 3, 4, 6 and 12).

Sample inputs	Sample outputs
13	            13 is a prime number
12	            12 is NOT a prime number
"""

num : int = 13
isPrime : bool = True

if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            isPrime = False
            break
else:
    isPrime = False

if isPrime:
    print(f"{num} is a prime number")
else:
    print(f"{num} is NOT a prime number")