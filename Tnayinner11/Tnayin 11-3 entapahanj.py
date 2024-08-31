# Write a python function, which create a dictionary
# for given number N, where keys are numbers from
# 1 to N, and values are cubs of that numbers


def cubs_of_numbers(number) :

    dict = {}
    i = 1

    while i <= number:
        dict[i] = i**3
        i+=1
        
    return dict 


print(cubs_of_numbers(8))


    