""" 
Write a Java program that prints all of the numbers from 10 to 20 to the screen using a while loop and prints the numbers from 20 to 10 using a for loop

Sample inputs	Sample outputs
N/A	            10 11 12 13 14 15 16 17 18 19 20
                20 19 18 17 16 15 14 13 12 11 10
"""
start : int = 10
end : int = 20
while start <= end:
    print(start, end = " ")
    start += 1

print(" ")

# Reset start to 10 for the for loop
start : int = 10

for num in range(end, start -1, -1):
    print(num, end=" ")