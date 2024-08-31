# 21-9. Dictionaries Exercise:
# Write a function that finds the key with the maximum value in a dictionary.



def key_founder_with_maximum_value(sequence):



    max_value = list(sequence.values())[0]
    max_key = list(sequence.keys())[0]

    for key, value in sequence.items():
        if value > max_value:
            max_value = value
            max_key = key

    return {max_key: max_value}

y = {"oo":11, "ll": 20, "pp":10}

print(key_founder_with_maximum_value(y))





