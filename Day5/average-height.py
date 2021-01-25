student_heights = input("Input a list of students heights"
                        "(separate your entries with commas):\n").split(",")

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

sum_heights = 0
for height in student_heights:
    sum_heights += height
total_height = sum_heights

num_students = 0
for student in student_heights:
    num_students += 1
total_students = num_students
average_height = round(total_height/num_students, 2)
print(f"The total sum of heights is {total_height}.")
print(f"The average height of the students is {average_height}")
