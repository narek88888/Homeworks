# 13. Sets Exercise:
# Write a function that checks if two sets are disjoint (have no common elements).

def disjoint_checker(sequence1, sequence2):
        
        if sequence1 & sequence2:
            return "the sets are joint"
        else:
            return "the sets are disjoint"
    
        
        

x = {1, 2, 3}
y = {5, 6, 8}

print(disjoint_checker(x,y))