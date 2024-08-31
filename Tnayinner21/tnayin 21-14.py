# 14. Strings Exercise:
# Write a function that capitalizes the first letter of each word in a sentence.


def capitalize_function(sentence):

    x = sentence.split()
    y = []

    for i in x:

        y.append(i.capitalize())

    return " ".join(y)
    
z = "hello world" 


print(capitalize_function(z))

