# Write a function in python to read the content from a text file "example.txt" line by
# line and display the same on screen.

with open('file_for_work.txt', 'r') as f :
    x = f.readline()
print(x)

