# ● * Write a list comprehension to print this output
# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********

# aranc bazmapatkel

k = [["*" for i in range(u)]  for u in range(11)] 

for i in k:

    print("".join(i))

