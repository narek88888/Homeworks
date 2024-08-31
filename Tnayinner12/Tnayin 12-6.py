# Exercise 6: Count Words Function
# Write a function that counts the number of words in a sentence.


def word_counter_function(sentence) :
    x = sentence.split()
    return len(x)
print(word_counter_function("Python code"))