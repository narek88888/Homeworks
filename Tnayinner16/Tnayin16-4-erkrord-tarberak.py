# Login System
# Write a simple login system where the user enters a username and password. Handle
# the KeyError by raising a custom exception if the username is not found in the users
# database(dictionary).

# erkrord tarberak

username = input("Write your username ")
password = input("Write your password ")

database = {"Max": "Mx12",  "John": "John44"}

try:
    for i in database.values():
        if password == i:
            print("correct")

        else:
            raise KeyError
                                   
except KeyError as e:
    print(KeyError)
    
     

#if grum enq menak passwordi hamar qani vor error chem stana ete m