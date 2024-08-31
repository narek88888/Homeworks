# Exercise 8: Find student with highest average score
# Write a function that takes a dictionary with information about students. Return info
# about the youngest student


def student_with_the_highest_average_score(sequence):

    highest_score = list(sequence.values())[0]
    the_youngest_student = list(sequence.values())[0]
    sum = 0
    for k,v in sequence:
        scores = v['scores']
        sum += scores
        average_score = sum / len(scores)
        
        if average_score > highest_score:
            highest_score = 



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




      




