import random


cursanti_grupa = ["Delia - Gabriela Simion,"
                  "Maria Oltean",
                  "Croitoru Alexandru - Theonel",
                  "Daniela -Madalina Ionita",
                  "Claudia - Maria Ionita",
                  "Otto - Richard Neamtu",
                  "Paul - Eugen Barbuta",
                  "Adela - Iasmina Petre",
                  "Bostan Andrei - Robert",
                  "Sipos Lajos - Bogdan",
                  "Cobzaru Dana",
                  "Butnaru Aurelian - Florin",
                  "Nedelescu Ana - Daniela",
                  "Petrina Andreea",
                  "Andrei Neagu"]

dic_grupe_mici = {}

key_nr_grup = 1

while len(cursanti_grupa) >= 2:
    grupa = random.sample(cursanti_grupa, 2)
    dic_grupe_mici["Grup " + str(key_nr_grup)] = grupa
    key_nr_grup += 1

    for cursant in grupa:
        cursanti_grupa.remove(cursant)

for key, value in dic_grupe_mici.items():
    print(f"{key}: {value}")

# rezultat generat:

"""
Grup 1: ['Andrei Neagu', 'Claudia - Maria Ionita']
Grup 2: ['Bostan Andrei - Robert', 'Croitoru Alexandru - Theonel']
Grup 3: ['Otto - Richard Neamtu', 'Butnaru Aurelian - Florin']
Grup 4: ['Paul - Eugen Barbuta', 'Petrina Andreea']
Grup 5: ['Cobzaru Dana', 'Delia - Gabriela Simion,Maria Oltean']
Grup 6: ['Adela - Iasmina Petre', 'Nedelescu Ana - Daniela']
Grup 7: ['Daniela -Madalina Ionita', 'Sipos Lajos - Bogdan']

Process finished with exit code 0
"""