import numpy as np

# Create NumPy array
marks = np.array([
    [78, 85, 90, 88],
    [92, 81, 76, 89],
    [65, 70, 72, 68],
    [88, 90, 94, 92],
    [55, 60, 58, 62]
])

# 1️⃣ Average marks of each student
student_avg = np.mean(marks, axis=1)
print("Average marks of each student:")
print(student_avg)

# 2️⃣ Average marks for each subject
subject_avg = np.mean(marks, axis=0)
print("\nAverage marks for each subject:")
print(subject_avg)

# 3️⃣ Total marks scored by each student
total_marks = np.sum(marks, axis=1)
print("\nTotal marks of each student:")
print(total_marks)

# 4️⃣ Maximum and Minimum marks in entire dataset
max_marks = np.max(marks)
min_marks = np.min(marks)
print("\nMaximum mark in dataset:", max_marks)
print("Minimum mark in dataset:", min_marks)

# 5️⃣ Extract marks of 2nd student using slicing
second_student = marks[1]
print("\nMarks of 2nd student:")
print(second_student)
