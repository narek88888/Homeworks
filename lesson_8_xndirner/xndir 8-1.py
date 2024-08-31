# 8-1 Check if a value exists in a dictionary



x = {"Hello": 11, "Good" : 15}

value = 11

result = False
for k, v in x.items() :
    if value == v :
        result = True

print(result)


 