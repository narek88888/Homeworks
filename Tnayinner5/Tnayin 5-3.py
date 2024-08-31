# 5-3 .Smallest
# Write a Python program to get the smallest number from a list.

numbers_list = [1, 5, 6, 7, 9]

the_smallest = numbers_list[0]

for i in numbers_list :
    if i < the_smallest :
        the_smallest = i

print(the_smallest)




     