""" 
Write a Java program that will:

Create a String that references “Computer Science”.
Create a String that references “Education”.
Use your knowledge of generating substrings to take “Science” from the first string and store it in a new String.
Use your knowledge of String concatenation to form a String “Science Education” from the newly created string and the second string.
Print the concatenated String to the screen.
Note: Do not print out “Science Education” without following the steps.

Sample Output
Science Education

"""

firstString : str = 'Computer Science'
secondString : str = 'Education'

newString : str = firstString[9:]

conCatString : str = newString + " " + secondString
print(conCatString)