# 1. Write a python program to read the whole text of a file and catch the error if files does not exists


try :

    with open("workk.txt", "r") as f :
        x = f.read()
        print(x)
except FileNotFoundError as e:
    print("got this error", e)
             


            
    








