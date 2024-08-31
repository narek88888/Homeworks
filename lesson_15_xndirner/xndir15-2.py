import random

def guess_number(num) :
    x = random.randint(1,100)
    if num >= x :
        return True
    else:
        return False
    
print(guess_number(5))
    