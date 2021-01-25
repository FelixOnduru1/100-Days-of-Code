student_heights = input("Input a list of students heights"
                        "(separate your entries with commas):\n").split(",")

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

highest_height = 0

for height in student_heights:
    if height > highest_height:
        highest_height = height
print(f"The highest height among students is {highest_height}.")
