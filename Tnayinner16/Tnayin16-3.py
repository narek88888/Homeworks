# URL Validator
# Write a function that validates a URL string. Handle the ValueError by raising a custom
# exception if the URL format is invalid.

import string

def url_velidator(url) :

    letters = string.ascii_letters
    
    if url[:8] == "https://" and "." in url[7:]: 
        return "Yes, it is URL"
    
    
    for i in url[7:]:
        if i in letters:
            return "Yes, it is URL"

    raise ValueError
        
    

x = "https://www.python"

print(url_velidator(x))
