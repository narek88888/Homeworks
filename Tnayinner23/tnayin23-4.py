#23-4 ● Character ASCII Values:
# ○ Given a string, create a dictionary where keys are characters, and values are
# their ASCII values.

import string


x = "Hello"


ascii_letters_values_founder_in_word = {i:ord(i) for i in x }


print(ascii_letters_values_founder_in_word)