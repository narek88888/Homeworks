#23-6 ● Dictionary Merge:
# ○ Given two dictionaries, merge them into a new dictionary, excluding any keys
# that start with an underscore.



dict1 = {"y":1, "_u":14}
dict2 = {"h":4, "_l":25}


dict3 = {k:v for i in (dict1, dict2) for k,v in i.items() if k[0] != "_" }


print(dict3)
