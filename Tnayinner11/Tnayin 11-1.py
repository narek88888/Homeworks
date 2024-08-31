# Tnayin 11-1
# 1.Max of Three
# Write a Python function to find the Max of three numbers.

def max_number(*args) :

    
    max_number_checker = args[0]

    for i in args  :
        if i > max_number_checker :
            max_number_checker = i
            
    
    return max_number_checker
print(max_number(1,4,2))     