#23-5 ● Filtering Word Lengths:
# ○ Given a list of words, create a dictionary where keys are words, and values are
# their lengths, but only for words with lengths greater than 3.


x = ["Armenain", "English", "Russian"]

filter_word_lengths = {word:len(word)  for word in x}

print(filter_word_lengths)