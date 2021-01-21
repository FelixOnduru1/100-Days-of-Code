name = input("What is your name?")
length = str(len(name))
nickname = input("What was your nickname when you were young?")
gender = input("What is your gender?")
if gender == "Male":
    gender = "Boys"
else:
    gender = "Girls"
school = input("What school did you go to?")
print("Your band name is " + nickname + length + " " + gender + " hailing from " + school)
