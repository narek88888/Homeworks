# 2. Write a function in Python to count and display the total number of words in a text file.

with open('file_for_work.txt', 'r') as f :
    x = f.read()
    y = x.split()

print(len(y))


