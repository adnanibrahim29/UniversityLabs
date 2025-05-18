""" 
Write a Java program that prints a sequence of messages based on the fizzbuzz rules below. Your program should have two variables called start and end, the range in which to print messages (inclusive).

If the value in "num" is divisible by 3, your program should print "fizz".
If the value in "num" is divisible by 5, your program should print "buzz".
If the value in "num" is divisible by both 3 and 5, your program should print "fizzbuzz".
If the value in "num" is divisible by neither 3 nor 5, your program should simply print the value of num.

You must use a series of if, else if and else statements to solve this problem, along with a for loop.


Sample inputs	Sample outputs
2
3	            2 fizz

10
15	            buzz 11 fizz 13 14 fizzbuzz

"""


start : int = 2
end : int = 3

for i in range(start, end + 1, 1):
    if(i % 3 == 0 and i % 5 == 0):
        print("fizzbuzz", end=" ")
    elif(i % 3 == 0):
        print("fizz", end=" ")
    elif(i % 5 == 0):
        print("buzz", end=" ")
    else:
        print(i, end=" ")

