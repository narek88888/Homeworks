# Write a Python program that input a sentence and return the longest word and the length of the longest one.


x = input()

x_splitted = x.split()
longest = x[0]

for i in x_splitted:
    if len(i) > len(longest):
        longest = i

print(longest)
print(len(longest))

    

