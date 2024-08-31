# Count how many uppercase and lowercase characters are in this sentence.(“The Quick Brown Fox")


senctence = ("TheQuickBrownFox")

y = senctence.upper()
z = senctence.lower()


count = 0

for i in senctence:

    if i in y :
        count = count + 1

    elif i in z :
        count = count + 1
        

print(count)        

        