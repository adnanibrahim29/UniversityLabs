""" 
Write a Python program that: Creates a String that refers to “Most guitars have six strings.” Using relevant String methods:

1. Print the length of the String on a new line.
2. Print the position of the first occurrence of the character 'h' on a new line.
3. Print to the screen the String in all lower case characters on a new line.
4. Print to the screen the String in all upper case characters on a new line.
For practice save the length and position in integer variables and the strings in new string variables. Then print these variables instead.

Output Format (this is the not correct output)
    String Length: 7
    Position of first 'h': 3
    mostly ...
    MOSTLY ...

"""
string : str = 'Most guitars have six strings'

length : int =  str(len(string))
hPos: int = str(string.index('h'))
print("String Length: " + length)
print("Position of the first 'h': " + hPos)
print(string.lower())
print(string.upper())
