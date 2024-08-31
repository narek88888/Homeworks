# Get the same items in two ranges using nested loop.(0,10), (5,15).




l = []

for i in range(0,10) :
    for u  in range(5,15) :
        if i == u :
            l.append(i)
                     
print(l)
        