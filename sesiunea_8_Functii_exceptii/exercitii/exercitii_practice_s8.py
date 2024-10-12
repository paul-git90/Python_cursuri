"""Exercitii practice - sesiunea 8: Functii si Exceptii"""

"""
EX1: Defineste o functie care printeaza, pe rand,
primele 10 numere (1, 10).
"""
print("ex 1 - rezolvare")


def afiseaza_primele_10_numere():
    for numar_din_lista in range(1, 11):
        print(numar_din_lista)


# Apelăm funcția pentru a afișa primele 10 numere
afiseaza_primele_10_numere()
"""
EX2: Scrie o functie care parcurge o lista de numere data si
afiseaza mesajul 'Este par' pentru numerele pare si
'Este impar' pentru numere impare.
Daca in lista se gaseste un element care nu e numar intreg,
afiseaza un mesaj utilizatorului si apoi sari peste
elementul respectiv.
(Foloseste functia built-in isinstance()
pentru verificare daca elementul curent e int sau nu)
"""
print("ex 2 - rezolvare")


def verifica_numere(lista_numere):
    for element in lista_numere:
        if isinstance(element, int):
            if element % 2 == 0:
                print(f'{element} este par')
            else:
                print(f'{element} este impar')
        else:
            print(f'{element} nu este un număr întreg, sar peste el')


# Exemplu de listă de numere
numere = [1, 2, 'a', 3.5, 4, 5, 'b', 6]

# Apelăm funcția pentru a verifica numerele din listă
verifica_numere(numere)
"""
EX3: Scrie o functie care calculeaza patratul unui numar.
Afiseaza rezultatul.
"""
print("ex 3 - rezolvare")


def calculeaza_patratul(numar):
    patratul = numar ** 2
    print(f'Pătratul numărului {numar} este {patratul}')


# Exemplu de apelare a funcției
calculeaza_patratul(4)
calculeaza_patratul(10)
"""
EX4: Scrie o functie care calculeaza impartirea dintre doua numere.
Afiseaza rezultatul.
"""
print("ex 4 - rezolvare")


def imparte(numar1, numar2):
    if numar2 == 0:
        print("Eroare: Împărțirea la zero nu este permisă.")
    else:
        rezultat = numar1 / numar2
        print(f"Rezultatul împărțirii dintre {numar1} și {numar2} este: {rezultat}")


# Exemplu de utilizare
imparte(10, 2)  # Rezultatul va fi 5.0
"""
EX5: Scrie o functie care calculeaza inmultirea dintre doua numere.
Afiseaza rezultatul.
"""
print("ex 5 - rezolvare")


def inmulteste(numar1, numar2):
    rezultat_inmultire = numar1 * numar2
    print(f"Rezultatul înmulțirii dintre {numar1} și {numar2} este: {rezultat_inmultire}")


# Exemplu de utilizare
inmulteste(5, 3)  # Rezultatul va fi 15
"""
EX6: Rescrie functia de la exercitiul 3, 
astfel incat sa returneze rezultatul.
"""
print("ex 6 - rezolvare")


def patrat(numar):
    rezultat_patrat = numar ** 2
    return rezultat_patrat


# Exemplu de utilizare
numar = 8
rezultat_patrat = patrat(numar)
print(f"Pătratul numărului {numar} este: {rezultat_patrat}")
"""
EX7: Rescrie functia de la exercitiul 4, 
astfel incat sa returneze rezultatul.
"""
print("ex 7 - rezolvare")


def imparte(numar1, numar2):
    if numar2 == 0:
        return "Eroare: Împărțirea la zero nu este permisă."
    else:
        return numar1 / numar2


# Exemplu de utilizare
rezultat = imparte(10, 2)
print(f"Rezultatul împărțirii este: {rezultat}")
"""
EX8: Scrie o functie care ia ca parametru un numar intreg
si returneaza True daca numarul e par
si False daca numarul e impar.
"""
print("ex 8 - rezolvare")


def este_par(numar_par):
    return numar_par % 2 == 0


# Exemplu de utilizare
numar = 4
rezultat = este_par(numar)
print(f"Numărul {numar} este par: {rezultat}")