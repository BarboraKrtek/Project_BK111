#Projekt textovy analyzator

"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Barbora Krtek
email: krtek.bara@gmail.com
"""
TEXTS_dict = {}

TEXTS_list = ['''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30 and the Union Pacific Railroad,
which traverse the valley.''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

for i, text in enumerate(TEXTS_list):
    TEXTS_dict[i+1] = text

import sys

jmeno = input("Username: ")
heslo = input("Password: ")

print("--------------------------------------")

if jmeno == "bob" and heslo == "123":
    print("""Welcome to the app, Bob!
We have 3 texts to be analyzed.""")
elif jmeno == "ann" and heslo == "pass123":
    print("""Welcome to the app, Ann!
We have 3 texts to be analyzed.""")
elif jmeno == "mike" and heslo == "password123":
    print("""Welcome to the app, Mike!
We have 3 texts to be analyzed.""")
elif jmeno == "liz" and heslo == "pass123":
    print("""Welcome to the app, Liz!
We have 3 texts to be analyzed.""")
else:
    print("Unregistered user, please register! Terminating the program...")
#Ukonceni programu:
    sys.exit("Program terminated")

print("--------------------------------------")

vyber_textu = input("Enter a number btw. 1 and 3 to select: ")

print("--------------------------------------")

if vyber_textu not in ["1", "2", "3"]:
    print("Selection does not match database. Terminating the program...")
#Ukonceni programu:
    sys.exit("Program terminated")
else:
    print("Processing...")

#pocet slov
#pocet slov zacinajicich na velke pismeno
#pocet slov psanych velkym
#pocet slov psanych malym
#pocet cisel (ne cifer)
#sumu vsech cisel (ne cifer) v textu

selected_text = TEXTS_dict[int(vyber_textu)]

print("--------------------------------------")

value = selected_text
words = value.split()

word_count = len (words)
titlecase_count = sum(1 for word in words if word.istitle())
uppercase_count = sum(1 for word in words if word.isupper() and word.isalpha())
lowercase_count = sum(1 for word in words if word.islower())
numeric_count = sum(1 for word in words if word.isnumeric())
numeric_sum = sum(int(word) for word in words if word.isnumeric())

print(f"There are {word_count} words in the selected text.")
print(f"There are {titlecase_count} titlecase words.")
print(f"There are {uppercase_count} uppercase words.")
print(f"There are {lowercase_count} lowercase words.")
print(f"There are {numeric_count} numeric strings.")
print(f"The sum of all the numbers {numeric_sum}.")

print("--------------------------------------")
print("""LEN|    OCCURENCES   | NUMBER OF WORDS""")
print("--------------------------------------")

length_count = {}
for word in words:

    cleaned_word = word.strip('.,!?"\'')
    length = len(cleaned_word)
    if length > 0:
        if length in length_count:
            length_count[length] += 1
        else:
            length_count[length] = 1

sorted_length_count = sorted(length_count.items())

for length, count in sorted_length_count:
    print(f"{length:>3}|{'*' * count:<17}|{count}")