# Append new string in the middle of a given (even number of characters) string

x = "Python"
y = "new"

middle = len(x) // 2
print(x[:middle] + y + x[middle:])