# 5-4 Second smallest
#Write a Python program to find the second smallest number in a list.


numbers = [4,3,5]

the_smallest = numbers[0]
the_second_smallest = numbers[0]

for i in numbers:
    if i < the_smallest:
        the_second_smallest = the_smallest
        the_smallest = i

print(the_second_smallest)
   

 
   

