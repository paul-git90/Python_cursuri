"""
2.	Generators

Implementați un generator pentru loteria 6/49 și noroc:
-	Primele 6 apelări către generator vor da cate un numar intre 1 si 49 (inclusiv)
-	Ultima apelare va da un singur număr de “noroc” format din 7 cifre
"""

import random


def loto_generator():
    # Generăm 6 numere unice între 1 și 49
    numere_loto = random.sample(range(1, 50), 6)

    # Returnăm fiecare număr din cele 6 generate
    for numar in numere_loto:
        yield numar  # Folosim yield pentru a returna câte un număr la fiecare apel

    # Generăm un număr de noroc format din 7 cifre
    numar_noroc = random.randint(1000000, 9999999)  # Un număr aleator între 1 milion și 9.999.999
    yield numar_noroc  # Returnăm numărul de noroc la final


# Exemplu de folosire:
loto_gen = loto_generator()

# Afișăm primele 6 numere din loterie
for _ in range(6):
    print(f"Număr loterie: {next(loto_gen)}")

# Afișăm numărul de noroc
print(f"Numărul norocos: {next(loto_gen)}")


# todo Logica din spate
"""
Pentru a implementa un generator pentru loteria 6/49 și un număr de noroc format din 7 cifre, vom folosi 
funcția yield din Python, care ne permite să creăm funcții generator. Spre deosebire de un iterator tradițional, 
un generator păstrează starea internă și permite să returnezi valori secvențial, fără a necesita stocarea tuturor 
valorilor în memorie.

Pași de implementare:
Generatorul pentru numerele 6/49:
La primele 6 apeluri, generatorul va returna câte un număr aleator între 1 și 49. Pentru asta, vom folosi funcția 
random.sample care ne dă o listă de numere unice din acest interval.
Generatorul pentru numărul de noroc:
La al șaptelea apel, vom genera un număr aleator format din 7 cifre.
"""

"""
Explicația logicii:
Generarea numerelor pentru loteria 6/49:

Am folosit funcția random.sample care alege 6 numere unice din intervalul [1, 49]. Aceasta garantează că nu există 
duplicate.
Cu ajutorul buclei for, returnăm câte un număr la fiecare apel al funcției next().
Generarea numărului de noroc:

După ce cele 6 numere au fost returnate, funcția continuă cu generarea unui număr de noroc format din 7 cifre. 
Am folosit random.randint pentru a genera un număr între 1.000.000 și 9.999.999.
Utilizare:

Generatorul poate fi folosit în mod repetat prin apeluri succesive la next(). De exemplu, folosim un for pentru 
a itera prin primele 6 numere, și un apel suplimentar la next() pentru a obține numărul de noroc.
"""