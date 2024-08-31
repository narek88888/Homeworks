import random



def guess_number(num) :
    x = random.randint(1,10)
    if num == x :
        return True
    else:
        return False
    
print(guess_number(2))    