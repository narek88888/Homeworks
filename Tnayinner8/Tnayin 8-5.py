# 8-5 You are given three lists, list1, list2, and list3. Your task is to implement a
# programm that takes these lists and prints the following:
# The set of elements that are common to all three lists.
# The set of elements that are present in at least two of the three lists, but not in all three.
# The set of elements that are unique to each list (present in only one list).

list1 = {"Arman", "Julie", "Gagik"} 
list2 = {"Arman", "Artyom", "Ani"}
list3 = {"Arman", "Gagik", "Anna"}

print(list1 & list2 & list3) # The set of elements that are common to all three list

print(list1 & list2 - list3, list2 & list3 - list1, list3 & list1 - list2) # The set of elements that are present in at least two of the three lists, but not in all three.
   
print(list1 ^ list2 ^ list3) # the set of elements that are unique to each list (present in only one list).


