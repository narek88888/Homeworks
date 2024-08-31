#Write a Python script that takes a list of words and return the longest word and the length of the longest one.


list_1 = ["work", "explanation", "a"]

longest = list_1[0]

for i in list_1 :
    if len(i) > len(list_1) :
        longest = i

print(longest)
print(len(longest))    


        
