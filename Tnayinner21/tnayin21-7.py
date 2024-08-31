# 21-7. Tuple Exercise:
# Write a function that swaps the values of two tuples.

def swaper(sequence1, sequence2 ):

    x = list(sequence1)
    y = list(sequence2)

    x[0] = 11
    y[0] = 11
    
    z = tuple(x)
    u = tuple(y)

    return z, u

numbers1 = (1,2,3)
numbers2 = (4,5,6)


print(swaper(numbers1, numbers2))


