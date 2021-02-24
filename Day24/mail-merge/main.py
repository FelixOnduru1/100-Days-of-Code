PLACEHOLDER = "[name]"

with open("./input/names/invited_names.txt") as names_list:
    names = names_list.readlines()
print(names)
with open("./input/Letters/starting_letter.docx") as letter:
    message = letter.read()
    for name in names:
        stripped_name = name.strip()
        new_message = message.replace(PLACEHOLDER, stripped_name)
        with open(f"./output/ReadyToSend/letter_for_{stripped_name}.docx", mode="w") as completed_letter:
            completed_letter.write(new_message)

