# 1.check how many ‘a’ characters are in inputed string


x = input("enter your word")

count_of_a = 0

for i in x:

    if i == "a":
        
        count_of_a = count_of_a + 1

print(count_of_a)


