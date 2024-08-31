# ● Using dict comprehension and a conditional argument create a dictionary from the current
# dictionary where only the key:value pairs with value above 2000 are taken to the new dictionary.
# #Type your answer here.
# dict1={"NFLX":4950,"TREX":2400,"FIZZ":1800, "XPO":1700}
# dict2={}
# print(dict2)


dict1 = {"NFLX":4950, "TREX":2400, "FIZZ":1800, "XPO":1700}

o = {k:v for k,v in dict1.items() if v > 2000 }
print(o)