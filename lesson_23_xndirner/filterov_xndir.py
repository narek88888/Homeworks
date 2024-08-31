# filtrel nranq, voronc tariqy tokosov bajanac 2-i mnacordy 1 e

orginal_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}


filter_of_age = filter(lambda x: x[1] % 2 == 0, orginal_dict.items() )    

x = dict(filter_of_age)

print(x)    