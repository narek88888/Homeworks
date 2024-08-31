# 21-12. List Exercise:
# Write a function that returns the nth largest element from a list.


def the_largest_element_founder(sequence):

    the_largest_element = sequence[0]

    for i in sequence:

        if i > the_largest_element:
            the_largest_element = i

    return the_largest_element
    
numbers = [1, 3, 20, 18, 35, 10]

print(the_largest_element_founder(numbers))


