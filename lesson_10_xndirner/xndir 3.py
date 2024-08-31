# Display the numbers from 1 to 10 except 6.
# Expected Output: 1 2 3 4 5 7 8 9 10

number = 0
while number < 10 :
    number+=1
    if number == 6 :
        continue
    print(number)


