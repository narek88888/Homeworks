# 21-8. Dictionaries Exercise:
# Create a dictionary of book titles and their authors. Write a function to search for a book
# by its title and return the author's name.

def author_founder(book_name):

    for k, v in x.items():

        if k in book_name:
            return v 


x = {"War and Peace": "Leo Tolstoy", 
     "Time Machine": "H.G Wells", 
     "The Tempest": "William Shakespeare"}


print(author_founder("Time Machine"))