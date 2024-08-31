# 14-1 Character Count:
# Write a Python script that reads a text file (input.txt) and counts the
# occurrences of each character (including spaces and punctuation). Output the
# character frequency to another text file (output.txt).


with open('file.for14-1.txt', 'r') as f_1 :
    read = f_1.read()
    words_occurrences = {}
    for i in read:
        if i in words_occurrences:
            words_occurrences[i] += 1
        else:
            words_occurrences[i] = 1 

with open('new.file.for14-1.txt', 'a') as f_2:
    x = f_2.write(str(words_occurrences))
   


   
    




# outputy petq e gcem urish file i mej