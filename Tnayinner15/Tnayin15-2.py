# Random Password Generator:
# Write a function that generates a random password for the user. Allow the user to
# specify the length and complexity of the password (include letters, numbers, and
# symbols).
# Ogtvel random u string module-neric (string.ascii_letters,
# string.digits,string.punctuation )


import random
import string


def Random_Password_Generator(length, letter, number, symbol) :

    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    x = ""
    password = ""
    
    if letter == True:
        x += letters
        password += random.choice(letters)
    if number == True:
        x += digits
        password += random.choice(digits)
    if symbol == True :
        x += symbols
        password += random.choice(symbols)

    
    while len(password) < length :
        password += random.choice(x)
    return password

print(Random_Password_Generator(5, True, True, False))

   
    
       





    


    