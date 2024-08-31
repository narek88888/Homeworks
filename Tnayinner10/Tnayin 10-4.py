# 10-4 Write a Python program that generates a random number between 1 and 100 and asks
# the user to guess the number. The program should give hints whether the guessed
# number is too high or too low until the correct number is guessed


import random

random_number = random.randint(1, 100)

print(random_number)

while True :
    x = int(input())    

    if x > random_number :
        print("higher than the kept number")

    elif x < random_number:
        print("lower than the kept number") 

    else: 
        print("You guessed the number correctly")   
        break 
# while true grum enq nra hamar, vor anverj cikly ashxati ays paragayum minchev chisht tivy gushaki 













