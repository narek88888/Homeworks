# 14-3 File Concatenation:
# Write a Python script that takes multiple text files as input and concatenates their
# contents into a single text file


with open('file.for.concatenation.1.txt', 'r') as f_1 :
    x = f_1.read()

with open('file.for.concatenation.2.txt', 'r') as f_2 :
    y = f_2.read()

with  open('new.file.for.concatenation.txt', 'a') as f_3 :
    t = f_3.write(x + y)

print(t)    