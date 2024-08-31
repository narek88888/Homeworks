# 1. Write a Python program to square and cube every number in a given list of integers using Lambda.

# Sample. ([1,2,3,4,5])
# Output: ([1, 4, 9, 16, 25], [1, 8, 27, 64, 125])


numbers = [1, 2, 3, 4]
square = map(lambda x: x **2, numbers)
cube = map(lambda y: y**3, numbers)

print(list(square))
print(list(cube))
