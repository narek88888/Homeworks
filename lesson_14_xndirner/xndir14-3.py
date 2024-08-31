# 3. Write a python program to add text to a file and display the text in python.txt.

with open('file_for_work.txt', 'a') as f:
    f.write(" ""again")
print(f)

with open('file_for_work.txt', 'r') as x:
    y = x.readline()
print(y)




