"""
Exercitii din cursul Cicluri Repetitive
# FOR EACH, BREAK, CONTINUE
"""

culori = ["rosu", "albastru", "galben", "mov"]

for culoare in culori:
    print(f"Culoarea mea preferata este {culoare}")

"""
EX5:
2. Se da lista:
produse = [
    {
        'nume produs': 'Rosii',
        'pret': 5
    },
    {
        'nume produs': 'Paine',
        'pret': 8
    },
    {
        'nume produs': 'Lapte',
        'pret': 6
    },
    {
        'nume produs': 'Cafea'
    }
]
Sa se afiseze toate produsele care au pretul mai mare de 5 lei.
"""

# Lista de produse
produse = [
    {
        'nume produs': 'Rosii',
        'pret': 5
    },
    {
        'nume produs': 'Paine',
        'pret': 8
    },
    {
        'nume produs': 'Lapte',
        'pret': 6
    },
    {
        'nume produs': 'Cafea'
    }
]

# Iterăm prin fiecare produs din lista produse
for produs in produse:

# Verificăm dacă produsul are un preț și dacă prețul este mai mare de 5
    if 'pret' in produs and produs['pret'] > 5:
        print(produs['nume produs'])

# BREAK

for i in range(1, 50):
    if i == 3:
        break
    print(i)

"""
EX6: Sa se afiseze primul numar par din intervalul 1 - 10
(inclusiv capetele de interval).
"""

# Iterăm prin intervalul de la 1 la 10 inclusiv
for numar in range(1, 11):
    # Verificăm dacă numărul este par
    if numar % 2 == 0:
        print(f"Primul număr par din interval este: {numar}")
        break  # Oprim bucla după ce găsim primul număr par

"""
EX7:
Se da lista:
participanti = ['Maria', 'Ionela', 'Marius', 'Paul']
Folosind un ciclu repetitiv, cauta daca 'Marius' se afla in lista de participanti.
Dupa ce l-ai gasit intrerupe ciclul repetitiv.
"""

# Lista de participanți
participanti = ['Maria', 'Ionela', 'Marius', 'Paul']

# Iterăm prin fiecare participant din lista participanți
for participant in participanti:
    # Verificăm dacă participantul curent este 'Marius'
    if participant == 'Marius':
        print(f"{participant} se află în lista de participanți.")
        break  # Oprim bucla după ce l-am găsit pe 'Marius'

# CONTINUE

for i in range(5):
    if i == 3:
        continue
    print(i)

"""
EX8: 1. Se da lista:
numere = [1, 2, 3, 4, 5, 6, 7]
Afiseaza toate elementele din lista numere,
cu exceptia numerelor 3 si 5
"""

# Lista de numere
numere = [1, 2, 3, 4, 5, 6, 7]

# Iterăm prin fiecare element din lista numere
for numar in numere:
    # Verificăm dacă numărul nu este 3 și nici 5
    if numar != 3 and numar != 5:
        print(numar)


