# Exercise 4: Find Index Function
# Write a function that finds the index of a given element in a list. If the element is not
# present, return -1.

def index_founder(list, element) :
    for i in range(len(list)) :
        if list[i] == element :
            return i
    return -1
        
        
x = [1,2,3,4,5]
y = 3

print(index_founder(x,y))



    
  
