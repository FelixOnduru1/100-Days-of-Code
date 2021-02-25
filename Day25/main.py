import csv
import pandas as pd

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     print(data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperature = int(row[1])
#             temperatures.append(temperature)
#     print(temperatures)

data = pd.read_csv("weather_data.csv")

# Convert the dataframe to a dictionary
data_dict = data.to_dict()

# Convert a series to a list
temp_series = data["temp"]
temp_list = temp_series.to_list()
average_temp_2 = sum(temp_list)/len(temp_list)
average_temp = temp_series.mean()
max_temp = temp_series.max()

# Get data in columns
# The code is similar to data["condition"]
condition_list = data.condition

# Pulling out a row
monday = data[data.day == "Monday"]
day_max_temp = data[data.temp == data.temp.max()]


# Getting a specific data in a row
monday_condition = monday.condition
monday_temp_f = (monday.temp * 9/5) + 32

# create a dataframe from scratch
new_data_dict = {
    "students": ["Mary", "John", "Jane"],
    "scores": [90, 78, 69]
}
new_data = pd.DataFrame(new_data_dict)
new_data.to_csv("new_data.csv")
