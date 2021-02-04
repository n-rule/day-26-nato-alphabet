student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)
nato_alphabet = pandas.read_csv('nato_phonetic_alphabet.csv')

print(nato_alphabet.code[1])

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}

print(nato_alphabet_dict)

{"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

name = input('Enter your name : \n').upper()

phonetic_list = [nato_alphabet_dict[letter] for letter in name]

# BOTH WORKS
# phonetic_list = []
# for n in name:
#     phonetic_list.append(nato_alphabet_dict[n])

print(phonetic_list)
