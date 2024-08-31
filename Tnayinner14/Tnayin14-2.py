# 14-2 Find and Replace:
# Implement a Python program that reads a text file (input.txt), prompts the user
# for a word to find, and another word to replace it with. Replace all occurrences of
# the first word with the second word and save the modified text to a new file
# (output.txt).

find = input("find word that there is in file ")
replace = input("write with which word do you want to replace the word ")

with open('file.for.14-2.txt', 'r') as f_1:
    x = f_1.read()

    word_replacing = x.replace(find, replace)

with open('new.file.for.14-2.txt', 'w') as f_2:
     f_2.write(word_replacing)








