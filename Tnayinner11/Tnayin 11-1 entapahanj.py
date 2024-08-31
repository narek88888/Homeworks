# Write a python function, which add a new value
# with given key in dict.

def new_value_adder_function(sequence, key,  new_value) :
    sequence[key] = new_value

    return sequence
 
x = {"John":22, "Mary":21}
y = "John"
z = 23
print(new_value_adder_function(x,y,z))