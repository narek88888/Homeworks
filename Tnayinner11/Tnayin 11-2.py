# Tnayin 11-2  
# 2.Letters Count
# Write a Python function to calculate count of each letter in string

def count_words_function(word) :
    count = 0
    letters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"    
    for i in letters :
        if i in word :
            count+=1
    return count

print(count_words_function("Python"))        
