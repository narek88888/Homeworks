# Count how many even and odd numbers are in given range(10,35).



even = 0
ord = 0
for i in range(0,35) :
    if i % 2 == 0 :
        even = even + 1
    else :
        ord = ord +1

print(even)
print(ord)        

