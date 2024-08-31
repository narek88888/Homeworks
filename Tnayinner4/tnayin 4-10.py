# 4-10 Salaries
# Given the salaries of three employees working at a department, find the
# amount of money by which the salary of the highest-paid employee differs
# from the salary of the lowest-paid employee. The input consists of three
# positive integers - the salaries of the employees. Output a single number,
# the difference between the top and the bottom salaries

salary_1 = int(input("write your salary"))
salary_2 = int(input("write your salary"))
salary_3 = int(input("write your salary "))



if salary_1 > salary_2 > salary_3:
    print(salary_1 - salary_3)
    

elif salary_1 > salary_3 > salary_2 :
    print(salary_1 - salary_2)


elif salary_2 > salary_1 > salary_3 :
    print(salary_2 - salary_3)
          
elif salary_2 > salary_3 > salary_1 :
    print(salary_2 - salary_1)


elif salary_3 > salary_2 > salary_1 :
    print(salary_3 - salary_1)

elif salary_3 > salary_1 > salary_2 :
    print(salary_3 - salary_2)

elif salary_1 < salary_2 < salary_3:
    print(salary_3 - salary_1)
    
elif salary_1 < salary_3 < salary_2  :
    print(salary_2 - salary_1)

elif salary_2 < salary_1 < salary_3 :
    print(salary_3 - salary_2)
    
elif salary_2 < salary_3 < salary_1 :
    print(salary_1 - salary_2)

elif salary_3 < salary_2 < salary_1 :
    print(salary_1 - salary_3)

elif salary_3 > salary_1 > salary_2 :
    print(salary_2 - salary_3)

elif salary_1 == salary_2 < salary_3 :
    print(salary_3 - salary_1)

elif salary_1 < salary_2 == salary_3 :  
    print(salary_2 - salary_1)

elif salary_1 > salary_2 == salary_3 :
    print(salary_1 - salary_2) 

elif salary_1 == salary_2 == salary_3 :
    print(salary_1 - salary_2)

elif salary_1 == salary_3 > salary_2 :
    print(salary_1 - salary_2) 

elif salary_1 > salary_2 > salary_3 :
    print(salary_1 - salary_3)    

elif salary_1 == salary_2 > salary_3 :
    print(salary_1 - salary_3)
    


    







