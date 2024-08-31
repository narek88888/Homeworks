# ● Generate a list with list comprehension which contains all numbers from (1 - 999)
# ○ Write a list comprehension which iterates on generated list and generate new list where are cubs of odd numbers from first list



y =  [x**3 for x in range(1,1000) if x % 2 != 0 ]

print(y)