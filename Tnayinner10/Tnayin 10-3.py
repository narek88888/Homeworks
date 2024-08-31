# 10-3 Write a Python program that calculates the sum of all even numbers between 1 and 100 
# using a while loop

i = 0
even_numbers = []
while i < 100 :
    i+=1
    if i % 2 == 0 :
        even_numbers.append(i)

sum = 0
for i in even_numbers :
    sum = sum + i
print(sum)


    





