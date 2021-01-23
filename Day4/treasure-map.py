row1 = ["⬛", "⬛", "⬛"]
row2 = ["⬛", "⬛", "⬛"]
row3 = ["⬛", "⬛", "⬛"]
treasure_map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}\n")
position = input("Where do you want to put the treasure?\n")
column_position = int(position[0])
row_position = int(position[1])
print(f"The row position is {row_position}.")
print(f"The column position is {column_position}.")
treasure_map[row_position - 1][column_position - 1] = "X"
print(f"{row1}\n{row2}\n{row3}\n")
