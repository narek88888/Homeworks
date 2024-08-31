# List Element Removal
#  Write a function that removes an element at a specified index from a list. Handle the
# IndexError by raising a custom exception if the index is out of range



def list_element_removal(sequence, index) :
    
        
        if index not in range(len(sequence)) :
            raise IndexError("the index is out of range")
        else:
              del sequence[index]
        return sequence
              

x = [1,2]
y = 1
print(list_element_removal(x,y))
    
    