#23-2 ● Character Frequency:
# ○ Given a string, create a dictionary where keys are characters and values are their
# frequencies in the string.



x = "hello"



character_frequency_counter = {i: x.count(i) for i in x}

print(character_frequency_counter)

