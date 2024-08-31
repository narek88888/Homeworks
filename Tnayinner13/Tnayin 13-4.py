# 4. Write a Python program to find intersection of two given arrays using Lambda.
# Original arrays:
# [1, 2, 3, 5, 7, 8, 9, 10]
# [1, 2, 4, 8, 9]


intersection_founder = lambda a, b : a & b

x = {1, 2, 3, 4, 5}
y = {1, 2, 5, 6, 7}



print(list(intersection_founder(x,y)))