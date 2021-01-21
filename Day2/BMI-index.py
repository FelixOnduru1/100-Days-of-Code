print("This program calculates your BMI and tells you whether you are underweight, have a normal weight,"
      " overweight, or obese.")
mass = float(input("What is your weight in kg?\n"))
height = float(input("What is your height in metres?\n"))
bmi = round((mass/height**2), 1)
bmi_new = str(bmi)


if bmi < 18.5:
    print("You BMI is " + bmi_new + "kg/m^2.\nThis means you are underweight.")
elif 18.5 >= bmi < 25:
    print("You BMI is " + bmi_new + "kg/m^2.\nThis means you have normal weight.")
elif 25 >= bmi < 30:
    print("You BMI is " + bmi_new + "kg/m^2.\nThis means you are overweight.")
else:
    print("You BMI is " + bmi_new + "kg/m^2.\nUnfortunately, you are obese.")
