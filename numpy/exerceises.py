import numpy as np

grades = np.array([
    [70, 80, 90],
    [50, 60, 55],
    [90, 95, 100],
    [40, 45, 50]
])

print("if you think each row as a student calculate average grade for each student")
student_averages = np.mean(grades, axis=1, dtype=int) 
print(student_averages)
average_of_each_exam = np.mean(grades, axis=0, dtype=int) 
print(average_of_each_exam) 

print("find max average grade student")
# max_average_grade = np.max(np.mean(grades, axis=1, dtype=int) )
max_average_grade = np.max(student_averages)
print(max_average_grade)
min_average_grade = np.min(np.mean(grades,axis=1, dtype=int))
print(min_average_grade)
min_average_grade_index = np.argmin(student_averages)
print("min average grade student index: ", min_average_grade_index)

print("let's say 60 is the passing avg grade who passes and who fails")
print("passing students: ", student_averages >= 60)
passed_students = student_averages[student_averages >= 60]
# the above line 
failed_students = student_averages[student_averages < 60]
print("passed student notes : ", student_averages[student_averages >= 60])
print("failing students notes: ", student_averages[student_averages < 60])

# the average note of grater then 60 less then 75 
print("average note of grater then 60 less then 75: ", student_averages[(student_averages >= 60) & (student_averages <= 75)])