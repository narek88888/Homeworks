# Write a python function which create dict from 2
# lists with the same length

def dictionary_creator(lst1_key, lst2_value):
    if len(lst1_key) != len(lst2_value):

        return "the lists must be equal"
    
    new_dict = {}

    for i in range(len(lst1_key)):

        new_dict[lst1_key[i]] = lst2_value[i]

    return  new_dict


x = ['name', "last name", "age"]
y = ["Narek", "Gabrelyan", 16]

print(dictionary_creator(x,y))