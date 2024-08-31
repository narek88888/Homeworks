# 21-3. List Exercise:
# Given a list of numbers, write a function to find the sum of all numbers in the list that
# can be divided by 7.


def sum_of_all_numbers_divisible_by_7(sum):
    
    result = 0

    for i in sum:
        if i % 7 == 0:
            result += i
    return result

numbers = [1, 7, 14, 21]

print(sum_of_all_numbers_divisible_by_7(numbers))        
            

