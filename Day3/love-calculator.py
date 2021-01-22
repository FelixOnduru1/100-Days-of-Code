print("Welcome to the Love Calculator.\n"
      "This program calculates the percentage compatibility of you and your partner.")
your_name = (input("What are your full names?\n")).lower()
partner_name = (input("What are your partners full name?\n")).lower()
t_true = your_name.count("t") + partner_name.count("t")
r_true = your_name.count("r") + partner_name.count("r")
u_true = your_name.count("u") + partner_name.count("u")
e_true = your_name.count("e") + partner_name.count("e")
first_digit = str(t_true + r_true + u_true + e_true)

l_love = your_name.count("l") + partner_name.count("l")
o_love = your_name.count("o") + partner_name.count("o")
v_love = your_name.count("v") + partner_name.count("v")
e_love = your_name.count("e") + partner_name.count("e")
second_digit = str(l_love + o_love + v_love + e_love)

love_score = int(first_digit + second_digit)
if 10 > love_score or love_score > 90:
    print(f"Your score is {love_score}%. You go together like coke and mentos")
elif 40 < love_score > 50:
    print(f"Your love score is {love_score}%. You are alright together.")
else:
    print(f"You love score is {love_score}%")
