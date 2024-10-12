"""
Exercitii in echipa sesiunea 6 si 7: Cicluri repetitive
"""

"""
1.Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel'] 

Folosește un for că să iterezi prin toată lista și să afișezi;
●	Mașina mea preferată este x.
●	Fă același lucru cu un for each.
●	Fă același lucru cu un while.
"""
# Lista de mașini
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# Iterăm prin lista folosind un for
for i in range(len(masini)):
    print(f"** FOR - Mașina mea preferată este {masini[i]}")
# Iterăm prin lista folosind un for each
for masina in masini:
    print(f"** FOR EACH - Mașina mea preferată este {masina}")
# Iterăm prin lista folosind un while
i = 0
while i < len(masini):
    print(f"** WHILE - Mașina mea preferată este {masini[i]}")
    i += 1

"""
2. Aceeași listă:
Folosește un for else
În for
-	Modifică elementele din listă astfel încât să fie scrise cu majuscule, exceptând primul și ultimul.
În else:
-	Printează lista.
"""
# Lista de mașini
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# Iterăm prin listă folosind un for else
for i in range(1, len(masini) - 1):
    masini[i] = masini[i].upper()
else:
    # Printează lista modificată
    print(masini)

"""
3. Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Iterează prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
   Printează ‘am găsit mașina dorită de dvs’
   Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
   Printează ‘Am găsit mașina X. Mai căutam‘
"""
# Lista de mașini
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# Iterăm prin lista de mașini
for masina in masini:
    if masina == 'Mercedes':
        print('Am găsit mașina dorită de dvs')
        break  # Ieșim din ciclu dacă am găsit Mercedes
    else:
        print(f'Am găsit mașina {masina}. Mai căutăm')

"""
4. Aceeași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu excepția Trabant și Lăstun. 
-   Dacă mașina e Trabant sau Lăstun:
    Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
-	Printează S-ar putea să vă placă mașina x.
"""
# Lista de mașini
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# Iterăm prin lista de mașini
for masina in masini:
    if masina == 'Trabant' or masina == 'Lăstun':
        continue  # Sărim peste Trabant și Lăstun
    print(f'S-ar putea să vă placă mașina {masina}.')

"""
5. Modernizează parcul de mașini:
●	Crează o listă goală, masini_vechi.
●	Iterează prin mașini.
●	Când găsesti Lăstun sau Trabant:
●	Salvează aceste mașini în masini_vechi.
●	Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
●	Printează Modele vechi: x.
●	Modele noi: x.
"""
# Lista inițială de mașini
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# Creăm o listă goală pentru mașinile vechi
masini_vechi = []
# Iterăm prin lista inițială de mașini
for i in range(len(masini)):
    if masini[i] == 'Lăstun' or masini[i] == 'Trabant':
        masini_vechi.append(masini[i])  # Salvăm mașinile vechi în lista masini_vechi
        masini[i] = 'Tesla'  # Suprascriem cu 'Tesla'
# Printează modelele vechi și modelele noi
print(f'Modele vechi: {masini_vechi}')
print(f'Modele noi: {masini}')

