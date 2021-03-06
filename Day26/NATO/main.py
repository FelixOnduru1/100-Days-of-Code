import pandas as pd
df = pd.read_csv("nato_phonetic_alphabet.csv")

alphabet_dict = {row.letter: row.code for (index, row) in df.iterrows()}


def generate_phonetic():
    user_word = input("Enter a word:\n").upper()

    try:
        user_word_list = [alphabet_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry! Only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(user_word_list)


generate_phonetic()
