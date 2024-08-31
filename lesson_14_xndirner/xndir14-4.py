# 4. Write a function display_words() in python to read text from a text file
# "example.txt", and display those words, which are less than 4 characters.

def display_words(file, mode) :
    less_than_four = []
    with open(file, mode) as f :
        x = f.read()
        y = x.split()
        for i in y :
            if len(i) < 4 :
                less_than_four.append(i)
        return less_than_four


print(display_words('file_for_work.txt', 'r'))

    
