# 4.Write a Python program to count the even, odd numbers in a given array of integers using Lambda.
# 2 filter

numbers = [1,2,3,4,5,6]


even_numbers_count =  filter(lambda x: x % 2 == 0, numbers )

odd_numbers_count = filter(lambda y: y % 2 !=0, numbers)

print(len(list(even_numbers_count)))

print(len(list(odd_numbers_count)))

