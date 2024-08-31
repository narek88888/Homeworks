# 4-8 Three Numbers
# Input three integers. Output the word “Sorted” if the numbers are listed in
# a non-increasing or non-decreasing order and “Unsorted” otherwise

a = int(input("Write first number"))
b = int(input("Write second number"))
c = int(input("Write third number"))

if a > b > c :
    print("Sorted")

elif  a <= b <=c and a >= b >= c :
    print("Sorted")

else:
    print("Unsorted")

