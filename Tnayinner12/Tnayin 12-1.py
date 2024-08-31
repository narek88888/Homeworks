# Exercise 1: Check Pangram Function
# Write a function that checks if a sentence is a pangram.



def pargram(letter):

    Tarer = "qwertyuiopasdfghjklzcxvbnm"

    for i in Tarer:
        if i not in letter:
            return False
    return True
            
         
print(pargram("qwertyuiopasdfghjklzcxvb"))



            

