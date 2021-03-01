import pandas as pd
df = pd.read_csv("nato_phonetic_alphabet.csv")

alphabet_dict = {row.letter: row.code for (index, row) in df.iterrows()}

user_word = input("Enter a word:\n").upper()

user_word_list = [alphabet_dict[letter] for letter in user_word]

print(user_word_list)
