# ● create a range from 100 to 160 with steps of 10. using dict comprehension, create a dictionary
# where each number in the range is the key and each item divided by 100 is the value.




h = {v: v / 100 for v in range(100,160,10) }

print(h)