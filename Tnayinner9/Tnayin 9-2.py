# Print a square pattern using a nested for loop. The pattern should have 5 rows and 5 columns

x = 5

for i in range(x):
    y = []
    for u in range(x):
        y.append("*")
    print(" ".join(y))
        
