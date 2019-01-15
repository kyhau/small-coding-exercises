"""
https://www.hackerrank.com/challenges/grading/problem
"""


def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] > 37:  # 40-3
            if (5 - grades[i] % 5) < 3:
                grades[i] += (5 - grades[i] % 5)
    return grades
