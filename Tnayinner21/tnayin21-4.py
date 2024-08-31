# 21-4. List Exercise:
# Write a function that takes two lists and returns a new list containing only the common
# elements. (without using set)

def common_returner(list1, list2):
    
    list3 = []

    for i in list1:
        if i in list2:
            list3.append(i)
    return list3

numbers1 = [1, 1, 3, 4]  
numbers2 = [1, 1, 2, 3]

print(common_returner(numbers1, numbers2))
