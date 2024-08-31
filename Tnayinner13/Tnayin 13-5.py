# 5. Write a Python program to add two given lists using map and lambda.

numbers_1 = [1,2,3]
numbers_2 = [4,5,6]



list_adder = map(lambda x, y : x + y, numbers_1, numbers_2 ) 


print(list(list_adder))