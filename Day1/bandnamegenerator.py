print("Welcome to the Band Name Generator. It suggests a possible band name and mentions where you hail from.")
name = input("What is your name?\n")
length = str(len(name))
nickname = input("What was your nickname when you were young?\n")
gender = input("What is your gender?\n")
if gender == "Male":
    gender = "Boys"
else:
    gender = "Girls"
school = input("What school did you go to?\n")
print("Your band name is " + nickname + length + " " + gender + " hailing from " + school + ".")


