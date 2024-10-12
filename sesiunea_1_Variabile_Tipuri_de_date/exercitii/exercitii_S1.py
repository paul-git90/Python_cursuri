'''
exercitii sesiunea 1
'''
# ex. 1
# 1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
'''
O variabila este un container, o adresa unde se stocheaza valori
'''
# ex. 2
# 2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de variabilă:
# -	string
# -	int
# -	float
# -	bool
string = 'string'
print(string)
integer = 1
print(integer)
float_1 = 1.102
print(float_1)
bool_1 = True
print(bool_1)
# ex. 3
# 3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.
print(type(string))
print(type(integer))
print(type(float_1))
print(type(bool_1))
# ex. 4
# 4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în aceeași variabilă (suprascriere):
# -	Verifică tipul acesteia.
print(float_1)
float_1 = round(float_1)
print(float_1)
print(type(float_1))
# ex. 5
# 5. Folosește print() și printează în consolă 4 propoziții folosind cele 4 variabile.
# Rezolvă nepotrivirile de tip prin ce modalitate dorești.
print(f'I have one {string}.')
print(f'I have {integer} car.')
print(f'Every season is {float_1} time a year.')
print(f'My result is {bool_1}.')
print(f'My {string} is {integer} time, and {float_1} time is {bool_1}.')
# ex. 6
# 6. Citește de la tastatură:
# -	numele;
# -	prenumele.
#     Afișează: 'Numele complet are x caractere'.
interogare = (input(f'Va rugam introduceti numele si prenumele: '))
print(f'Numele dvs. este: {interogare}')
print(len(interogare))
interogare = (interogare.lower())
print(interogare.count('a'))
################################################################
"""
EX1: 
a. Defineste o variabila de tip int, numita 'latime'.
b. Defineste o variabila de tip string, numita 'descriere'.
c. Defineste 2 variabile de tip float, numite 'pret' si 'discount'.
d. Defineste o variabila de tip bool, numita 'initializat' care are valoarea True.
e. Printeaza variabilele definite la punctele anterioare.
"""
latime = int(10)
descriere = str('Triunghi')
pret_triunghi = float(23.99)
discount_triunghi = float(50)
initializat = bool(True)
print(f'Am initializat {initializat} o variabila {descriere} cu latime {latime} la '
      f'pretul de {pret_triunghi} cu discount {discount_triunghi}')

"""
EX2: Folosind o singura linie de cod, defineste 2 variabile, de tip int, cu valoarea 10.
"""
one_int = two_int = 10
print(one_int)
print(two_int)
print(f'{one_int} and {two_int}')

"""
EX3: Folosind o singura linie de cod, initializeaza/ defineste doua variabile de tip string cu valori diferite.
"""
portocala, mandarina = 'mare', 'mica'
print(portocala)
print(mandarina)
print(f'portocala este {portocala}, iar mandarina este {mandarina}')

"""
EX4: Defineste doua variabile de tip string, numite 'nume', respectiv 'pret'.
Afiseaza in consola un mesaj care sa contina cele doua variabile.
"""
nume = 'Ciocolata'
pret = 4.5
print(f'{nume} costa {pret} lei.')

"""
EX5:
a. Defineste doua variabile: nume (string) si varsta (int).
b. Folosind f-string, afiseaza in consola, o propozitie care sa contina cele doua variabile.
"""
NUME = "Paul"
VARSTA = 34
print(f'Clientul {NUME} are varsta de {VARSTA} ani.')

# ex. 6 / 7 / 8

integer = 30
print(integer)
print(type(integer))

integer = str(integer)
print(integer)
print(type(integer))

my_string = '10'
print(my_string)
print(type(my_string))

my_string = int(my_string)
print(my_string)
print(type(my_string))

my_string = float(my_string)
print(my_string)
print(type(my_string))

my_string = bool(my_string)
print(my_string)
print(type(my_string))

"""
EX9: Citeste de la tastatura un nume de produs.
Salveaza rezultatul intr-o variabila.
Afiseaza un mesaj care sa contina variabila salvata.
"""
produs = input("Ce produs doriti? ")
print(f'Produsul ales este: {produs}.')

"""
EX10: Citeste de la tastatura un pret. Obliga utilizatorul sa introduca pretul ca si numar zecimal.
Salveaza rezultatul intr-o variabila.
Afiseaza un mesaj care sa contina variabila salvata.
"""
pret_produs = int(input("Introduceti pretul oferit: "))
print(f'Pretul oferit este: {pret_produs:.3f}')  # .3f indica cate zecimale sa afiseze la finalul cifrei nu schimba in float
print(type(pret_produs))