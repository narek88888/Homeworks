# String Length Checker
# Write a function that checks the length of a string provided by the user. Handle the
# TypeError by raising a custom exception if the input is not a string.



def length_of_a_string(word):

        if not type(word) is str :
                raise TypeError ("Only strings are allowed")
        else :
                return len(word)

print(length_of_a_string("p"))                  



