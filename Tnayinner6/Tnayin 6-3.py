# 6-3 Word Finder
# Write a program that takes a list of words and a target word as input. The
# program should find and print all words in the list that contain the target word.
# Use a for loop, the in operator, and an if statement to check if the target word is
# present in each word in the list.

x = input("Write sentence")

Verbs = ["swim", "run", "walk"]

result = []

for i in Verbs :
    if i in x :
        result.append(i)
print(result)        



        
    



