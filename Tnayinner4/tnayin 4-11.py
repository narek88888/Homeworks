# 4-11 Rounding - 2
# Given a real number, round it to the nearest whole.

x = float(input("Write number, which do you want to round"))


if x - int(x) >= 0.5 :
    print(int(x) + 1)
else:
    print(int(x))  


                        


