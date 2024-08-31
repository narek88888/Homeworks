# 21-6. Tuple Exercise:
# Create a tuple of student names and their corresponding scores. Write a function to find
# the student with the highest score.


def the_highest_student_score_founder(sequence):



    the_highest_score = sequence[0][1]
    the_highest_student_with_score = sequence[0]

    for i in sequence:

        if i[1] > the_highest_score: 
            the_highest_score = i[1]
            the_highest_student_with_score = i

    return  the_highest_student_with_score

student_scores = (("Armen", 8), ("Gayane", 10), ("Lilit", 9))

print(the_highest_student_score_founder(student_scores))


