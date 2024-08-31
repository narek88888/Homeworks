# Exercise 7: Find youngest student
# Write a function that takes a dictionary with information about students. Return info
# about the youngest student

def the_youngest_student_founder(sequence):

    the_youngest_student = list(sequence.keys())[0]
    the_youngest_age = 20
    the_subjects_of_the_youngest_student = list(sequence.keys())[0]
    the_scores_of_the_youngest_student = list(sequence.keys())[0]
    
    

    for k,v in sequence.items():
        if v['age'] < the_youngest_age:
            the_youngest_student = v['name']
            the_youngest_age = v['age']
            the_subjects_of_the_youngest_student = v['subjects']
            the_scores_of_the_youngest_student = v['scores']
            

    return f"The youngest student is {the_youngest_student}, age is {the_youngest_age}, subjects are {the_subjects_of_the_youngest_student}, scores are {the_scores_of_the_youngest_student}"

students_info = {
'student1': {
'name': 'John Doe',
'age': 20,
'subjects': ['Math', 'Physics', 'English'],
'scores': [7, 9, 9, 6],
},
'student2': {
'name': 'Jane Smith',
'age': 19,
'subjects': ['Chemistry', 'Biology', 'History'],
'scores': [5, 6, 8, 10],
},
'student3': {
'name': 'Bob Johnson',
'age': 21,
'subjects': ['Computer Science', 'Statistics', 'Psychology'],
'scores': [8, 8, 9, 9, 9],
},
}


print(the_youngest_student_founder(students_info))





