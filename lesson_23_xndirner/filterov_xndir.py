# filter their age if we divide by 2 the output will be 0

orginal_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}


filter_of_age = filter(lambda x: x[1] % 2 == 0, orginal_dict.items() )    

x = dict(filter_of_age)

print(x)    
