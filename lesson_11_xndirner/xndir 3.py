# Write a Python function to return the even numbers from a given list. Sample List
# : [1, 2, 3, 4, 5, 6, 7, 8, 9]

def even_numbers(*numbers) :

    numers_list =  [1, 2, 3, 4, 5, 6, 7, 8, 9]

    result = []

    for i in numers_list :
        if i%2 == 0 :
            result.append(i)

    return result

print(even_numbers())            


