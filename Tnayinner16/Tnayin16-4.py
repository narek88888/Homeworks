# Login System
# Write a simple login system where the user enters a username and password. Handle
# the KeyError by raising a custom exception if the username is not found in the users
# database(dictionary).

username = input("Write your username ")
password = input("Write your password ")

database = {"Max": "Mx12",  "John": "John44"}

try:
    if database[username] == password:
        print("correct")
            
except :
    raise KeyError



