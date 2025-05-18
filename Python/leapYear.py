""" 
Write a Python program with two int variables, year and month. The program should print out how many days are in that month in that year.

Hint:
A year is a leap year if it is divisible by 400 or if it is divisible by 4 and not divisible by 100. So, 1900 was a not a leap year, but 2000 and 2004 were.

You also need to print an appropriate message (see sample 2) if the month is invalid.

Sample inputs	Sample outputs
2023
10	            In October 2023 there were 31 days

2023
13	            Not a valid month
"""

year : int = 2000
month : int = 2

if(month == 1):
    print(f"In January {year} there were 31 days")
elif(month == 2):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(f"In February {year} there were 29 days")
    else:
        print(f"In February {year} there were 28 days")
elif(month == 3):
    print(f"In March {year} there were 31 days")
elif(month == 4):
    print(f"In April {year} there were 30 days")
elif(month == 5):
    print(f"In May {year} there were 31 days")
elif(month == 6):
    print(f"In June {year} there were 30 days")
elif(month == 7):
    print(f"In July {year} there were 31 days")
elif(month == 8):
    print(f"In August {year} there were 31 days")
elif(month == 9):
    print(f"In September {year} there were 30 days")
elif(month == 10):
    print(f"In October {year} there were 31 days")
elif(month == 11):
    print(f"In November {year} there were 30 days")
elif(month == 12):
    print(f"In December {year} there were 31 days")
else:
    print("Not a valid month ")