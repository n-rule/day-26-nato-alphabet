import pandas

nato_alphabet = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}
phonetic_list = []

while len(phonetic_list) < 1:
    try:
        name = input('Enter your name : \n').upper()
        phonetic_list = [nato_alphabet_dict[letter] for letter in name]

    except KeyError:
        print('This is an ugly name')

print(phonetic_list)

# BOTH WORKS
# phonetic_list = []
# for n in name:
#     phonetic_list.append(nato_alphabet_dict[n])


