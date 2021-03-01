import pandas as pd
student_dict = {
    "student": ["Felix", "Maggie", "Mary"],
    "score": [90, 80, 75]
}

# Looping through rows in a Dataframe
student_dataframe = pd.DataFrame(student_dict)

for (index, row) in student_dataframe.iterrows():
    print(row.student)
