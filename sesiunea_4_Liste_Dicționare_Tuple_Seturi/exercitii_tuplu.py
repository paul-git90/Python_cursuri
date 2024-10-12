"""
Exercitii din curs: Structuri de date
    Tuplu - ordonata, imutabila, nu poate fi editata, elementele pot fi accesate dupa index.
Un tuplu în Python este o colecție ordonată și imuabilă de elemente. Spre deosebire de liste, tuplurile nu pot fi
modificate după ce au fost create, ceea ce le face utile pentru stocarea datelor care nu trebuie să fie schimbate.
Tuplurile sunt foarte utile în scenarii unde se dorește protejarea datelor de modificări accidentale și pentru
optimizarea performanței programului.
"""
"""
EX6:
Se da urmatoarea structura de date:
locatie = (44.34, 12.456)
a. Verifica tipul structurii de date
b. Este aceasta structura de date ordonata?
c. Este aceasta structura de date mutabila?
d. Determina lungimea structurii de date.
e. Salveaza a doua valoare intr-o variabila.
Verifica daca aceasta este mai mare de 13, si afiseaza
un mesaj corespunzator.
"""
locatie = (44.34, 12.456)
print(type(locatie))
print(locatie[0])
print(len(locatie))
locatie_sec = locatie[1]
print(locatie_sec)
if locatie_sec > 13:
    print(True)
else:
    print(False)


"""
Defineste un tuplu si exploreaza metodele ajutatoare ale tuplurilor
"""
# Definirea unui tuplu
numere = (1, 2, 2, 3, 4)

# Count: Returnează numărul de apariții ale unui element în tuplu
numar_de_doi = numere.count(2)
print(f"Numărul 2 apare de {numar_de_doi} ori în tuplu.")  # Output: 2

# Index: Returnează indexul primei apariții a unui element în tuplu
index_de_trei = numere.index(3)
print(f"Numărul 3 apare prima dată la indexul {index_de_trei}.")  # Output: 3

# Length: Returnează numărul de elemente din tuplu
lungime_tuplu = len(numere)
print(f"Tuplul are {lungime_tuplu} elemente.")  # Output: 5

# Minimum: Returnează elementul cu valoarea minimă din tuplu
valoare_minima = min(numere)
print(f"Valoarea minimă din tuplu este {valoare_minima}.")  # Output: 1

# Maximum: Returnează elementul cu valoarea maximă din tuplu
valoare_maxima = max(numere)
print(f"Valoarea maximă din tuplu este {valoare_maxima}.")  # Output: 4

# Sum: Returnează suma elementelor din tuplu (dacă sunt numerice)
suma_tuplu = sum(numere)
print(f"Suma elementelor din tuplu este {suma_tuplu}.")  # Output: 12

# Conversie la tuplu: Conversia altor structuri de date (liste, seturi) în tupluri
lista = [1, 2, 3]
tuplu_convertit = tuple(lista)
print(f"Lista convertită la tuplu este {tuplu_convertit}.")  # Output: (1, 2, 3)

# Definirea unui tuplu cu mai multe tipuri de date
tuplu_mixt = (1, "text", 3.14, True)

# Accesarea elementelor
primul_element = tuplu_mixt[0]
print(f"Primul element este {primul_element}.")  # Output: 1

# Slicing
sub_tuplu = tuplu_mixt[1:3]
print(f"Sub-tuplul este {sub_tuplu}.")  # Output: ('text', 3.14)

# Concatenarea tuplurilor
tuplu1 = (1, 2, 3)
tuplu2 = (4, 5, 6)
tuplu_concatenat = tuplu1 + tuplu2
print(f"Tuplul concatenat este {tuplu_concatenat}.")  # Output: (1, 2, 3, 4, 5, 6)

# Verificarea apartenenței unui element
exista_text = "text" in tuplu_mixt
print(f"Există 'text' în tuplu: {exista_text}.")  # Output: True

# Iterarea printr-un tuplu
for element in tuplu_mixt:
    print(element)

# all: verifică dacă toate elementele sunt adevărate
tuplu1 = (1, 2, 3)
print(all(tuplu1))  # Output: True

# any: verifică dacă oricare element este adevărat
tuplu2 = (0, 1, 2)
print(any(tuplu2))  # Output: True

# enumerate: returnează un iterator care produce tupluri de (index, element)
tuplu3 = ('a', 'b', 'c')
for index, valoare in enumerate(tuplu3):
    print(f"Index: {index}, Valoare: {valoare}")

# zip: combină două tupluri element cu element
tuplu4 = (1, 2, 3)
tuplu5 = ('a', 'b', 'c')
for element in zip(tuplu4, tuplu5):
    print(element)

# reversed: returnează un iterator care produce elementele în ordine inversă
tuplu6 = (1, 2, 3)
for element in reversed(tuplu6):
    print(element)

# sorted: returnează o listă sortată a elementelor din tuplu
tuplu7 = (3, 1, 2)
lista_sortata = sorted(tuplu7)
print(lista_sortata)  # Output: [1, 2, 3]