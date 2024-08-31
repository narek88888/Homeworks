# Write a Python function to sum all the numbers in a list.Sample List : (8, 2, 3, 0,
# 7)Expected Output : 20

def sum_of_all_numbers(numbers):

    result = 0
    for i in numbers :
        result = result + i
    return result

my_list = [5, 6, 7]
my_list_2 = [1,1,1]

print( sum_of_all_numbers(my_list_2))
print(sum_of_all_numbers(my_list))

    

    

