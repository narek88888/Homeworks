# 6-4 Palindrome Checker
# Write a program that prompts the user to enter a word and checks if it is a
# palindrome. A palindrome is a word that reads the same backward as forward.
# Use string slicing and an if-else statement to compare the original word with its
# reverse.

word = "lav"

x = ""

for i in word:
     x = i + x

if word == x:
     print("Yes, it is palindrom")
else:
     print("It does not palindrom")

