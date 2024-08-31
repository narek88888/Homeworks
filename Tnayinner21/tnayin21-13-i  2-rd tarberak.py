# 21-13 2-rd tarberak. Sets Exercise:
# Write a function that checks if two sets are disjoint (have no common elements).


def disjoint_checker(sequence1, sequence2):
    
    for i in sequence1:

        if i in sequence2:
            return False
        
    return True
    
            
x = {1, 2, 3}
y = {5, 2, 7}

print(disjoint_checker(x,y))