"""
6. Având dict:
pret_masini = {
    'Dacia': 6800,
    'Lăstun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}

Vine un client cu un buget de 15000 euro.
●	Prezintă doar mașinile care se încadrează în acest buget.
●	Iterează prin dict.items() și accesează mașina și prețul.
●	Printează Pentru un buget de sub 15000 euro puteți alege mașină xLastun
"""
# Dicționarul cu prețurile mașinilor
pret_masini = {
    'Dacia': 6800,
    'Lăstun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
# Bugetul clientului
buget = 15000
# Iterăm prin dict.items() pentru a accesa mașina și prețul
for masina, pret in pret_masini.items():
    if pret <= buget:
        print(f'Pentru un buget de sub {buget} euro puteți alege mașina {masina}')

"""
7. Având lista:
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
●	Iterează prin ea.
●	Afișează de câte ori apare 3 (nu ai voie să folosești count).
"""
# Lista de numere
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# Variabilă pentru a contoriza aparițiile valorii 3
counter = 0
# Iterăm prin lista de numere
for numar in numere:
    if numar == 3:
        counter += 1
# Afișăm de câte ori apare 3
print(f'Numărul 3 apare de {counter} ori în listă.')

"""
8. Aceeași listă:
●	Iterează prin ea
●	Calculează și afișează suma numerelor (nu ai voie să folosești sum).
"""
# Lista de numere
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# Variabilă pentru a stoca suma numerelor
suma = 0
# Iterăm prin lista de numere
for numar in numere:
    suma += numar
# Afișăm suma numerelor
print(f'Suma numerelor din listă este: {suma}')

"""
9. Aceeași listă:
●	Iterează prin ea.
●	Afișază cel mai mare număr (nu ai voie să folosești max).
"""
# Lista de numere
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# Inițializăm variabila pentru cel mai mare număr cu primul element din listă
cel_mai_mare_numar = numere[0]
# Iterăm prin lista de numere
for numar in numere:
    if numar > cel_mai_mare_numar:
        cel_mai_mare_numar = numar
# Afișăm cel mai mare număr
print(f'Cel mai mare număr din listă este: {cel_mai_mare_numar}')

"""
10. Aceeași listă:
●	Iterează prin ea.
●	Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
"""
# Lista de numere
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# Iterăm prin lista de numere
for i in range(len(numere)):
    if numere[i] > 0:
        numere[i] = -numere[i]
# Afișăm lista modificată
print(f'Lista modificată: {numere}')

"""
11.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Itereaza prin listă alte_numere 
Populează corect celelalte liste
Afișează cele 4 liste la final
"""
# Lista de numere
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# Liste pentru numere pare, impare, pozitive și negative
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
# Iterăm prin lista alte_numere
for numar in alte_numere:
    if numar % 2 == 0:
        numere_pare.append(numar)
    else:
        numere_impare.append(numar)

    if numar > 0:
        numere_pozitive.append(numar)
    elif numar < 0:
        numere_negative.append(numar)

# Afișăm cele 4 liste
print(f'Numere pare: {numere_pare}')
print(f'Numere impare: {numere_impare}')
print(f'Numere pozitive: {numere_pozitive}')
print(f'Numere negative: {numere_negative}')

"""
12. Aceeași listă:
Ordonează crescător lista fară să folosești sort.
"""
# Lista de numere
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# Implementarea algoritmului de selection sort
for i in range(len(alte_numere)):
    min_index = i
    for j in range(i+1, len(alte_numere)):
        if alte_numere[j] < alte_numere[min_index]:
            min_index = j
    alte_numere[i], alte_numere[min_index] = alte_numere[min_index], alte_numere[i]
# Afișăm lista sortată
print(f'Lista sortată crescător: {alte_numere}')

"""
13. Ghicitoare de număr:
numar_secret = Generați un număr random între 1 și 30
Numar_ghicit = None
Folosind un while
   User alege un număr
   Programul îi spune:
●	Nr secret e mai mare
●	Nr secret e mai mic
●	Felicitări! Ai ghicit!
"""
import random

# Generăm un număr secret între 1 și 30
numar_secret = random.randint(1, 30)

# Inițializăm numărul ghicit cu None pentru a începe ciclul
numar_ghicit = None

# Mesaj de început
print("Ghicitoare de număr! Ghicește numărul secret între 1 și 30.")

# Începem ghicirea cu while
while numar_ghicit != numar_secret:
    # User alege un număr
    numar_ghicit = int(input("Introdu un număr: "))

    # Verificăm numărul ghicit
    if numar_ghicit < numar_secret:
        print("Nr secret e mai mare.")
    elif numar_ghicit > numar_secret:
        print("Nr secret e mai mic.")
    else:
        print("Felicitări! Ai ghicit!")

# La final, după ce se ghicește numărul secret, se afișează un mesaj de finalizare
print(f"Numărul secret era: {numar_secret}. Joc încheiat!")

"""
14. Alege un număr de la tastatură.
Scrie un program care să genereze în consolă următoarea piramidă
Varianta 1:

1
22
333
4444
55555
666666
7777777

Varianta 2:

1
22
333
"""
# Varianta 1: Full Pyramid
num = int(input("Introduceți un număr: "))

for i in range(1, num + 1):
    print(str(i) * i)

# Varianta 2: Half Pyramid
num = int(input("Introduceți un număr: "))

for i in range(1, min(num + 1, 4)):
    print(str(i) * i)

"""
15.
tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
Iterează prin listă 2d
Printează ‘Cifra curentă este x’
"""
# Definim lista 2D pentru tastatura telefon
tastatura_telefon = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# Iterăm prin lista 2D
for row in tastatura_telefon:
    print(f'Valoarea sublistei definita ca row este {row}')
    for cifra in row:
        print(f'Cifra curentă este {cifra}')
