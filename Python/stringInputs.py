""" 
Write a program that takes a String in from user input. You should then:

1. Print the String in lowercase.
2. Print every even indexed letter in uppercase and every odd indexed letter in lowercase.
3. Print the length of the word.
4. Print every odd indexed letter of the word on it's own line.

Sample input	Sample output
PROGRAMMING	    programming
                PrOgRaMmInG
                11
                R
                G
                A
                M
                N
"""

print("Enter a string")
text : str = str(input())

print(text.lower())

# Print even index uppercase and odd index lowercase
formatted_text = ""
for i in range(len(text)):
    if i % 2 == 0:
        formatted_text += text[i].upper()
    else:
        formatted_text += text[i].lower()

print(formatted_text)

# Print the length of the word
print(len(text))

# Print every odd indexed letter of the word on its own line
for i in range(len(text)):
    if i % 2 == 0:
        continue
    else:
        print(text[i].upper())
